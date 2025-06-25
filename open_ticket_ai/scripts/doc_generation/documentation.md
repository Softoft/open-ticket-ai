# Project Documentation

## Module: `src\ce\app.py`

### `class App`

Main application entry point.

#### `def __init__(self, config, validator, orchestrator)`

```text
Initialize the application.

Args:
    config: Loaded configuration for the application.
    validator: Validator used to check the configuration.
    orchestrator: Orchestrator used to run attribute predictors.
```

#### `def run(self)`

```text
Validate configuration and start the scheduler loop.

This method:
1. Validates the application configuration
2. Sets up scheduled jobs using the orchestrator
3. Enters an infinite loop to run pending scheduled tasks
```


---

## Module: `src\ce\core\config\config_models.py`

### `class SystemConfig`

Configuration for the ticket system adapter.

### `class FetcherConfig`

Configuration for data fetchers.

### `class PreparerConfig`

Configuration for data preparers.

### `class ModifierConfig`

Configuration for modifiers.

### `class AIInferenceServiceConfig`

Configuration for AI inference services.

### `class SchedulerConfig`

Configuration for scheduling recurring tasks.

### `class PipelineConfig`

Configuration for a single pipeline workflow.

#### `def validate_pipe_ids_are_registered(self, all_pipe_ids)`

```text
Validate that all pipe IDs in this pipeline exist.
```

### `class OpenTicketAIConfig`

Root configuration model for Open Ticket AI.

#### `def cross_validate_references(self)`

```text
Validate that all pipeline references to components exist.
```

#### `def get_all_register_instance_configs(self)`

```text
Return all registered instances in the configuration.
```

### `def load_config(path)`

```text
Load a YAML configuration file from ``path``.
```


---

## Module: `src\ce\core\config\config_validator.py`

### `class OpenTicketAIConfigValidator`

Validate configuration values against the registry.

#### `def __init__(self, config, registry)`

```text
Create a new validator.

Args:
    config: Loaded ``OpenTicketAIConfig`` instance.
    registry: Registry containing available classes.
```

#### `def validate_registry(self)`

```text
Ensure all configured providers are registered.
```


---

## Module: `src\ce\core\dependency_injection\abstract_container.py`

### `class AbstractContainer`

Abstract interface for dependency containers.

#### `def get_instance(self, provider_key, subclass_of)`

```text
Retrieve an instance from the container.

The instance is retrieved based on the provider key and must be a subclass of the given type.

Args:
    provider_key: The key identifying the provider for the instance.
    subclass_of: The class (or type) of the instance to be retrieved. The type T must be a subclass of
        `RegistryProvidableInstance`.

Returns:
    An instance of the type specified by `subclass_of` (or a subclass).
```


---

## Module: `src\ce\core\dependency_injection\container.py`

### `class AppModule`

Injector module that binds the validated configuration.

#### `def configure(self, binder)`

```text
Bind core configuration objects.
```

#### `def provide_validator(self, config, registry)`

```text
Provide a configuration validator instance.
```

#### `def provide_otobo_client(self, config)`

```text
Create an :class:`OTOBOClient` using the system configuration.
```

### `class DIContainer`

Dependency injection container for Open Ticket AI.

#### `def __init__(self)`

```text
Initialize the container and bind common instances.
```

#### `def get_instance_config(self, id)`

```text
Retrieve the configuration for a specific instance by its ID.

Args:
    id: The unique identifier of the instance configuration to retrieve.

Returns:
    The configuration object for the specified instance.

Raises:
    KeyError: If no configuration is found for the given ID.
```

#### `def get_instance(self, id, subclass_of)`

```text
Return an instance from the registry.

Args:
    id: Identifier of the desired instance.
    subclass_of: Expected base class of the instance.
    config_list: List of configuration entries to search in.

Returns:
    The created instance of ``subclass_of``.
```

#### `def get_pipeline(self, predictor_id)`

```text
Create an attribute predictor instance by its ID.
```


---

## Module: `src\ce\core\dependency_injection\create_registry.py`

### `def create_registry()`

```text
Create the default class registry.
```


---

## Module: `src\ce\core\dependency_injection\registry.py`

### `class Registry`

Simple class registry used for dependency lookup.

#### `def __init__(self)`

```text
Create an empty registry.
```

#### `def register_all(self, instance_classes)`

```text
Register multiple classes at once.
```

