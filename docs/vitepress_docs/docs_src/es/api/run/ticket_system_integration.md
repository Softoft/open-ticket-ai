---
description: Descubra nuestra biblioteca de Python para una integración perfecta con sistemas de tickets. Esta
  documentación detalla `TicketSystemAdapter`, una clase base abstracta para construir
  conectores personalizados, y proporciona un `OTOBOAdapter` listo para usar. Aprenda a gestionar tickets
  en diferentes plataformas utilizando modelos unificados como `UnifiedTicket`, `UnifiedNote`,
  y `SearchCriteria` para crear, actualizar y buscar tickets de soporte.
---
# Documentación para `**/ce/ticket_system_integration/*.py`

## Módulo: `open_ticket_ai\src\ce\ticket_system_integration\otobo_adapter.py`

Paquete para la integración con sistemas OTOBO.
Este módulo proporciona la interfaz principal para la integración con OTOBO al exponer
la clase `OTOBOAdapter`. Sirve como el punto de entrada de la API pública para
interactuar con los servicios de OTOBO.



---

## Módulo: `open_ticket_ai\src\ce\ticket_system_integration\otobo_adapter_config.py`



---

## Módulo: `open_ticket_ai\src\ce\ticket_system_integration\ticket_system_adapter.py`


### <span style='text-info'>class</span> `TicketSystemAdapter`

Una clase base abstracta para adaptadores de sistemas de tickets.
Esta clase define la interfaz que todos los adaptadores de sistemas de tickets concretos deben
implementar para interactuar con diferentes sistemas de ticketing. Proporciona un manejo
de configuración común a través de inyección de dependencias y requiere que las subclases
implementen las operaciones principales de los tickets.

**Parámetros:**

- **`config`** (`SystemConfig`) - Objeto de configuración del sistema que contiene los ajustes del adaptador.


::: details #### <Badge type="info" text="method"/> <span class='text-warning'>def</span> `__init__(self, config: SystemConfig)`
Inicializa el adaptador con la configuración del sistema.
Este constructor es inyectado automáticamente con la configuración del sistema
utilizando el framework de inyección de dependencias. Inicializa el adaptador
con la configuración proporcionada y asegura la configuración adecuada de los
componentes heredados.

**Parámetros:**

- **`config`** (`SystemConfig`) - El objeto de configuración del sistema que contiene
todos los ajustes y parámetros necesarios para el adaptador.

:::


::: details #### <Badge type="info" text="method"/> <span class="text-warning">async def</span> `update_ticket(self, ticket_id: str, updates: dict) -> bool`
Actualiza un ticket en el sistema.
Este método debe ser implementado por los adaptadores concretos para manejar la actualización
de los atributos de un ticket en el sistema de ticketing de destino. Debe soportar actualizaciones
parciales y devolver la representación del ticket actualizado.

**Parámetros:**

- **`ticket_id`** () - Identificador único del ticket a actualizar.
- **`updates`** () - Diccionario de atributos a actualizar en el ticket.

**Devuelve:** (`bool`) - ``True`` si la actualización tuvo éxito, de lo contrario ``False``.

:::


::: details #### <Badge type="info" text="method"/> <span class="text-warning">async def</span> `find_tickets(self, criteria: SearchCriteria) -> list[UnifiedTicket]`
Busca tickets que coincidan con los ``criteria``.
Este método debe ser implementado por los adaptadores concretos para realizar
búsquedas complejas en el sistema de ticketing de destino. La estructura de la
consulta es específica del adaptador, pero debe soportar operaciones comunes de
filtrado y búsqueda.

**Parámetros:**

- **`criteria`** () - Parámetros que definen qué tickets buscar.

**Devuelve:** (`list[UnifiedTicket]`) - Una lista de tickets que coinciden con los criterios.
Devuelve una lista vacía si no se encuentran coincidencias.

:::


::: details #### <Badge type="info" text="method"/> <span class="text-warning">async def</span> `find_first_ticket(self, criteria: SearchCriteria) -> UnifiedTicket | None`
Devuelve el primer ticket que coincida con los ``criteria``, si existe.
Este es un método de conveniencia que debe devolver el primer ticket coincidente
de una operación de búsqueda. Debe optimizar el rendimiento
limitando los resultados internamente.

**Parámetros:**

- **`criteria`** () - Parámetros que definen qué ticket buscar.

**Devuelve:** (`Optional[UnifiedTicket]`) - El primer ticket coincidente o ``None`` si ningún ticket coincide.

:::


