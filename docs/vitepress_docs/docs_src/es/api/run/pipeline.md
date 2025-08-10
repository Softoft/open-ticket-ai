---
description: 'Descubra un framework de pipeline modular de Python para construir flujos
  de trabajo de procesamiento de datos robustos. Esta documentación cubre los componentes
  principales: el orquestador `Pipeline`, las etapas individuales `Pipe` y el `PipelineContext`
  para la gestión de estado. Aprenda a implementar el procesamiento secuencial, manejar
  errores elegantemente, gestionar el estado de ejecución (RUNNING, SUCCESS, FAILED,
  STOPPED) y garantizar la seguridad de tipos con Pydantic.'
---
# Documentación para `**/ce/run/pipeline/*.py`

## Módulo: `open_ticket_ai\src\ce\run\pipeline\context.py`


### <span style='text-info'>class</span> `PipelineContext`

Objeto de contexto pasado entre las etapas del pipeline.
Esta clase genérica sirve como un contenedor para compartir estado y datos a través
de las diferentes etapas de un pipeline de procesamiento. Utiliza Pydantic para la validación
y serialización de datos.

El parámetro de tipo genérico `DataT` debe ser una subclase de `BaseModel`,
garantizando la seguridad de tipos para la carga útil de datos principal.

**Parámetros:**

- **`data`** (`DataT`) - La carga útil de datos principal que se procesa a través del pipeline.
Debe ser una instancia de un modelo de Pydantic que coincida con el tipo genérico.
- **`meta_info`** (`MetaInfo`) - Metadatos sobre la ejecución del pipeline, incluyendo
información de estado y detalles operativos.


::: details #### <Badge type="info" text="method"/> <span class='text-warning'>def</span> `stop_pipeline(self)`
Señala al pipeline que detenga el procesamiento.
Este método proporciona una forma controlada para que las etapas del pipeline indiquen
que el procesamiento debe detenerse. Actualiza los metadatos de estado del contexto
a `STOPPED`, que las etapas posteriores pueden verificar para terminar anticipadamente.

Nota:
    Este método modifica el estado del contexto pero no devuelve ningún valor.

:::


---

## Módulo: `open_ticket_ai\src\ce\run\pipeline\meta_info.py`


### <span style='text-info'>class</span> `MetaInfo`

Almacena metadatos sobre el estado de ejecución del pipeline.
Este modelo captura el estado actual de un pipeline junto con cualquier información
de error cuando ocurren fallos.

**Parámetros:**

- **`status`** () (por defecto: `RUNNING`) - Estado de ejecución actual del pipeline. Por defecto es RUNNING.
- **`error_message`** () - Mensaje de error detallado si el pipeline falló. None si tuvo éxito.
- **`failed_pipe`** () - Identificador del pipe específico que causó el fallo. None si tuvo éxito.


---

## Módulo: `open_ticket_ai\src\ce\run\pipeline\pipe.py`


### <span style='text-info'>class</span> `Pipe`

Interfaz para todos los componentes del pipeline.
Esta clase base abstracta define la interfaz común que todos los componentes
del pipeline deben implementar. Hereda de `Providable`
para permitir el registro automático en un registro de componentes y de `ABC`
para forzar la implementación de métodos abstractos.

Las subclases deben implementar el método `process` para definir su lógica específica
de transformación de datos dentro del pipeline.

Atributos:
    Hereda atributos de `Providable` para la gestión del registro.
    InputDataType (type[InputDataT]): El tipo del modelo de datos de entrada 
        esperado por este componente pipe.
    OutputDataType (type[OutputDataT]): El tipo del modelo de datos de salida 
        producido por este componente pipe.


::: details #### <Badge type="info" text="method"/> <span class='text-warning'>def</span> `process(self, context: PipelineContext[InputDataT]) -> PipelineContext[OutputDataT]`
Procesa un objeto de contexto del pipeline y devuelve el contexto modificado.
Este método define la lógica de procesamiento principal para un componente del pipeline.
Toma un objeto `PipelineContext` que contiene el estado compartido del pipeline,
realiza transformaciones u operaciones en este contexto y devuelve el
contexto actualizado para el siguiente componente en el pipeline.

Argumentos:
    context: El contexto actual del pipeline que contiene los datos de estado compartidos.

Devuelve:
    El objeto `PipelineContext` actualizado después del procesamiento.

Lanza:
    Las subclases pueden lanzar excepciones específicas de la implementación para
    indicar errores de procesamiento o estados no válidos.

:::


---

## Módulo: `open_ticket_ai\src\ce\run\pipeline\pipeline.py`

Define la clase Pipeline para ejecutar una secuencia de pipes.
El Pipeline es un Pipe especializado que ejecuta múltiples pipes en secuencia. Gestiona el contexto
y el estado a lo largo de la ejecución, manejando errores y solicitudes de detención de manera apropiada.

### <span style='text-info'>class</span> `Pipeline`

Un pipeline que ejecuta una secuencia de pipes secuencialmente.
Esta clase gestiona el flujo de ejecución de múltiples pipes, manejando transiciones de estado,
propagación de errores y solicitudes de detención durante el procesamiento.

**Parámetros:**

- **`pipes`** () - Lista de objetos Pipe para ejecutar en secuencia.


::: details #### <Badge type="info" text="method"/> <span class='text-warning'>def</span> `__init__(self, config: PipelineConfig, pipes: List[Pipe])`
Inicializa el Pipeline con la configuración y la secuencia de pipes.

**Parámetros:**

- **`config`** () - Ajustes de configuración para el pipeline.
- **`pipes`** () - Lista ordenada de instancias de Pipe para ejecutar.

:::


::: details #### <Badge type="info" text="method"/> <span class='text-warning'>def</span> `execute(self, context: PipelineContext) -> PipelineContext`
Ejecuta todos los pipes secuencialmente con manejo de errores y propagación de estado.
Procesa cada pipe en secuencia mientras:
- Valida los datos de entrada usando el modelo de entrada de cada pipe
- Maneja las solicitudes de estado STOPPED de los pipes
- Captura y registra excepciones durante la ejecución del pipe
- Actualiza el estado del contexto apropiadamente (RUNNING, SUCCESS, FAILED, STOPPED)

**Parámetros:**

- **`context`** () - El contexto del pipeline que contiene el estado de ejecución y los datos.

**Devuelve:** () - PipelineContext actualizado que refleja el estado de ejecución final después del procesamiento.

:::


::: details #### <Badge type="info" text="method"/> <span class='text-warning'>def</span> `process(self, context: PipelineContext) -> PipelineContext`
Procesa el contexto a través de toda la secuencia del pipeline.
Implementa el método abstracto de la clase base Pipe. Delega al
método `execute()` para el procesamiento real del pipeline.

**Parámetros:**

- **`context`** () - El contexto del pipeline que contiene el estado de ejecución y los datos.

**Devuelve:** () - PipelineContext actualizado después de procesar a través de todos los pipes.

:::


---

## Módulo: `open_ticket_ai\src\ce\run\pipeline\status.py`


### <span style='text-info'>class</span> `PipelineStatus`

Representa los posibles estados de la ejecución de un pipeline.
Este enum define los diversos estados que un pipeline puede tener durante su ciclo de vida.

**Parámetros:**

- **`RUNNING`** () - Indica que el pipeline se está ejecutando actualmente.
- **`SUCCESS`** () - Indica que el pipeline se completó con éxito y sin errores.
- **`STOPPED`** () - Indica que el pipeline fue detenido intencionadamente (parada controlada).
- **`FAILED`** () - Indica que el pipeline terminó debido a un error inesperado.


---