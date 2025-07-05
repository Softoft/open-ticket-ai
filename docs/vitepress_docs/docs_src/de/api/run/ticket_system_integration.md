---
description: Entdecken Sie unsere Python-Bibliothek für die nahtlose Integration von Ticketsystemen. Diese
  Dokumentation beschreibt den `TicketSystemAdapter`, eine abstrakte Basisklasse zum Erstellen
  benutzerdefinierter Konnektoren, und stellt einen einsatzbereiten `OTOBOAdapter` zur Verfügung. Lernen Sie, wie Sie Tickets
  über verschiedene Plattformen hinweg mit einheitlichen Modellen wie `UnifiedTicket`, `UnifiedNote`,
  und `SearchCriteria` zum Erstellen, Aktualisieren und Suchen von Support-Tickets verwalten.
---
# Dokumentation für `**/ce/ticket_system_integration/*.py`

## Modul: `open_ticket_ai\src\ce\ticket_system_integration\otobo_adapter.py`

Paket zur Integration mit OTOBO-Systemen.
Dieses Modul stellt die primäre Schnittstelle für die OTOBO-Integration bereit, indem es
die `OTOBOAdapter`-Klasse verfügbar macht. Es dient als öffentlicher API-Einstiegspunkt für
die Interaktion mit OTOBO-Diensten.



---

## Modul: `open_ticket_ai\src\ce\ticket_system_integration\otobo_adapter_config.py`



---

## Modul: `open_ticket_ai\src\ce\ticket_system_integration\ticket_system_adapter.py`


### <span style='text-info'>class</span> `TicketSystemAdapter`

Eine abstrakte Basisklasse für Ticketsystem-Adapter.
Diese Klasse definiert die Schnittstelle, die alle konkreten Ticketsystem-Adapter
implementieren müssen, um mit verschiedenen Ticketsystemen zu interagieren. Sie bietet eine gemeinsame
Konfigurationsbehandlung durch Dependency Injection und erfordert, dass Unterklassen
die Kernoperationen für Tickets implementieren.

**Parameter:**

- **`config`** (`SystemConfig`) - Systemkonfigurationsobjekt, das die Adapter-Einstellungen enthält.


::: details #### <Badge type="info" text="method"/> <span class='text-warning'>def</span> `__init__(self, config: SystemConfig)`
Initialisiert den Adapter mit der Systemkonfiguration.
Dieser Konstruktor wird automatisch über das Dependency-Injection-Framework mit der Systemkonfiguration
versorgt. Er initialisiert den Adapter mit der bereitgestellten
Konfiguration und stellt die korrekte Einrichtung der geerbten
Komponenten sicher.

**Parameter:**

- **`config`** (`SystemConfig`) - Das Systemkonfigurationsobjekt, das
alle notwendigen Einstellungen und Parameter für den Adapter enthält.

:::


::: details #### <Badge type="info" text="method"/> <span class="text-warning">async def</span> `update_ticket(self, ticket_id: str, updates: dict) -> bool`
Aktualisiert ein Ticket im System.
Diese Methode muss von konkreten Adaptern implementiert werden, um die Aktualisierung
von Ticket-Attributen im Ziel-Ticketsystem zu handhaben. Sie sollte Teilaktualisierungen
unterstützen und die aktualisierte Ticket-Darstellung zurückgeben.

**Parameter:**

- **`ticket_id`** () - Eindeutiger Bezeichner des zu aktualisierenden Tickets.
- **`updates`** () - Wörterbuch der auf dem Ticket zu aktualisierenden Attribute.

**Rückgabewert:** (`bool`) - ``True``, wenn die Aktualisierung erfolgreich war, andernfalls ``False``.

:::


::: details #### <Badge type="info" text="method"/> <span class="text-warning">async def</span> `find_tickets(self, criteria: SearchCriteria) -> list[UnifiedTicket]`
Sucht nach Tickets, die den ``criteria`` entsprechen.
Diese Methode muss von konkreten Adaptern implementiert werden, um
komplexe Suchen im Ziel-Ticketsystem durchzuführen. Die Abfragestruktur
ist adapterspezifisch, sollte aber gängige Filter-
und Suchoperationen unterstützen.

**Parameter:**

- **`criteria`** () - Parameter, die definieren, nach welchen Tickets gesucht werden soll.

**Rückgabewert:** (`list[UnifiedTicket]`) - Eine Liste von Tickets, die den Kriterien entsprechen.
Gibt eine leere Liste zurück, wenn keine Übereinstimmungen gefunden werden.

:::


::: details #### <Badge type="info" text="method"/> <span class="text-warning">async def</span> `find_first_ticket(self, criteria: SearchCriteria) -> UnifiedTicket | None`
Gibt das erste Ticket zurück, das den ``criteria`` entspricht, falls vorhanden.
Dies ist eine Hilfsmethode, die das erste passende
Ticket aus einer Suchoperation zurückgeben sollte. Sie sollte die Leistung
optimieren, indem sie die Ergebnisse intern begrenzt.

**Parameter:**

- **`criteria`** () - Parameter, die definieren, nach welchem Ticket gesucht werden soll.

**Rückgabewert:** (`Optional[UnifiedTicket]`) - Das erste passende Ticket oder ``None``, wenn keine Tickets übereinstimmen.

:::


