---
description: Aprenda a integrar aplicaciones Python con OTOBO, Znuny y OTRS utilizando
  una librería de cliente asíncrona. Esta guía proporciona instrucciones paso a paso y
  ejemplos de código para gestionar tickets de helpdesk a través de la REST API, incluyendo
  la creación, búsqueda, actualización y recuperación del historial de tickets.
---
# Guía de Integración con OTOBO, Znuny y OTRS

Para la integración con OTOBO, Znuny u OTRS, estamos utilizando nuestra librería cliente de python otobo.

## Librería Cliente de Python para OTOBO

Un cliente Python asíncrono para interactuar con la REST API de OTOBO. Construido con `httpx` y `pydantic` para seguridad de tipos y facilidad de uso.

### Características

*   **Peticiones HTTP asíncronas** usando `httpx.AsyncClient`
*   **Modelos Pydantic** para la validación de datos de petición y respuesta
*   Operaciones CRUD completas para tickets:

    *   `TicketCreate`
    *   `TicketSearch`
    *   `TicketGet`
    *   `TicketUpdate`
    *   `TicketHistoryGet`
*   **Manejo de errores** a través de `OTOBOError` para errores de la API
*   Método de utilidad `search_and_get` para combinar resultados de búsqueda con una recuperación detallada

### Instalación

Instalar desde PyPI:

```bash
pip install otobo
```

### Inicio Rápido

#### Configurar los Webservices de OTOBO:

Cree un nuevo servicio web en OTOBO con la siguiente configuración:
Consulte la Guía de Instalación.

#### Crear un nuevo Agente

Cree un nuevo Agente de Otobo con una contraseña segura y otórguele los permisos necesarios para la tarea que desea realizar.


#### 1. Configurar el cliente

```python
from otobo import TicketOperation, OTOBOClientConfig
from otobo import AuthData

config = OTOBOClientConfig(
    base_url="https://your-otobo-server/nph-genericinterface.pl",
    service="OTOBO",
    auth=AuthData(UserLogin="user1", Password="SecurePassword"),
    operations={
        TicketOperation.CREATE.value: "ticket",
        TicketOperation.SEARCH.value: "ticket/search",
        TicketOperation.GET.value: "ticket/get",
        TicketOperation.UPDATE.value: "ticket",
        TicketOperation.HISTORY_GET.value: "ticket/history",
    }
)
```

#### 2. Inicializar el cliente

```python
import logging
from otobo import OTOBOClient

logging.basicConfig(level=logging.INFO)


client = OTOBOClient(config)
```

#### 3. Crear un ticket

```python
from otobo import (TicketOperation, OTOBOClientConfig, AuthData, TicketSearchParams, TicketCreateParams,
                   TicketHistoryParams, TicketUpdateParams, \
                   TicketGetParams, OTOBOClient, OTOBOTicketCreateResponse)

payload = TicketCreateParams(
    Ticket={
        "Title": "New Order",
        "Queue": "Sales",
        "State": "new",
        "Priority": "3 normal",
        "CustomerUser": "customer@example.com"
    },
    Article={
        "Subject": "Product Inquiry",
        "Body": "Please send pricing details...",
        "MimeType": "text/plain"
    }
)

response: OTOBOTicketCreateResponse = await client.create_ticket(payload)
print(response.TicketID, response.TicketNumber)
```

#### 4. Buscar y recuperar tickets

```python
from otobo import TicketSearchParams, TicketGetParams

search_params = TicketSearchParams(Title="%Order%")
search_res = await client.search_tickets(search_params)
ids = search_res.TicketID

for ticket_id in ids:
    get_params = TicketGetParams(TicketID=ticket_id, AllArticles=1)
    details = await client.get_ticket(get_params)
    print(details.Ticket[0])
```

#### 5. Actualizar un ticket

```python
from otobo import TicketUpdateParams

update_params = TicketUpdateParams(
    TicketID=response.TicketID,
    Ticket={"State": "closed"}
)
await client.update_ticket(update_params)
```

#### 6. Obtener el historial de un ticket

```python
from otobo import TicketHistoryParams

history_params = TicketHistoryParams(TicketID=str(response.TicketID))
history_res = await client.get_ticket_history(history_params)
print(history_res.History)
```

#### 7. Búsqueda y obtención combinadas

```python
from otobo import FullTicketSearchResponse

full_res: FullTicketSearchResponse = await client.search_and_get(search_params)
```