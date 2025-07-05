---
description: Explore the OpenTicketAI `Orchestrator` class, a core component for automating
  ticket processing workflows. This Python module manages the complete lifecycle of
  pipelines, including instantiation via dependency injection, individual ticket processing,
  and scheduled execution for continuous automation.
---
# Documentation for `**/ce/run/managers/*.py`

## Module: `open_ticket_ai\src\ce\run\managers\orchestrator.py`

Top level orchestration utilities.

### <span style='text-info'>class</span> `Orchestrator`

Orchestrates the execution of ticket processing pipelines.
This class manages the lifecycle of pipelines including:
- Pipeline instantiation via dependency injection
- Individual ticket processing
- Scheduled execution of pipelines

**Parameters:**

- **`config`** () - Configuration settings for the orchestrator
- **`container`** () - Dependency injection container providing pipeline instances
- **`_logger`** () - Logger instance for orchestration operations
- **`_pipelines`** () - Dictionary mapping pipeline IDs to pipeline instances


::: details #### <Badge type="info" text="method"/> <span class='text-warning'>def</span> `__init__(self, config: OpenTicketAIConfig, container: AbstractContainer)`
Initialize the Orchestrator with configuration and DI container.

**Parameters:**

- **`config`** () - Configuration settings for the orchestrator.
- **`container`** () - Dependency injection container providing pipeline instances.

:::


::: details #### <Badge type="info" text="method"/> <span class='text-warning'>def</span> `process_ticket(self, ticket_id: str, pipeline: Pipeline) -> PipelineContext`
Executes a pipeline for a specific ticket.
Creates a processing context and runs the specified pipeline to process
the given ticket. This is the core method for individual ticket processing.

**Parameters:**

- **`ticket_id`** () - Unique identifier of the ticket to process.
- **`pipeline`** () - Pipeline instance to execute.

**Returns:** (`PipelineContext`) - The execution context containing results and state
after pipeline execution.

:::


::: details #### <Badge type="info" text="method"/> <span class='text-warning'>def</span> `build_pipelines(self) -> None`
Instantiates all configured pipeline objects.
Uses the dependency injection container to create pipeline instances
based on the configuration. Populates the internal pipeline registry
with pipeline ID to instance mappings.

:::


::: details #### <Badge type="info" text="method"/> <span class='text-warning'>def</span> `set_schedules(self) -> None`
Configures scheduled execution for all pipelines.
Performs the following operations:
1. Builds pipelines if not already instantiated
2. Configures periodic execution for each pipeline according to its
   schedule configuration using the `schedule` library

The scheduling uses the following configuration parameters:
- interval: Numeric interval value
- unit: Time unit (e.g., minutes, hours, days)

Note:
- Uses `schedule.every(interval).unit` pattern for scheduling
- Passes an empty ticket_id context during scheduled executions

:::


---