#### `def register(self, instance_class)`

```text
Register a single class with an optional key.
```

#### `def get(self, registry_instance_key, instance_class)`

```text
Retrieve a registered class and validate its type.
```

#### `def contains(self, registry_instance_key)`

```text
Check whether a key is registered under a compatible type.
```

#### `def get_registry_types_descriptions(self)`

```text
Return a list of all registered types and descriptions.
```

#### `def get_all_registry_keys(self)`

```text
Return a list of all registered keys.
```

#### `def get_type_from_key(self, registry_instance_key)`

```text
Get the type of a registered instance by its key.
```


---

## Module: `src\ce\core\mixins\registry_instance_config.py`

### `class RegistryInstanceConfig`

Base configuration for registry instances.


---

## Module: `src\ce\core\mixins\registry_providable_instance.py`

### `class RegistryProvidableInstance`

Base class for objects that can be provided by a registry.

This class provides common functionality for registry-managed objects including
configuration storage, pretty printing of configuration, and provider registration.

Attributes:
    console (Console): Rich console instance for output formatting.
    config (RegistryInstanceConfig): Configuration object for this instance.

#### `def __init__(self, config, console=None)`

```text
Store the configuration and pretty print it.
```

#### `def _pretty_print(self)`

```text
Pretty print the configuration of the class.
```

#### `def get_provider_key(cls)`

```text
Return the provider key for the class.

This key is used to register and retrieve instances from the registry.
```

#### `def get_description()`

```text
Return a human readable description for the class.
```


---

## Module: `src\ce\core\util\create_json_config_schema.py`

### `class RootConfig`

Wrapper model used for schema generation.


---

## Module: `src\ce\core\util\path_util.py`

### `def find_project_root(project_name='open_ticket_ai')`

```text
Search parent directories for the project root.

This function traverses upwards from the current file's directory to locate
the root directory of the project identified by the given name.

Args:
    project_name: The name of the project root directory to find.
        Defaults to 'open_ticket_ai'.

Returns:
    Path: The absolute path to the project root directory.

Raises:
    FileNotFoundError: If the project root directory cannot be found in any
        parent directories.
```


---

## Module: `src\ce\core\util\pretty_print_config.py`

### `def pretty_print_config(config, console)`

```text
Pretty print a pydantic model using ``rich``.

This function converts a Pydantic BaseModel to a dictionary, serializes it to YAML,
and prints it to the console using rich's syntax highlighting.

Args:
    config (BaseModel): The Pydantic model configuration to display.
    console (Console): The rich console instance for output rendering.
```


---

## Module: `src\ce\main.py`

Open Ticket AI CLI entry point.

This module provides the command-line interface for the Open Ticket AI application.
It configures logging levels and launches the main application.

### `def main(verbose=typer.Option(False, '-v', '--verbose', help='INFO-level logging'), debug=typer.Option(False, '-d', '--debug', help='DEBUG-level logging'))`

```text
Configure logging based on CLI options.

Args:
    verbose (bool): Enable INFO-level logging when True.
    debug (bool): Enable DEBUG-level logging when True.
```

### `def start()`

```text
Initialize the container and start the application.
```


---

## Module: `src\ce\run\ai_models\hf_local_ai_inference_service.py`

### `class HFAIInferenceService`

A class representing a Hugging Face AI model.

This class is a placeholder for future implementation of Hugging Face AI model functionalities.
Currently, it does not contain any methods or properties.

#### `def __init__(self, config)`

```text
Initializes the HFAIInferenceService with configuration.

Args:
    config (RegistryInstanceConfig): Configuration instance for the service.
```

#### `def process(self, context)`

```text
Processes pipeline context by storing prepared data as model result.

Args:
    context (PipelineContext): The pipeline context containing data to process.

Returns:
    PipelineContext: The updated pipeline context with model result stored.
```

#### `def get_description()`

```text
Provides a description of the service.

Returns:
    str: Description text for the Hugging Face AI model service.
```


---

## Module: `src\ce\run\fetchers\basic_ticket_fetcher.py`

### `class BasicTicketFetcher`

Simple fetcher that loads ticket data using the ticket system adapter.

#### `def __init__(self, config, ticket_system)`

```text
Initializes the BasicTicketFetcher with configuration and ticket system adapter.

Args:
    config: The configuration instance for the fetcher.
    ticket_system: The adapter for interacting with the ticket system.
```

