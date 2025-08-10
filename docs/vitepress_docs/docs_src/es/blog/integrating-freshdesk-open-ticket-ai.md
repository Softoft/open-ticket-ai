---
description: Aprenda a integrar Open Ticket AI (OTAI) on-premise con Freshdesk para una clasificación de tickets potente y automatizada. Este documento detalla la creación de un `TicketSystemAdapter` personalizado en Python para conectar los modelos de IA de OTAI con la REST API de Freshdesk. Automatice el triaje de tickets actualizando los tickets de Freshdesk con categorías y prioridades predichas por la IA, integrando la clasificación inteligente directamente en su flujo de trabajo de soporte.
---
# Integración de IA de Freshdesk con Open Ticket AI

Open Ticket AI (OTAI) es un sistema local, on-premise, de **clasificación de tickets** (también llamado ATC Community Edition) que automatiza la categorización y el enrutamiento de tickets de soporte. Freshdesk es una popular plataforma de soporte al cliente basada en la nube con sus propias herramientas de IA, que ofrece gestión de tickets, flujos de trabajo e informes. Al escribir un *TicketSystemAdapter* personalizado, puede integrar OTAI con Freshdesk y actualizar los tickets de Freshdesk automáticamente a través de su REST API. Esto habilita el triaje de tickets impulsado por IA dentro del entorno de Freshdesk. En el pipeline de Open Ticket AI, la etapa final es un **TicketSystemAdapter** que aplica las predicciones de la IA al sistema de tickets mediante llamadas REST. Para extender OTAI para Freshdesk, se implementa un `FreshdeskAdapter` que hereda de `TicketSystemAdapter` e implementa métodos para consultar y actualizar tickets en Freshdesk.

&#x20;*Figura: Diagrama de clases UML de la arquitectura de Open Ticket AI. La clase abstracta `TicketSystemAdapter` proporciona una base para adaptadores específicos del sistema (p. ej., un OTOBOAdapter) que se conectan a sistemas de tickets externos.* La arquitectura de OTAI es modular: los tickets entrantes pasan por clasificadores NLP y un **TicketSystemAdapter** escribe los resultados de vuelta en el sistema de tickets. La documentación explica que `TicketSystemAdapter` es una clase base abstracta "que todos los adaptadores de sistemas de tickets concretos deben implementar" para interactuar con diferentes plataformas de tickets. Las subclases deben implementar tres métodos `async` principales: `update_ticket(ticket_id, data)`, `find_tickets(query)` y `find_first_ticket(query)`. En la práctica, crearías una nueva clase de Python, por ejemplo, `class FreshdeskAdapter(TicketSystemAdapter)`, y sobrescribirías esos métodos. Por ejemplo:

```python
import aiohttp

from open_ticket_ai.src.ticket_system_integration.ticket_system_adapter import TicketSystemAdapter


class FreshdeskAdapter(TicketSystemAdapter):
    async def update_ticket(self, ticket_id: str, data: dict) -> dict:
        # Construct Freshdesk API URL for updating a ticket
        base = f"https://{self.config.freshdesk_domain}.freshdesk.com"
        url = f"{base}/api/v2/tickets/{ticket_id}"
        auth = aiohttp.BasicAuth(self.config.freshdesk_api_key, password="X")
        async with aiohttp.ClientSession(auth=auth) as session:
            async with session.put(url, json=data) as resp:
                return await resp.json()

    async def find_tickets(self, query: dict) -> list[dict]:
        # Use Freshdesk List Tickets or Search API to retrieve tickets matching query
        base = f"https://{self.config.freshdesk_domain}.freshdesk.com"
        params = {k: v for k, v in query.items()}
        url = f"{base}/api/v2/tickets"
        async with aiohttp.ClientSession(
                auth=aiohttp.BasicAuth(self.config.freshdesk_api_key, password="X"),
        ) as session:
            async with session.get(url, params=params) as resp:
                data = await resp.json()
                return data.get('tickets', [])

    async def find_first_ticket(self, query: dict) -> dict:
        tickets = await self.find_tickets(query)
        return tickets[0] if tickets else None
```