::: details #### <Badge type="info" text="method"/> <span class="text-warning">async def</span> `create_ticket(self, ticket_data: UnifiedTicket) -> UnifiedTicket`
Crea un nuevo ticket en el sistema.
Este método debe ser implementado por los adaptadores concretos para manejar la creación de tickets
en el sistema de ticketing de destino. Los datos del ticket se proporcionan en un formato unificado.

**Parámetros:**

- **`ticket_data`** (`UnifiedTicket`) - Los datos del ticket a crear. Contiene todos los campos necesarios en un 
formato independiente del sistema.

**Devuelve:** (`UnifiedTicket`) - El objeto del ticket creado con identificadores y campos generados por el sistema.

:::


::: details #### <Badge type="info" text="method"/> <span class="text-warning">async def</span> `add_note(self, ticket_id: str, note: UnifiedNote) -> UnifiedNote`
Añade una nota a un ticket existente.
Este método debe ser implementado por los adaptadores concretos para adjuntar notas/comentarios
a los tickets en el sistema de destino. El contenido de la nota se proporciona en un formato unificado.

**Parámetros:**

- **`ticket_id`** (`str`) - Identificador único del ticket de destino.
- **`note`** (`UnifiedNote`) - El contenido y los metadatos de la nota a añadir.

**Devuelve:** (`UnifiedNote`) - El objeto de la nota añadida con metadatos generados por el sistema (p. ej., marca de tiempo, ID).

:::


---

## Módulo: `open_ticket_ai\src\ce\ticket_system_integration\unified_models.py`


### <span style='text-info'>class</span> `UnifiedEntity`

Entidad base con ID y nombre opcionales.

**Parámetros:**

- **`id`** (`Optional[int]`) (default: `None`) - Identificador único para la entidad. Por defecto es None.
- **`name`** (`Optional[str]`) (default: `None`) - Nombre de visualización de la entidad. Por defecto es None.

### <span style='text-info'>class</span> `UnifiedUser`

Representa un usuario dentro del sistema.
Hereda atributos de `UnifiedEntity` y añade:

**Parámetros:**

- **`email`** (`Optional[str]`) (default: `None`) - Dirección de correo electrónico del usuario. Por defecto es None.

### <span style='text-info'>class</span> `UnifiedQueue`

Representa una cola de tickets.
Hereda atributos de `UnifiedEntity`.

### <span style='text-info'>class</span> `UnifiedPriority`

Representa un nivel de prioridad de ticket.
Hereda atributos de `UnifiedEntity`.

### <span style='text-info'>class</span> `UnifiedStatus`

Representa un estado de ticket.
Hereda atributos de `UnifiedEntity`.

### <span style='text-info'>class</span> `UnifiedNote`

Representa una nota adjunta a un ticket.

**Parámetros:**

- **`id`** (`Optional[str]`) (default: `None`) - Identificador único para la nota. Por defecto es None.
- **`body`** (`str`) - Contenido de la nota.
- **`created_at`** (`datetime`) - Marca de tiempo de cuándo se creó la nota.
- **`is_internal`** (`bool`) - Indica si la nota es interna (no visible para los clientes).
- **`author`** (`UnifiedUser`) - Usuario que creó la nota.

### <span style='text-info'>class</span> `UnifiedTicket`

Representación unificada de un ticket de soporte.

**Parámetros:**

- **`id`** (`str`) - Identificador único para el ticket.
- **`subject`** (`str`) - Línea de asunto del ticket.
- **`body`** (`str`) - Contenido principal/descripción del ticket.
- **`custom_fields`** (`Dict`) - Datos de campos personalizados adicionales asociados con el ticket.
- **`queue`** (`UnifiedQueue`) - Cola a la que pertenece el ticket.
- **`priority`** (`UnifiedPriority`) - Nivel de prioridad del ticket.
- **`status`** (`UnifiedStatus`) - Estado actual del ticket.
- **`owner`** (`UnifiedUser`) - Usuario actualmente asignado al ticket.
- **`notes`** (`List[UnifiedNote]`) (default: `empty list`) - Lista de notas adjuntas al ticket. Por defecto es una lista vacía.

### <span style='text-info'>class</span> `SearchCriteria`

Criterios para buscar/filtrar tickets.

**Parámetros:**

- **`id`** (`Optional[str]`) (default: `None`) - ID del ticket a buscar. Por defecto es None.
- **`subject`** (`Optional[str]`) (default: `None`) - Texto a buscar en los asuntos de los tickets. Por defecto es None.
- **`queue`** (`Optional[UnifiedQueue]`) (default: `None`) - Cola por la que filtrar. Por defecto es None.
- **`user`** (`Optional[UnifiedUser]`) (default: `None`) - Usuario por el que filtrar (p. ej., propietario). Por defecto es None.


---