#### `def process(self, context)`

```text
Fetches ticket data and updates the pipeline context.

Retrieves the ticket using the ticket ID from the context and updates
the context's data dictionary with the ticket information.

Args:
    context: The pipeline context containing the ticket ID.

Returns:
    PipelineContext: The updated pipeline context with ticket data.
```

#### `def get_description()`

```text
Provides a description of this pipe's functionality.

Returns:
    str: A description of the pipe.
```


---

## Module: `src\ce\run\modifiers\generic_ticket_updater.py`

### `class GenericTicketUpdater`

Update a ticket in the ticket system using data from the context.

#### `def __init__(self, config, ticket_system)`

```text
Initializes the GenericTicketUpdater with configuration and ticket system adapter.

Args:
    config: Configuration instance for the pipeline component.
    ticket_system: Adapter for interacting with the ticket system.
```

#### `def process(self, context)`

```text
Processes the pipeline context to update the ticket if update data exists.

Retrieves update data from the context and updates the ticket in the ticket system
if update data is present. Returns the context unchanged.

Args:
    context: The pipeline context containing data and ticket information.

Returns:
    The original pipeline context after processing.
```

#### `def get_description()`


---

## Module: `src\ce\run\orchestrator.py`

Top level orchestration utilities.

### `class Orchestrator`

Execute ticket processing pipelines.

#### `def __init__(self, config, container)`

```text
Initialize the Orchestrator with configuration and DI container.

Args:
    config: Configuration settings for the orchestrator.
    container: Dependency injection container providing pipeline instances.
```

#### `def process_ticket(self, ticket_id, pipeline)`

```text
Fetch data and run ``pipeline`` for ``ticket_id``.
```

#### `def build_pipelines(self)`

```text
Instantiate pipeline objects using the DI container.
```

#### `def set_schedules(self)`

```text
Schedule pipeline execution according to configuration.
```


---

## Module: `src\ce\run\pipeline\context.py`

### `class PipelineContext`

Context object passed between pipeline stages.

Attributes:
    ticket_id (str): The ID of the ticket being processed.
    data (dict[str, Any]): A dictionary to hold arbitrary data for the pipeline stages. Defaults to an empty dictionary.


---

## Module: `src\ce\run\pipeline\pipe.py`

### `class Pipe`

Interface for all pipeline components.

#### `def process(self, context)`

```text
Process ``context`` and return it.
```


---

## Module: `src\ce\run\pipeline\pipeline.py`

### `class Pipeline`

Composite pipe executing a sequence of pipes.

#### `def __init__(self, config, pipes)`

```text
Initializes the Pipeline with configuration and component pipes.

Args:
    config: Configuration settings for the pipeline.
    pipes: Ordered list of Pipe instances to execute sequentially.
```

#### `def execute(self, context)`

```text
Executes all pipes in the pipeline sequentially.

Processes the context through each pipe in the defined order, passing
the output of one pipe as input to the next.

Args:
    context: The initial pipeline context containing data to process.

Returns:
    The final context after processing through all pipes.
```

#### `def process(self, context)`

```text
Processes context through the entire pipeline.

This method implements the Pipe interface by delegating to execute().

Args:
    context: The pipeline context to process.

Returns:
    The modified context after pipeline execution.
```


---

## Module: `src\ce\run\preparers\subject_body_preparer.py`

### `class SubjectBodyPreparer`

Extract and concatenate the ticket subject and body.

#### `def __init__(self, config)`

```text
Initializes the SubjectBodyPreparer with configuration.

Args:
    config (RegistryInstanceConfig): Configuration parameters for the preparer.
```

#### `def process(self, context)`

```text
Processes ticket data to prepare subject and body content.

Extracts subject and body fields from context data, repeats the subject
as specified in configuration, and concatenates with the body. Stores
the result in context under 'prepared_data' key.

Args:
    context (PipelineContext): Pipeline context containing ticket data.

Returns:
    PipelineContext: Updated context with prepared data.
```

#### `def get_description()`

```text
Provides a description of the pipe's functionality.

Returns:
    str: Description of the pipe's purpose.
```


---

## Module: `src\ce\ticket_system_integration\otobo_adapter.py`

### `class OTOBOAdapter`

Adapter for OTOBO ticket system integration.
This class provides methods to interact with the OTOBO API.

