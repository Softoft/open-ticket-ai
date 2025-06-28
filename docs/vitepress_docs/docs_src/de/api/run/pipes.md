# Dokumentation für `**/ce/run/pipe_implementations/*.py`

## Modul: `open_ticket_ai\src\ce\run\pipe_implementations\basic_ticket_fetcher.py`


### <span style='text-info'>class</span> `BasicTicketFetcher`

Einfacher Fetcher, der Ticketdaten mithilfe des Ticket-System-Adapters lädt.
Diese Pipe ruft Ticketinformationen aus einem externen Ticketsystem mithilfe des bereitgestellten Adapters ab. Sie dient als Platzhalter für komplexere Fetching-Implementierungen.

**Parameter:**

- **`fetcher_config`** (``RegistryInstanceConfig``) - Konfigurationsinstanz für den Fetcher.
- **`ticket_system`** (``TicketSystemAdapter``) - Adapter zur Interaktion mit dem Ticketsystem.


::: details #### <Badge type="info" text="method"/> <span class='text-warning'>def</span> `__init__(self, config: RegistryInstanceConfig, ticket_system: TicketSystemAdapter)`
Initialisiert den BasicTicketFetcher mit Konfiguration und Ticket-System-Adapter.

**Parameter:**

- **`config`** (``RegistryInstanceConfig``) - Die Konfigurationsinstanz für den Fetcher.
- **`ticket_system`** (``TicketSystemAdapter``) - Der Adapter zur Interaktion mit dem Ticketsystem.

:::


::: details #### <Badge type="info" text="method"/> <span class='text-warning'>def</span> `process(self, context: PipelineContext) -> PipelineContext`
Ruft Ticketdaten ab und aktualisiert den Pipeline-Kontext.
Ruft das Ticket mithilfe der Ticket-ID aus dem Kontext ab. Wenn es gefunden wird, wird das Daten-Dictionary des Kontexts mit den Ticketinformationen aktualisiert. Wenn kein Ticket gefunden wird, bleibt der Kontext unverändert.

**Parameter:**

- **`context`** (``PipelineContext``) - Der Pipeline-Kontext, der die `ticket_id` enthält.

**Rückgabe:** (``PipelineContext``) - Das Kontextobjekt. Wenn ein Ticket gefunden wurde, enthält sein `data`-Dictionary die Ticketinformationen. Andernfalls wird der ursprüngliche Kontext zurückgegeben.

:::


::: details #### <Badge type="info" text="method"/> <span class='text-warning'>def</span> `get_description() -> str`
Liefert eine statische Beschreibung der Funktionalität dieser Pipe.

**Rückgabe:** (`str`) - Eine statische Beschreibung des Zwecks und Verhaltens der Pipe.

:::


---

## Modul: `open_ticket_ai\src\ce\run\pipe_implementations\generic_ticket_updater.py`


### <span style='text-info'>class</span> `GenericTicketUpdater`

Aktualisiert ein Ticket im Ticketsystem unter Verwendung von Daten aus dem Kontext.
Diese Pipe-Komponente ist für die Aktualisierung von Tickets in einem externen Ticket-Tracking-System (wie Jira, ServiceNow usw.) verantwortlich, wobei Daten verwendet werden, die während der Pipeline-Ausführung generiert wurden. Sie prüft den Pipeline-Kontext auf Aktualisierungsanweisungen und delegiert den eigentlichen Aktualisierungsvorgang an den konfigurierten Ticket-System-Adapter.

**Parameter:**

- **`modifier_config`** () - Konfigurationseinstellungen für den Ticket-Updater.
- **`ticket_system`** () - Adapter-Instanz zur Interaktion mit dem externen Ticketsystem.


::: details #### <Badge type="info" text="method"/> <span class='text-warning'>def</span> `__init__(self, config: RegistryInstanceConfig, ticket_system: TicketSystemAdapter)`
Initialisiert den `GenericTicketUpdater` mit Konfiguration und Ticket-System-Adapter.

**Parameter:**

- **`config`** () - Konfigurationsinstanz, die Einstellungen für die Pipeline-Komponente enthält.
- **`ticket_system`** () - Adapter-Objekt, das die Kommunikation mit dem externen Ticketsystem abwickelt.

:::


::: details #### <Badge type="info" text="method"/> <span class='text-warning'>def</span> `process(self, context: PipelineContext) -> PipelineContext`
Verarbeitet den Pipeline-Kontext, um das Ticket zu aktualisieren, falls Aktualisierungsdaten vorhanden sind.
Ruft Aktualisierungsdaten aus dem Kontext ab (insbesondere aus dem Schlüssel `"update_data"` in `context.data`) und aktualisiert das Ticket im Ticketsystem, wenn Aktualisierungsdaten vorhanden sind. Gibt den Kontext unverändert zurück.

