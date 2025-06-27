# Dokumentation für `**/ce/run/managers/*.py`

## Modul: `open_ticket_ai\src\ce\run\managers\orchestrator.py`

Höchste Ebene der Orchestrierungs-Hilfsprogramme.

### <span style='color: #8E44AD;'>Klasse</span> `Orchestrator`

Führt Ticket-Verarbeitungspipelines aus.


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>Methode</span> <span style='color: #2980B9;'>def</span> `__init__(self, config: OpenTicketAIConfig, container: AbstractContainer)`</summary>

Initialisiert den Orchestrator mit Konfiguration und DI-Container.

**Parameter:**

- **`config`** () - Konfigurationseinstellungen für den Orchestrator.
- **`container`** () - Dependency-Injection-Container, der Pipeline-Instanzen bereitstellt.

</details>


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>Methode</span> <span style='color: #2980B9;'>def</span> `process_ticket(self, ticket_id: str, pipeline: Pipeline) -> PipelineContext`</summary>

Ruft Daten ab und führt ``pipeline`` für ``ticket_id`` aus.

</details>


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>Methode</span> <span style='color: #2980B9;'>def</span> `build_pipelines(self) -> None`</summary>

Instanziiert Pipeline-Objekte mittels DI-Container.

</details>


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>Methode</span> <span style='color: #2980B9;'>def</span> `set_schedules(self) -> None`</summary>

Plant die Pipeline-Ausführung gemäß Konfiguration.

</details>


---