El código anterior muestra un **FreshdeskAdapter** simple. Extrae el dominio de Freshdesk (el nombre de la empresa) y la clave de API de la configuración de OTAI (`self.config`) que se inyecta en tiempo de ejecución. Luego, utiliza `aiohttp` de Python para realizar llamadas HTTP `async`. El método `update_ticket` emite un `PUT` a `https://<dominio>.freshdesk.com/api/v2/tickets/<id>` con el payload JSON de los campos a cambiar. El método `find_tickets` utiliza `GET` en `/api/v2/tickets` con parámetros de consulta (o podrías llamar a `/api/v2/search/tickets` para búsquedas más complejas). La API de Freshdesk requiere autenticación básica (basic auth): tu clave de API (de tu perfil de Freshdesk) se utiliza como nombre de usuario y cualquier contraseña (a menudo simplemente "X") como la contraseña.

**Pasos Clave para Integrar Freshdesk:**

*   *Configurar el acceso a la API:* Inicie sesión en Freshdesk y obtenga su **clave de API** (API key) del perfil (esta clave se utiliza para autenticar las solicitudes a la API). Anote también su dominio de Freshdesk (el subdominio en su URL de Freshdesk).
*   *Implementar el Adaptador:* Cree una clase `FreshdeskAdapter` que extienda `TicketSystemAdapter` e implemente `update_ticket`, `find_tickets` y `find_first_ticket`. En estos métodos, utilice los endpoints de la REST API de Freshdesk (p. ej., `GET /api/v2/tickets` y `PUT /api/v2/tickets/{id}`).
*   *Configurar OTAI:* Actualice el archivo `config.yml` de OTAI para incluir el `FreshdeskAdapter` y su configuración (como `freshdesk_domain` y `freshdesk_api_key`). Gracias a la configuración de inyección de dependencias (dependency-injection) de OTAI, el nuevo adaptador se cargará en tiempo de ejecución.
*   *Ejecutar la Clasificación:* Inicie Open Ticket AI (p. ej., mediante `python -m open_ticket_ai.src.ce.main start`). A medida que se obtienen nuevos tickets, el pipeline los clasificará y luego llamará a su `FreshdeskAdapter.update_ticket(...)` para escribir la cola o prioridad predicha de vuelta en Freshdesk.

Usando este adaptador personalizado, los tickets de Freshdesk fluyen a través del pipeline de OTAI como cualquier otro sistema de tickets. Una vez que OTAI asigna un ID de cola o una prioridad, la llamada a `update_ticket` lo enviará de vuelta a Freshdesk a través de su API. Esto permite a los usuarios de Freshdesk aprovechar los modelos de IA de OTAI para la *clasificación automatizada de tickets* sin dejar de trabajar dentro de la plataforma Freshdesk. La flexible REST API de Freshdesk (que admite la búsqueda, el listado, la creación y la actualización de tickets) hace que esta integración sea sencilla. Siguiendo el patrón de adaptador de OTAI y las convenciones de la API de Freshdesk, los desarrolladores pueden integrar sin problemas el triaje de tickets impulsado por IA en Freshdesk sin depender de una IA propietaria en la nube, manteniendo todos los datos locales si se desea.

**Referencias:** La documentación de Open Ticket AI explica su arquitectura de adaptadores y la interfaz `TicketSystemAdapter`. La descripción general de la arquitectura de OTAI muestra el paso del adaptador en el pipeline. La guía de la API y los blogs para desarrolladores de Freshdesk documentan cómo autenticarse (con una clave de API) y llamar a los endpoints de tickets. En conjunto, estas fuentes describen los pasos para construir una integración personalizada con Freshdesk.