**Parameter:**

- **`context`** () - Der Pipeline-Kontext, der Daten und Ticketinformationen enthält.

**Rückgabe:** () - Der ursprüngliche Pipeline-Kontext nach der Verarbeitung (unverändert).

:::


::: details #### <Badge type="info" text="method"/> <span class='text-warning'>def</span> `get_description() -> str`
Liefert eine Beschreibung des Zwecks der Pipe.

**Rückgabe:** () - Ein String, der die Funktionalität der Pipe beschreibt.

:::


---

## Modul: `open_ticket_ai\src\ce\run\pipe_implementations\hf_local_ai_inference_service.py`


### <span style='text-info'>class</span> `HFAIInferenceService`

Eine Klasse, die ein Hugging Face AI-Modell repräsentiert.
Diese Klasse ist ein Platzhalter für die zukünftige Implementierung von Funktionalitäten des Hugging Face AI-Modells. Derzeit enthält sie keine Methoden oder Eigenschaften.


::: details #### <Badge type="info" text="method"/> <span class='text-warning'>def</span> `__init__(self, config: RegistryInstanceConfig)`
Initialisiert den HFAIInferenceService mit der Konfiguration.

**Parameter:**

- **`config`** (`RegistryInstanceConfig`) - Konfigurationsinstanz für den Dienst.

:::


::: details #### <Badge type="info" text="method"/> <span class='text-warning'>def</span> `process(self, context: PipelineContext) -> PipelineContext`
Verarbeitet den Pipeline-Kontext, indem vorbereitete Daten als Modellergebnis gespeichert werden.
Diese Methode dient als Platzhalter für die eigentliche Modell-Inferenzlogik. Derzeit kopiert sie einfach die 'prepared_data' aus dem Kontext in 'model_result'.

**Parameter:**

- **`context`** (`PipelineContext`) - Der Pipeline-Kontext, der die zu verarbeitenden Daten enthält.

**Rückgabe:** (`PipelineContext`) - Der aktualisierte Pipeline-Kontext mit dem gespeicherten Modellergebnis.

:::


::: details #### <Badge type="info" text="method"/> <span class='text-warning'>def</span> `get_description() -> str`
Liefert eine Beschreibung des Dienstes.

**Rückgabe:** (`str`) - Beschreibungstext für den Hugging Face AI-Modelldienst.

:::


---

## Modul: `open_ticket_ai\src\ce\run\pipe_implementations\subject_body_preparer.py`


### <span style='text-info'>class</span> `SubjectBodyPreparer`

Eine Pipeline-Komponente, die den Betreff und den Inhalt eines Tickets für die Verarbeitung vorbereitet.
Diese Pipe extrahiert die Felder für Betreff und Inhalt aus den Ticketdaten, wiederholt den Betreff eine konfigurierbare Anzahl von Malen und verkettet ihn mit dem Inhalt. Die vorbereiteten Daten werden im Pipeline-Kontext für die nachgelagerte Verarbeitung gespeichert.

**Parameter:**

- **`preparer_config`** (`RegistryInstanceConfig`) - Konfigurationsparameter für den Preparer.


::: details #### <Badge type="info" text="method"/> <span class='text-warning'>def</span> `__init__(self, config: RegistryInstanceConfig)`
Initialisiert den SubjectBodyPreparer mit der Konfiguration.

**Parameter:**

- **`config`** (`RegistryInstanceConfig`) - Konfigurationsparameter für den Preparer.

:::


::: details #### <Badge type="info" text="method"/> <span class='text-warning'>def</span> `process(self, context: PipelineContext) -> PipelineContext`
Verarbeitet Ticketdaten, um Betreff und Inhalt vorzubereiten.
Extrahiert Betreff- und Inhaltsfelder aus den Kontextdaten, wiederholt den Betreff wie in der Konfiguration angegeben und verkettet ihn mit dem Inhalt. Speichert das Ergebnis im Kontext unter dem Schlüssel 'prepared_data'.

**Parameter:**

- **`context`** (`PipelineContext`) - Pipeline-Kontext, der Ticketdaten enthält.

**Rückgabe:** (`PipelineContext`) - Aktualisierter Kontext mit vorbereiteten Daten.

:::


::: details #### <Badge type="info" text="method"/> <span class='text-warning'>def</span> `get_description() -> str`
Liefert eine Beschreibung der Funktionalität der Pipe.

**Rückgabe:** (`str`) - Beschreibung des Zwecks der Pipe.

:::


---