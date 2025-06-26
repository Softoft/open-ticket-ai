# Documentation for `**/ce/run/managers/*.py`

## Module: `open_ticket_ai\src\ce\run\managers\orchestrator.py`

Top level orchestration utilities.

### <span style='color: #8E44AD;'>class</span> `Orchestrator`

Execute ticket processing pipelines.


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `__init__(self, config: OpenTicketAIConfig, container: AbstractContainer)`</summary>

Initialize the Orchestrator with configuration and DI container.

**Parameters:**

- **`config`** () - Configuration settings for the orchestrator.
- **`container`** () - Dependency injection container providing pipeline instances.

</details>


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `process_ticket(self, ticket_id: str, pipeline: Pipeline) -> PipelineContext`</summary>

Fetch data and run ``pipeline`` for ``ticket_id``.

</details>


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `build_pipelines(self) -> None`</summary>

Instantiate pipeline objects using the DI container.

</details>


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `set_schedules(self) -> None`</summary>

Schedule pipeline execution according to configuration.

</details>


---
