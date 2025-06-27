# Documentation for `**/ce/core/config/**/*.py`

## Module: `open_ticket_ai\src\ce\core\config\config_models.py`


### <span style='color: #8E44AD;'>class</span> `SystemConfig`

Configuration for the ticket system adapter.

### <span style='color: #8E44AD;'>class</span> `FetcherConfig`

Configuration for data fetchers.

### <span style='color: #8E44AD;'>class</span> `PreparerConfig`

Configuration for data preparers.

### <span style='color: #8E44AD;'>class</span> `ModifierConfig`

Configuration for modifiers.

### <span style='color: #8E44AD;'>class</span> `AIInferenceServiceConfig`

Configuration for AI inference services.

### <span style='color: #8E44AD;'>class</span> `SchedulerConfig`

Configuration for scheduling recurring tasks.

### <span style='color: #8E44AD;'>class</span> `PipelineConfig`

Configuration for a single pipeline workflow.


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `validate_pipe_ids_are_registered(self, all_pipe_ids: set[str]) -> None`</summary>

Validate that all pipe IDs in this pipeline exist.

</details>

### <span style='color: #8E44AD;'>class</span> `OpenTicketAIConfig`

Root configuration model for Open Ticket AI.


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `cross_validate_references(self) -> Self`</summary>

Validate that all pipeline references to components exist.

</details>


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `get_all_register_instance_configs(self) -> list[RegistryInstanceConfig]`</summary>

Return all registered instances in the configuration.

</details>


### <span style='color: #2980B9;'>def</span> `load_config(path: str) -> OpenTicketAIConfig`

Load a YAML configuration file from ``path``.



---

## Module: `open_ticket_ai\src\ce\core\config\config_validator.py`


### <span style='color: #8E44AD;'>class</span> `OpenTicketAIConfigValidator`

Validate configuration values against the registry.


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `__init__(self, config: OpenTicketAIConfig, registry: Registry)`</summary>

Create a new validator.

**Parameters:**

- **`config`** () - Loaded ``OpenTicketAIConfig`` instance.
- **`registry`** () - Registry containing available classes.

</details>


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `validate_registry(self) -> None`</summary>

Ensure all configured providers are registered.

</details>


---
