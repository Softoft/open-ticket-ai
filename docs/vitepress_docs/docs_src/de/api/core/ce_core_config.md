# Dokumentation für `**/ce/core/config/**/*.py`

## Modul: `open_ticket_ai\src\ce\core\config\config_models.py`


### <span style='color: #8E44AD;'>class</span> `SystemConfig`

Konfiguration für den Ticket-System-Adapter.

### <span style='color: #8E44AD;'>class</span> `FetcherConfig`

Konfiguration für Datenabrufer.

### <span style='color: #8E44AD;'>class</span> `PreparerConfig`

Konfiguration für Datenaufbereiter.

### <span style='color: #8E44AD;'>class</span> `ModifierConfig`

Konfiguration für Modifikatoren.

### <span style='color: #8E44AD;'>class</span> `AIInferenceServiceConfig`

Konfiguration für KI-Inferenzdienste.

### <span style='color: #8E44AD;'>class</span> `SchedulerConfig`

Konfiguration für die Planung wiederkehrender Aufgaben.

### <span style='color: #8E44AD;'>class</span> `PipelineConfig`

Konfiguration für einen einzelnen Pipeline-Workflow.


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `validate_pipe_ids_are_registered(self, all_pipe_ids: set[str]) -> None`</summary>

Stellen Sie sicher, dass alle Pipe-IDs in dieser Pipeline vorhanden sind.

</details>

### <span style='color: #8E44AD;'>class</span> `OpenTicketAIConfig`

Hauptkonfigurationsmodell für Open Ticket AI.


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `cross_validate_references(self) -> Self`</summary>

Stellen Sie sicher, dass alle Pipeline-Verweise auf Komponenten vorhanden sind.

</details>


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `get_all_register_instance_configs(self) -> list[RegistryInstanceConfig]`</summary>

Gibt alle registrierten Instanzen in der Konfiguration zurück.

</details>


### <span style='color: #2980B9;'>def</span> `load_config(path: str) -> OpenTicketAIConfig`

Lädt eine YAML-Konfigurationsdatei von ``path``.



---

## Modul: `open_ticket_ai\src\ce\core\config\config_validator.py`


### <span style='color: #8E44AD;'>class</span> `OpenTicketAIConfigValidator`

Validiert Konfigurationswerte gegen das Registry.


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `__init__(self, config: OpenTicketAIConfig, registry: Registry)`</summary>

Erstellt einen neuen Validator.

**Parameter:**

- **`config`** () - Geladene ``OpenTicketAIConfig``-Instanz.
- **`registry`** () - Registry mit verfügbaren Klassen.

</details>


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `validate_registry(self) -> None`</summary>

Stellen Sie sicher, dass alle konfigurierten Provider registriert sind.

</details>


---