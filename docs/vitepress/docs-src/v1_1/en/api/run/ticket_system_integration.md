# Documentation for `**/ce/ticket_system_integration/*.py`

## Module: `open_ticket_ai\src\ce\ticket_system_integration\otobo_adapter.py`


### <span style='color: #8E44AD;'>class</span> `OTOBOAdapter`

Adapter for OTOBO ticket system integration.
This class provides methods to interact with the OTOBO API.


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `get_description() -> str`</summary>

Return a description of the adapter's functionality.

**Returns:** (`str`) - A description of the OTOBO adapter.

</details>


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `__init__(self, config: SystemConfig, otobo_client: OTOBOClient)`</summary>

Initialize the OTOBO adapter with configuration and client.

**Parameters:**

- **`config`** (`SystemConfig`) - System configuration object.
- **`otobo_client`** (`OTOBOClient`) - Client for interacting with OTOBO API.

</details>


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>async def</span> `find_tickets(self, query: dict) -> list[dict]`</summary>

Return all tickets matching ``query``.

**Parameters:**

- **`query`** (`dict`) - Search parameters for tickets.

**Returns:** (`list[dict]`) - List of tickets matching the query.

</details>


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>async def</span> `find_first_ticket(self, query: dict) -> dict | None`</summary>

Return the first ticket found for ``query`` if available.

**Parameters:**

- **`query`** (`dict`) - Search parameters for tickets.

**Returns:** () - dict | None: First matching ticket dictionary or None if none found.

</details>


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>async def</span> `update_ticket(self, ticket_id: str, data: dict) -> dict`</summary>

Update ``ticket_id`` with ``data`` and return the updated record.

**Parameters:**

- **`ticket_id`** (`str`) - ID of the ticket to update.
- **`data`** (`dict`) - Update parameters for the ticket.

**Returns:** (`dict`) - Updated ticket record.

</details>


---

## Module: `open_ticket_ai\src\ce\ticket_system_integration\otobo_adapter_config.py`


### <span style='color: #8E44AD;'>class</span> `OTOBOAdapterConfig`

Configuration model for OTOBO adapter.

**Parameters:**

- **`server_address`** (`str`) - The base URL of the OTOBO server.
- **`webservice_name`** (`str`) - The name of the web service to use.
- **`search_operation_url`** (`str`) - The URL for the search operation.
- **`update_operation_url`** (`str`) - The URL for the update operation.
- **`get_operation_url`** (`str`) - The URL for the get operation.
- **`username`** (`str`) - The username for authentication.
- **`password_env_var`** (`str`) - The environment variable that contains the password.


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `__str__(self)`</summary>

Return a string representation of the configuration.

</details>


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `password(self) -> str`</summary>

Retrieves the password from the environment variable specified in the configuration.

**Returns:** (`str`) - The password for authentication.

</details>


---

## Module: `open_ticket_ai\src\ce\ticket_system_integration\ticket_system_adapter.py`


### <span style='color: #8E44AD;'>class</span> `TicketSystemAdapter`

An abstract base class for ticket system adapters.
This class defines the
interface that all ticket system adapters must implement.


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `__init__(self, config: SystemConfig)`</summary>

Initialize the adapter with system configuration.

</details>


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>async def</span> `update_ticket(self, ticket_id: str, data: dict) -> dict | None`</summary>

Update a ticket in the system.

**Parameters:**

- **`ticket_id`** () - Ticket identifier.
- **`data`** () - Attributes to update.

**Returns:** (`Optional[dict]`) - Updated ticket information.

</details>


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>async def</span> `find_tickets(self, query: dict) -> list[dict]`</summary>

Search for tickets matching ``query``.

**Parameters:**

- **`query`** () - Search parameters for the ticket system.

**Returns:** (`list[dict]`) - Matching tickets.

</details>


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>async def</span> `find_first_ticket(self, query: dict) -> dict | None`</summary>

Return the first ticket that matches ``query`` if any.

**Parameters:**

- **`query`** () - Search parameters for the ticket system.

**Returns:** (`Optional[dict]`) - The first matching ticket or None if no ticket is found.

</details>


---