#### `def get_description()`

```text
Return a description of the adapter's functionality.

Returns:
    str: A description of the OTOBO adapter.
```

#### `def __init__(self, config, otobo_client)`

```text
Initialize the OTOBO adapter with configuration and client.

Args:
    config (SystemConfig): System configuration object.
    otobo_client (OTOBOClient): Client for interacting with OTOBO API.
```

#### `async def find_tickets(self, query)`

```text
Return all tickets matching ``query``.

Args:
    query (dict): Search parameters for tickets.

Returns:
    list[dict]: List of tickets matching the query.
```

#### `async def find_first_ticket(self, query)`

```text
Return the first ticket found for ``query`` if available.

Args:
    query (dict): Search parameters for tickets.

Returns:
    dict | None: First matching ticket dictionary or None if none found.
```

#### `async def update_ticket(self, ticket_id, data)`

```text
Update ``ticket_id`` with ``data`` and return the updated record.

Args:
    ticket_id (str): ID of the ticket to update.
    data (dict): Update parameters for the ticket.

Returns:
    dict: Updated ticket record.
```


---

## Module: `src\ce\ticket_system_integration\otobo_adapter_config.py`

### `class OTOBOAdapterConfig`

Configuration model for OTOBO adapter.

Attributes:
    server_address (str): The base URL of the OTOBO server.
    webservice_name (str): The name of the web service to use.
    search_operation_url (str): The URL for the search operation.
    update_operation_url (str): The URL for the update operation.
    get_operation_url (str): The URL for the get operation.
    username (str): The username for authentication.
    password_env_var (str): The environment variable that contains the password.

#### `def __str__(self)`

```text
Return a string representation of the configuration.
```

#### `def password(self)`

```text
Retrieves the password from the environment variable specified in the configuration.

Returns:
    str: The password for authentication.
```


---

## Module: `src\ce\ticket_system_integration\otobo_adapter_test.py`

### `def adapter_and_client()`

```text
Fixture that provides an instance of OTOBOAdapter and a mocked OTOBOClient.

Returns:
    tuple: A tuple containing:
        adapter (OTOBOAdapter): Configured OTOBOAdapter instance
        client (AsyncMock): Mocked OTOBOClient instance
```

### `def test_config_str_and_password(monkeypatch)`

```text
Test OTOBOAdapterConfig string representation and password retrieval from environment.

Verifies:
    1. The __str__ method excludes the password value
    2. Password is correctly retrieved from environment variable
```

### `def test_config_password_missing_env(monkeypatch)`

```text
Test OTOBOAdapterConfig raises error when password environment variable is missing.

Verifies:
    Accessing password property raises ValueError when env var doesn't exist
```

### `def test_find_tickets(adapter_and_client)`

```text
Test find_tickets correctly processes search queries and returns results.

Verifies:
    1. Query parameters are correctly passed to OTOBO client
    2. Results are properly converted to dictionaries
```

### `def test_find_first_ticket(adapter_and_client)`

```text
Test find_first_ticket returns first match or None when no tickets found.

Verifies:
    1. Returns first ticket when matches exist
    2. Returns None when no tickets match the query
```

### `def test_update_ticket(adapter_and_client)`

```text
Test update_ticket correctly formats payload and processes response.

Verifies:
    1. Update parameters are correctly converted to OTOBO format
    2. Response data is properly returned
```


---

## Module: `src\ce\ticket_system_integration\ticket_system_adapter.py`

### `class TicketSystemAdapter`

An abstract base class for ticket system adapters.
This class defines the
interface that all ticket system adapters must implement.

#### `def __init__(self, config)`

```text
Initialize the adapter with system configuration.
```

#### `async def update_ticket(self, ticket_id, data)`

```text
Update a ticket in the system.

Args:
    ticket_id: Ticket identifier.
    data: Attributes to update.

Returns:
    Optional[dict]: Updated ticket information.
```

#### `async def find_tickets(self, query)`

```text
Search for tickets matching ``query``.

Args:
    query: Search parameters for the ticket system.

Returns:
    list[dict]: Matching tickets.
```

#### `async def find_first_ticket(self, query)`

```text
Return the first ticket that matches ``query`` if any.

Args:
    query: Search parameters for the ticket system.

Returns:
    Optional[dict]: The first matching ticket or None if no ticket is found.
```


---
