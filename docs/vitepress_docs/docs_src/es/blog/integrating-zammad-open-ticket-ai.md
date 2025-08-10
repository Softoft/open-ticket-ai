---
description: Aprenda a integrar OpenTicketAI con Zammad para la clasificación y enrutamiento automatizado de tickets on-premise. Esta guía detalla cómo crear un ZammadAdapter usando la REST API para obtener tickets, procesarlos a través de un pipeline de IA y actualizar automáticamente su cola, prioridad y notas.
---
# Integración de OpenTicketAI con Zammad para la Clasificación Automatizada de Tickets

OpenTicketAI es un **clasificador de tickets por IA** on-premise que automatiza la categorización, el enrutamiento y la priorización de los tickets de soporte. Para integrarlo con Zammad, implementamos un **ZammadAdapter** que extiende la interfaz `TicketSystemAdapter` de OpenTicketAI. Este adaptador utiliza la REST API de Zammad para *obtener* tickets de Zammad, *procesarlos a través del pipeline de OpenTicketAI* y *actualizar* el ticket (cola, prioridad, comentarios) basándose en las predicciones de la IA. Los componentes clave se ilustran en la arquitectura: la **AdapterFactory** de OpenTicketAI crea el adaptador apropiado (p. ej., ZammadAdapter) para comunicarse vía REST con el sistema de tickets. El pipeline obtiene los tickets, los clasifica y, finalmente, el adaptador del sistema de tickets actualiza Zammad a través de su API.

La arquitectura de OpenTicketAI utiliza un pipeline modular donde cada ticket es procesado por una serie de pasos (pipes). La etapa final del *Adaptador del Sistema de Tickets* aplica las actualizaciones (cola, prioridad, notas) al sistema externo a través de la REST API. En la práctica, registras tu `ZammadAdapter` en la configuración de inyección de dependencias para que el paso **BasicTicketFetcher** lo use para cargar tickets, y el paso **GenericTicketUpdater** lo use para aplicar las actualizaciones.

## Descripción General del Pipeline de OpenTicketAI

OpenTicketAI se ejecuta en un *pipeline* que transforma los datos del ticket paso a paso. Un flujo simplificado es:

1.  **Preprocesador** – fusiona/limpia `subject` y `body`.
2.  **Transformador / Tokenizador** – prepara el texto para la IA.
3.  **Clasificador de Cola** – predice la cola/grupo de destino.
4.  **Clasificador de Prioridad** – predice el nivel de prioridad.
5.  **Postprocesador** – aplica umbrales, elige acciones.
6.  **Adaptador del Sistema de Tickets** – actualiza el ticket en Zammad a través de la REST API.

Cada etapa toma un objeto `PipelineContext` (que contiene `ticket_id` y un diccionario `data`) y lo enriquece. Por ejemplo, después de que se ejecutan los clasificadores, el `data` del contexto podría tener claves como `new_queue`, `new_priority`, o un `article` (comentario) para añadir. El paso **GenericTicketUpdater** busca entonces una entrada `update_data` en el contexto y llama al adaptador para aplicar esos campos al ticket. Este diseño facilita la adición de nuevos pasos (p. ej., un paso de seudonimización) o la personalización de la lógica de actualización. El orquestador gestiona estos *AttributePredictors* (fetcher, preparer, AI service, modifier) basándose en la configuración YAML.

## TicketSystemAdapter y ZammadAdapter

OpenTicketAI define una clase base abstracta `TicketSystemAdapter` que todas las integraciones deben extender. Declara métodos principales como:

*   `async update_ticket(ticket_id: str, data: dict) -> dict | None`: **Actualiza** los campos de un ticket (p. ej., cola, prioridad, añadir nota). Debe manejar actualizaciones parciales y devolver el objeto del ticket actualizado.
*   `async find_tickets(query: dict) -> list[dict]`: **Busca** tickets que coincidan con una consulta. El formato de la consulta es específico del adaptador, pero esto debería devolver una lista de los tickets coincidentes.
*   `async find_first_ticket(query: dict) -> dict | None`: Utilidad para devolver solo la primera coincidencia.

Un **ZammadAdapter** heredará de esta clase e implementará estos métodos usando la API de Zammad. Típicamente, contendrá la configuración (URL base, credenciales) inyectada a través de un `SystemConfig`. Por ejemplo:

