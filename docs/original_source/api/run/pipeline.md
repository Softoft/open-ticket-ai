---
description: This documentation outlines a modular Python framework for building sequential
  data processing pipelines. It details core components such as `Pipeline` for managing
  execution flow, the `Pipe` interface for creating individual processing stages,
  and `PipelineContext` for passing state and data between pipes. The system includes
  robust features for status tracking, error handling, and controlled pipeline termination,
  enabling the creation of resilient and maintainable data workflows.
---
# Documentation for `**/ce/run/pipeline/*.py`

## Module: `open_ticket_ai\src\ce\run\pipeline\context.py`


### <span style='text-info'>class</span> `PipelineContext`

Context object passed between pipeline stages.
This class serves as a container for sharing state and data across different stages
of a processing pipeline. It uses Pydantic for data validation and serialization.

**Parameters:**

- **`ticket_id`** (`str`) - The unique identifier of the ticket being processed through
the pipeline stages.
- **`data`** (`dict[str, Any]`) - A flexible dictionary for storing arbitrary data exchanged
between pipeline stages. Defaults to an empty dictionary.


::: details #### <Badge type="info" text="method"/> <span class='text-warning'>def</span> `stop_pipeline(self)`
A convenience method for pipes to signal a controlled stop.

:::


---

## Module: `open_ticket_ai\src\ce\run\pipeline\meta_info.py`


### <span style='text-info'>class</span> `MetaInfo`

Stores metadata about the pipeline execution state.
This model captures the current status of a pipeline along with any error
information when failures occur.

**Parameters:**

- **`status`** () (default: `RUNNING`) - Current execution status of the pipeline. Defaults to RUNNING.
- **`error_message`** () - Detailed error message if the pipeline failed. None if successful.
- **`failed_pipe`** () - Identifier of the specific pipe that caused failure. None if successful.


---

## Module: `open_ticket_ai\src\ce\run\pipeline\pipe.py`


### <span style='text-info'>class</span> `Pipe`

Interface for all pipeline components.
This abstract base class defines the common interface that all pipeline
components must implement. It inherits from `Providable`
to enable automatic registration in a component registry and from `ABC`
to enforce abstract method implementation.

Subclasses must implement the `process` method to define their specific
data transformation logic within the pipeline.

Attributes:
    Inherits attributes from `Providable` for registry management.
    InputDataType (type[InputDataT]): The type of the input data model 
        expected by this pipe component.
    OutputDataType (type[OutputDataT]): The type of the output data model 
        produced by this pipe component.


::: details #### <Badge type="info" text="method"/> <span class='text-warning'>def</span> `process(self, context: PipelineContext[InputDataT]) -> PipelineContext[OutputDataT]`
Process a pipeline context object and return the modified context.
This method defines the core processing logic for a pipeline component.
It takes a `PipelineContext` object containing shared pipeline state,
performs transformations or operations on this context, and returns the
updated context for the next component in the pipeline.

Args:
    context: The current pipeline context containing shared state data.

Returns:
    The updated `PipelineContext` object after processing.

Raises:
    Implementation-specific exceptions may be raised by subclasses to
    indicate processing errors or invalid states.

:::


---

## Module: `open_ticket_ai\src\ce\run\pipeline\pipeline.py`


### <span style='text-info'>class</span> `Pipeline`

A pipeline that executes a sequence of pipes sequentially.
This class manages the execution flow of multiple pipes, handling status transitions,
error propagation, and stop requests during processing.

**Parameters:**

- **`pipes`** () - List of Pipe objects to execute in sequence.


::: details #### <Badge type="info" text="method"/> <span class='text-warning'>def</span> `__init__(self, config: PipelineConfig, pipes: List[Pipe])`
Initializes the Pipeline with configuration and pipe sequence.

**Parameters:**

- **`config`** () - Configuration settings for the pipeline.
- **`pipes`** () - Ordered list of Pipe instances to execute.

:::


::: details #### <Badge type="info" text="method"/> <span class='text-warning'>def</span> `execute(self, context: PipelineContext) -> PipelineContext`
Executes all pipes sequentially with error handling and status propagation.
Processes each pipe in sequence while:
- Validating input data using each pipe's input model
- Handling STOPPED status requests from pipes
- Catching and logging exceptions during pipe execution
- Updating context status appropriately (RUNNING, SUCCESS, FAILED, STOPPED)

**Parameters:**

- **`context`** () - The pipeline context containing execution state and data.

**Returns:** () - Updated PipelineContext reflecting final execution state after processing.

:::


::: details #### <Badge type="info" text="method"/> <span class='text-warning'>def</span> `process(self, context: PipelineContext) -> PipelineContext`
Processes context through the entire pipeline sequence.
Implements the abstract method from the Pipe base class. Delegates to
the `execute()` method for actual pipeline processing.

**Parameters:**

- **`context`** () - The pipeline context containing execution state and data.

**Returns:** () - Updated PipelineContext after processing through all pipes.

:::


---

## Module: `open_ticket_ai\src\ce\run\pipeline\status.py`


### <span style='text-info'>class</span> `PipelineStatus`

Represents the possible states of a pipeline execution.
This enum defines the various statuses a pipeline can have during its lifecycle.

**Parameters:**

- **`RUNNING`** () - Indicates the pipeline is currently executing.
- **`SUCCESS`** () - Indicates the pipeline completed successfully without errors.
- **`STOPPED`** () - Indicates the pipeline was intentionally halted (controlled stop).
- **`FAILED`** () - Indicates the pipeline terminated due to an unexpected error.


---
