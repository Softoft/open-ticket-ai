---
description: Explora la clase `Orchestrator` de OpenTicketAI, un componente central para automatizar
  los flujos de trabajo de procesamiento de tickets. Este módulo de Python gestiona el ciclo de vida completo de
  los pipelines, incluyendo la instanciación mediante inyección de dependencias, el procesamiento individual de tickets
  y la ejecución programada para una automatización continua.
---
# Documentación para `**/ce/run/managers/*.py`

## Módulo: `open_ticket_ai\src\ce\run\managers\orchestrator.py`

Utilidades de orquestación de alto nivel.

### <span style='text-info'>class</span> `Orchestrator`

Orquesta la ejecución de los pipelines de procesamiento de tickets.
Esta clase gestiona el ciclo de vida de los pipelines, incluyendo:
- Instanciación de pipelines mediante inyección de dependencias
- Procesamiento individual de tickets
- Ejecución programada de pipelines

**Parámetros:**

- **`config`** () - Ajustes de configuración para el orquestador
- **`container`** () - Contenedor de inyección de dependencias que proporciona las instancias de los pipelines
- **`_logger`** () - Instancia de logger para las operaciones de orquestación
- **`_pipelines`** () - Diccionario que mapea los IDs de los pipelines a sus instancias


::: details #### <Badge type="info" text="method"/> <span class='text-warning'>def</span> `__init__(self, config: OpenTicketAIConfig, container: AbstractContainer)`
Inicializa el Orchestrator con la configuración y el contenedor de DI.

**Parámetros:**

- **`config`** () - Ajustes de configuración para el orquestador.
- **`container`** () - Contenedor de inyección de dependencias que proporciona las instancias de los pipelines.

:::


::: details #### <Badge type="info" text="method"/> <span class='text-warning'>def</span> `process_ticket(self, ticket_id: str, pipeline: Pipeline) -> PipelineContext`
Ejecuta un pipeline para un ticket específico.
Crea un contexto de procesamiento y ejecuta el pipeline especificado para procesar
el ticket dado. Este es el método principal para el procesamiento individual de tickets.

**Parámetros:**

- **`ticket_id`** () - Identificador único del ticket a procesar.
- **`pipeline`** () - Instancia del pipeline a ejecutar.

**Devuelve:** (`PipelineContext`) - El contexto de ejecución que contiene los resultados y el estado
después de la ejecución del pipeline.

:::


::: details #### <Badge type="info" text="method"/> <span class='text-warning'>def</span> `build_pipelines(self) -> None`
Instancia todos los objetos de pipeline configurados.
Utiliza el contenedor de inyección de dependencias para crear instancias de pipeline
basadas en la configuración. Rellena el registro interno de pipelines
con los mapeos de ID de pipeline a instancia.

:::


::: details #### <Badge type="info" text="method"/> <span class='text-warning'>def</span> `set_schedules(self) -> None`
Configura la ejecución programada para todos los pipelines.
Realiza las siguientes operaciones:
1. Construye los pipelines si no han sido instanciados previamente
2. Configura la ejecución periódica para cada pipeline según su
   configuración de programación utilizando la librería `schedule`

La programación utiliza los siguientes parámetros de configuración:
- interval: Valor numérico del intervalo
- unit: Unidad de tiempo (p. ej., minutos, horas, días)

Nota:
- Utiliza el patrón `schedule.every(interval).unit` para la programación
- Pasa un contexto de ticket_id vacío durante las ejecuciones programadas

:::


---