```python
from open_ticket_ai.src.ticket_system_integration.ticket_system_adapter import TicketSystemAdapter
import httpx


class ZammadAdapter(TicketSystemAdapter):
    def __init__(self, config):
        super().__init__(config)
        # Assume config.zammad contains URL and auth info
        self.base_url = config.zammad.base_url.rstrip('/')
        self.auth = (config.zammad.user, config.zammad.password)

    async def find_tickets(self, query: dict) -> list[dict]:
        # Use Zammad search API (e.g. full-text search or filters).
        async with httpx.AsyncClient(auth=self.auth) as client:
            params = {"query": query.get("search", "")}
            res = await client.get(f"{self.base_url}/api/v1/tickets/search", params=params)
            res.raise_for_status()
            return res.json()  # list of matching tickets (each as dict)

    async def find_first_ticket(self, query: dict) -> dict | None:
        tickets = await self.find_tickets(query)
        return tickets[0] if tickets else None

    async def update_ticket(self, ticket_id: str, data: dict) -> dict | None:
        # Send PUT to update the ticket. Data can include 'group', 'priority', etc.
        url = f"{self.base_url}/api/v1/tickets/{ticket_id}"
        async with httpx.AsyncClient(auth=self.auth) as client:
            res = await client.put(url, json=data)
            if res.status_code == 200:
                return res.json()  # updated ticket object
            return None
```

*Cita:* La clase base requiere estos métodos. En este ejemplo usamos `httpx.AsyncClient` (ya que los métodos son `async`), pero podrías usar `requests` de manera similar en un contexto síncrono. Por ejemplo, obtener todos los tickets podría ser tan simple como `requests.get(f"{base_url}/api/v1/tickets", auth=(user, pwd))`.

### Obteniendo Tickets de Zammad

La REST API de Zammad proporciona endpoints para listar y buscar tickets. Una forma sencilla de obtener tickets recientes o coincidentes es a través de:

*   **Listar Todos (paginado)**: `GET /api/v1/tickets` devuelve un array de objetos de ticket.
*   **Buscar**: `GET /api/v1/tickets/search?query=...` soporta búsquedas de texto completo o por campos, devolviendo los tickets coincidentes en formato JSON (y `expand=true` puede resolver campos relacionados).

Tu implementación de `find_tickets` puede usar estos. Por ejemplo, para filtrar por estado o asunto:

```python
async with httpx.AsyncClient(auth=self.auth) as client:
    res = await client.get(f"{base_url}/api/v1/tickets/search", params={"query": "state:open OR state:new"})
    res.raise_for_status()
    tickets = res.json()  # a list of dicts
```

Luego, envuelve o devuelve esos en el formato que OpenTicketAI espera (una lista de diccionarios de tickets). El paso `BasicTicketFetcher` llamará a esto usando el ID del ticket del `PipelineContext` para cargar un ticket antes de procesarlo.

### Actualizando Tickets de Zammad

Después de la clasificación, actualizamos Zammad usando su API de **Actualización de Ticket**. Zammad permite cambiar campos como el grupo (cola) y la prioridad, e incluso añadir una nota interna o un artículo en una sola llamada. Por ejemplo, el siguiente payload (enviado vía `PUT /api/v1/tickets/{id}`) establece un nuevo grupo y prioridad y añade un artículo interno:

```json
{
  "group": "Sales",
  "state": "open",
  "priority": "3 high",
  "article": {
    "subject": "AI Insight",
    "body": "Sentiment analysis: negative tone detected.",
    "internal": true
  }
}
```

Esto reasignaría el ticket al grupo “Ventas”, lo establecería en prioridad alta y adjuntaría una nueva nota (comentario interno) con información de la IA. En código, nuestro `update_ticket` podría hacer:

```python
await client.put(f"{base_url}/api/v1/tickets/{ticket_id}", json={
    "group": new_queue,
    "priority": f"{priority_level} {priority_label}",
    "article": {
        "subject": "Auto-classified Ticket",
        "body": f"Queue={new_queue}, Priority={priority_label}",
        "internal": True
    }
})
```

La respuesta será el JSON completo del ticket actualizado si el estado es 200. Si solo necesitas publicar un comentario o nota, incluye el bloque `article` como se muestra arriba. Alternativamente, actualizaciones más pequeñas (como solo establecer una nota) pueden usar el campo “nota” del ticket o un endpoint de artículos separado, pero el `article` incluido en el PUT es conveniente.

## Integración del Pipeline en OpenTicketAI

Para conectar esto en el pipeline de OpenTicketAI, añades **pasos** (pipes) en `config.yml`. Por ejemplo:

*   **BasicTicketFetcher**: configurado con `ticket_system: ZammadAdapter`. Llama a `find_tickets`/`find_first_ticket` y rellena `context.data` con los campos del ticket.
*   **Preparer**: p. ej., `SubjectBodyPreparer` para combinar el texto del asunto y el cuerpo.
*   **Servicios de Inferencia de IA**: tus clasificadores personalizados de cola/prioridad (p. ej., un modelo de HuggingFace).
*   **GenericTicketUpdater**: configurado con `ticket_system: ZammadAdapter`. Busca `context.data["update_data"]` después de la inferencia y llama a `update_ticket`.