::: details #### <Badge type="info" text="method"/> <span class="text-warning">async def</span> `create_ticket(self, ticket_data: UnifiedTicket) -> UnifiedTicket`
Erstellt ein neues Ticket im System.
Diese Methode muss von konkreten Adaptern implementiert werden, um die Ticketerstellung
im Ziel-Ticketsystem zu handhaben. Die Ticketdaten werden in einem einheitlichen Format bereitgestellt.

**Parameter:**

- **`ticket_data`** (`UnifiedTicket`) - Die zu erstellenden Ticketdaten. Enthält alle notwendigen Felder in einem 
systemunabhängigen Format.

**Rückgabewert:** (`UnifiedTicket`) - Das erstellte Ticket-Objekt mit systemgenerierten Bezeichnern und Feldern.

:::


::: details #### <Badge type="info" text="method"/> <span class="text-warning">async def</span> `add_note(self, ticket_id: str, note: UnifiedNote) -> UnifiedNote`
Fügt eine Notiz zu einem bestehenden Ticket hinzu.
Diese Methode muss von konkreten Adaptern implementiert werden, um Notizen/Kommentare
an Tickets im Zielsystem anzuhängen. Der Notizinhalt wird in einem einheitlichen Format bereitgestellt.

**Parameter:**

- **`ticket_id`** (`str`) - Eindeutiger Bezeichner des Ziel-Tickets.
- **`note`** (`UnifiedNote`) - Der hinzuzufügende Notizinhalt und die Metadaten.

**Rückgabewert:** (`UnifiedNote`) - Das hinzugefügte Notizobjekt mit systemgenerierten Metadaten (z. B. Zeitstempel, ID).

:::


---

## Modul: `open_ticket_ai\src\ce\ticket_system_integration\unified_models.py`


### <span style='text-info'>class</span> `UnifiedEntity`

Basis-Entität mit optionaler ID und optionalem Namen.

**Parameter:**

- **`id`** (`Optional[int]`) (default: `None`) - Eindeutiger Bezeichner für die Entität. Standardwert ist `None`.
- **`name`** (`Optional[str]`) (default: `None`) - Anzeigename der Entität. Standardwert ist `None`.

### <span style='text-info'>class</span> `UnifiedUser`

Repräsentiert einen Benutzer innerhalb des Systems.
Erbt Attribute von `UnifiedEntity` und fügt hinzu:

**Parameter:**

- **`email`** (`Optional[str]`) (default: `None`) - E-Mail-Adresse des Benutzers. Standardwert ist `None`.

### <span style='text-info'>class</span> `UnifiedQueue`

Repräsentiert eine Ticket-Warteschlange.
Erbt Attribute von `UnifiedEntity`.

### <span style='text-info'>class</span> `UnifiedPriority`

Repräsentiert eine Ticket-Prioritätsstufe.
Erbt Attribute von `UnifiedEntity`.

### <span style='text-info'>class</span> `UnifiedStatus`

Repräsentiert einen Ticket-Status.
Erbt Attribute von `UnifiedEntity`.

### <span style='text-info'>class</span> `UnifiedNote`

Repräsentiert eine an ein Ticket angehängte Notiz.

**Parameter:**

- **`id`** (`Optional[str]`) (default: `None`) - Eindeutiger Bezeichner für die Notiz. Standardwert ist `None`.
- **`body`** (`str`) - Inhalt der Notiz.
- **`created_at`** (`datetime`) - Zeitstempel, wann die Notiz erstellt wurde.
- **`is_internal`** (`bool`) - Gibt an, ob die Notiz intern ist (für Kunden nicht sichtbar).
- **`author`** (`UnifiedUser`) - Benutzer, der die Notiz erstellt hat.

### <span style='text-info'>class</span> `UnifiedTicket`

Einheitliche Darstellung eines Support-Tickets.

**Parameter:**

- **`id`** (`str`) - Eindeutiger Bezeichner für das Ticket.
- **`subject`** (`str`) - Betreffzeile des Tickets.
- **`body`** (`str`) - Hauptinhalt/Beschreibung des Tickets.
- **`custom_fields`** (`Dict`) - Zusätzliche benutzerdefinierte Felddaten, die mit dem Ticket verknüpft sind.
- **`queue`** (`UnifiedQueue`) - Warteschlange, zu der das Ticket gehört.
- **`priority`** (`UnifiedPriority`) - Prioritätsstufe des Tickets.
- **`status`** (`UnifiedStatus`) - Aktueller Status des Tickets.
- **`owner`** (`UnifiedUser`) - Benutzer, dem das Ticket aktuell zugewiesen ist.
- **`notes`** (`List[UnifiedNote]`) (default: `empty list`) - Liste der an das Ticket angehängten Notizen. Standardwert ist eine leere Liste.

### <span style='text-info'>class</span> `SearchCriteria`

Kriterien zum Suchen/Filtern von Tickets.

**Parameter:**

- **`id`** (`Optional[str]`) (default: `None`) - Ticket-ID, nach der gesucht werden soll. Standardwert ist `None`.
- **`subject`** (`Optional[str]`) (default: `None`) - Text, der in Ticket-Betreffs gesucht werden soll. Standardwert ist `None`.
- **`queue`** (`Optional[UnifiedQueue]`) (default: `None`) - Warteschlange, nach der gefiltert werden soll. Standardwert ist `None`.
- **`user`** (`Optional[UnifiedUser]`) (default: `None`) - Benutzer, nach dem gefiltert werden soll (z. B. Besitzer). Standardwert ist `None`.


---