# Dokumentation für `**/ce/ticket_system_integration/*.py`

## Modul: `open_ticket_ai\src\ce\ticket_system_integration\otobo_adapter.py`


### <span style='color: #8E44AD;'>class</span> `OTOBOAdapter`

Adapter für die OTOBO-Ticketsystem-Integration.
Diese Klasse stellt Methoden zur Interaktion mit der OTOBO-API bereit.


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `get_description() -> str`</summary>

Gibt eine Beschreibung der Funktionalität des Adapters zurück.

**Returns:** (`str`) - Eine Beschreibung des OTOBO-Adapters.

</details>


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `__init__(self, config: SystemConfig, otobo_client: OTOBOClient)`</summary>

Initialisiert den OTOBO-Adapter mit Konfiguration und Client.

**Parameters:**

- **`config`** (`SystemConfig`) - Systemkonfigurationsobjekt.
- **`otobo_client`** (`OTOBOClient`) - Client zur Interaktion mit der OTOBO-API.

</details>


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>async def</span> `find_tickets(self, query: dict) -> list[dict]`</summary>

Gibt alle Tickets zurück, die mit ``query`` übereinstimmen.

**Parameters:**

- **`query`** (`dict`) - Suchparameter für Tickets.

**Returns:** (`list[dict]`) - Liste der passenden Tickets.

</details>


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>async def</span> `find_first_ticket(self, query: dict) -> dict | None`</summary>

Gibt das erste gefundene Ticket für ``query`` zurück, falls verfügbar.

**Parameters:**

- **`query`** (`dict`) - Suchparameter für Tickets.

**Returns:** () - dict | None: Erstes passendes Ticket-Dictionary oder None, falls keins gefunden wurde.

</details>


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>async def</span> `update_ticket(self, ticket_id: str, data: dict) -> dict`</summary>

Aktualisiert ``ticket_id`` mit ``data`` und gibt den aktualisierten Datensatz zurück.

**Parameters:**

- **`ticket_id`** (`str`) - ID des zu aktualisierenden Tickets.
- **`data`** (`dict`) - Aktualisierungsparameter für das Ticket.

**Returns:** (`dict`) - Aktualisierter Ticket-Datensatz.

</details>


---

## Modul: `open_ticket_ai\src\ce\ticket_system_integration\otobo_adapter_config.py`


### <span style='color: #8E44AD;'>class</span> `OTOBOAdapterConfig`

Konfigurationsmodell für den OTOBO-Adapter.

**Parameters:**

- **`server_address`** (`str`) - Die Basis-URL des OTOBO-Servers.
- **`webservice_name`** (`str`) - Der Name des zu verwendenden Webdienstes.
- **`search_operation_url`** (`str`) - Die URL für die Suchoperation.
- **`update_operation_url`** (`str`) - Die URL für die Aktualisierungsoperation.
- **`get_operation_url`** (`str`) - Die URL für die Abfrageoperation.
- **`username`** (`str`) - Der Benutzername zur Authentifizierung.
- **`password_env_var`** (`str`) - Die Umgebungsvariable, die das Passwort enthält.


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `__str__(self)`</summary>

Gibt eine String-Darstellung der Konfiguration zurück.

</details>


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `password(self) -> str`</summary>

Ruft das Passwort aus der in der Konfiguration angegebenen Umgebungsvariable ab.

**Returns:** (`str`) - Das Passwort zur Authentifizierung.

</details>


---

## Modul: `open_ticket_ai\src\ce\ticket_system_integration\ticket_system_adapter.py`


### <span style='color: #8E44AD;'>class</span> `TicketSystemAdapter`

Eine abstrakte Basisklasse für Ticketsystem-Adapter.
Diese Klasse definiert die Schnittstelle, die alle Ticketsystem-Adapter implementieren müssen.


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `__init__(self, config: SystemConfig)`</summary>

Initialisiert den Adapter mit Systemkonfiguration.

</details>


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>async def</span> `update_ticket(self, ticket_id: str, data: dict) -> dict | None`</summary>

Aktualisiert ein Ticket im System.

**Parameters:**

- **`ticket_id`** () - Ticketkennung.
- **`data`** () - Zu aktualisierende Attribute.

**Returns:** (`Optional[dict]`) - Aktualisierte Ticketinformationen.

</details>


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>async def</span> `find_tickets(self, query: dict) -> list[dict]`</summary>

Sucht nach Tickets, die mit ``query`` übereinstimmen.

**Parameters:**

- **`query`** () - Suchparameter für das Ticketsystem.

**Returns:** (`list[dict]`) - Passende Tickets.

</details>


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>async def</span> `find_first_ticket(self, query: dict) -> dict | None`</summary>

Gibt das erste Ticket zurück, das mit ``query`` übereinstimmt, falls vorhanden.

**Parameters:**

- **`query`** () - Suchparameter für das Ticketsystem.

**Returns:** (`Optional[dict]`) - Das erste passende Ticket oder None, falls kein Ticket gefunden wurde.

</details>


---