Por ejemplo, un paso (pipe) personalizado podría hacer:

```python
class QueuePriorityPredictor(Pipe):
    def process(self, context: PipelineContext) -> PipelineContext:
        subject = context.data.get("subject", "")
        body = context.data.get("body", "")
        queue_pred = my_queue_model.predict(subject + body)
        prio_pred = my_prio_model.predict(subject + body)
        # Prepare update data for Zammad
        context.data['update_data'] = {
            "group": queue_pred.group_name,
            "priority": f"{prio_pred.score} {prio_pred.label}",
            "article": {
                "subject": "AI Classification",
                "body": f"Assigned to {queue_pred.group_name}, Priority={prio_pred.label}",
                "internal": True
            }
        }
        return context
```

Esto prepara el `update_data` que usará GenericTicketUpdater.

Finalmente, la **AdapterFactory** (configurada mediante inyección de dependencias) se asegura de que `ticket_system: Zammad` cree una instancia de tu clase `ZammadAdapter`, inyectando la URL base y la autenticación desde `config.yml`. El paso **GenericTicketUpdater** llama entonces a `await adapter.update_ticket(id, update_data)`, aplicando tus cambios impulsados por la IA.

## Mejoras: Clasificación, Seudonimización y Notas

Más allá de la cola/prioridad básica, OpenTicketAI ofrece características para enriquecer la integración con Zammad:

*   **Clasificación de Cola y Prioridad:** Puedes entrenar modelos personalizados para colas o esquemas de prioridad específicos de Zammad. Los valores predichos se mapean a los grupos y prioridades de Zammad (por ejemplo, la API de prioridad usa el formato `"priority": "2 normal"`). Ajustando los umbrales en el **postprocesador**, también puedes descartar automáticamente predicciones de baja confianza o escalar tickets.

*   **Conectores de Seudonimización:** Para proteger la privacidad del usuario, puedes insertar un *paso de pipeline* personalizado antes de la inferencia que **seudonimice** o enmascare datos sensibles (p. ej., nombres, correos electrónicos) en el texto del ticket. Esto podría usar regex o servicios externos para reemplazar la PII con tokens. El texto enmascarado se clasifica entonces, y el ticket original se actualiza, asegurando que ningún contenido sensible salga de tu sistema.

*   **Creación de Notas/Artículos:** Puedes aprovechar la API de artículos de Zammad para registrar información de la IA o análisis de sentimiento. Como se mostró anteriormente, incluye un `article` en el payload de actualización para añadir comentarios. Alternativamente, podrías configurar un **paso de creación de notas** separado que, independientemente de si se actualiza la cola/prioridad, siempre añada una nota al ticket con las puntuaciones de confianza del modelo o el análisis de sentimiento. Estas notas ayudan a los agentes a entender *por qué* se tomó una decisión.

Cada mejora encaja de forma natural en el pipeline y es aplicada automáticamente por el GenericTicketUpdater a través del adaptador. Por ejemplo, después de ejecutar un paso de análisis de sentimiento, podrías hacer:

```python
context.data['update_data'] = {
    "article": {
        "subject": "Sentiment Score",
        "body": f"Sentiment polarity: {sentiment_score}",
        "internal": True,
    },
}
```

Luego, el adaptador lo publicará (POST) como un artículo en Zammad.

## Beneficios para la Automatización de Tickets en Zammad

Con esta integración, Zammad obtiene automatización on-premise impulsada por IA. Los tickets entrantes pueden ser auto-asignados a la cola correcta y recibir una prioridad preliminar, liberando a los equipos de soporte para que se centren en problemas urgentes. Debido a que OpenTicketAI se ejecuta localmente, los datos sensibles de los tickets permanecen internamente (importante para el cumplimiento normativo). Esta **integración de IA para Zammad** convierte el triaje manual en un proceso optimizado: mantienes el control total y la personalización (a través de la configuración y modelos personalizados) mientras aprovechas el pipeline de OpenTicketAI.

En resumen, implementar un **ZammadAdapter** implica heredar de `TicketSystemAdapter` y conectarlo al pipeline de OpenTicketAI. El adaptador utiliza la API de Zammad para operaciones CRUD de tickets (p. ej., `GET /tickets` y `PUT /tickets/{id}`). Una vez configurado, OpenTicketAI obtendrá continuamente tickets, los procesará a través de tu pila de modelos de IA y actualizará Zammad con la cola, prioridad y cualquier nota predicha. Esta integración de **IA para sistemas de tickets** dota a Zammad de clasificación y enrutamiento automatizados, haciendo realidad la visión de un clasificador de tickets por IA on-premise para equipos de soporte empresariales.

**Fuentes:** Documentación de la REST API de Zammad; documentación para desarrolladores de OpenTicketAI.