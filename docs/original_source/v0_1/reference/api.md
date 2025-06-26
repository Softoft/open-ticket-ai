# Open Ticket AI - Reference

## Module: `open_ticket_ai\experimental\anonymize_data.py`



### <span style='color: #2980B9;'>def</span> `anonymize_text(text)`

Anonymize sensitive information in a given text.

**Parameters:**

- **`text`** (`str`) - The input text to anonymize.

**Returns:** (`str`) - The anonymized text with replaced named entities, email addresses, phone numbers, IBANs, and addresses.



---

## Module: `open_ticket_ai\experimental\email_extraction.py`

### ⚠️ Error parsing `open_ticket_ai\experimental\email_extraction.py`

```
expected an indented block after function definition on line 14 (<unknown>, line 15)
```


---

## Module: `open_ticket_ai\scripts\doc_generation\add_docstrings.py`



### <span style='color: #2980B9;'>def</span> `find_python_files(path: Path) -> list[Path]`

Recursively finds all Python files in a given path, respecting exclusion rules.

**Parameters:**

- **`path`** () - The root directory path to start searching from.

**Returns:** () - A list of Path objects representing Python files to process.



### <span style='color: #2980B9;'>def</span> `clean_ai_response(response_text: str) -> str`

Cleans the AI's response to ensure it's only valid Python code.
It removes markdown code fences and any leading/trailing text.

**Parameters:**

- **`response_text`** () - The raw text response from the AI model.

**Returns:** () - Cleaned Python code string extracted from the response.



### <span style='color: #2980B9;'>async def</span> `add_docstrings_to_file_content(file_content: str) -> str | None`

Sends the entire file content to an AI model to add missing docstrings.

**Parameters:**

- **`file_content`** () - A string containing the entire source code of a Python file.

**Returns:** () - The updated file content with docstrings, or None if it fails.



### <span style='color: #2980B9;'>async def</span> `process_file(file_path: Path)`

Processes a single Python file by sending it to the AI for docstring
addition and overwriting the file with the result.

**Parameters:**

- **`file_path`** () - The path to the Python file to process.



### <span style='color: #2980B9;'>async def</span> `main()`

Main asynchronous function to orchestrate the docstring generation process.



---

## Module: `open_ticket_ai\scripts\doc_generation\example_package\main_module.py`

### ⚠️ Error parsing `open_ticket_ai\scripts\doc_generation\example_package\main_module.py`

```
'DocstringRaises' object has no attribute 'default'
```


---

## Module: `open_ticket_ai\scripts\doc_generation\generate_docs.py`

A script to generate beautiful Markdown documentation from Python source code.
This script uses Python's `ast` module to traverse the source code,
extracting classes, functions, and their docstrings. It then parses the
docstrings (supports Google, reStructuredText, and Numpydoc styles) and
formats the output into a clean, modern Markdown file.

Features:
-   Class and function-based structure.
-   Rich parsing of docstrings for parameters, returns, and raises sections.
-   Inclusion of type hints in signatures.
-   Modern Markdown styling with badges and collapsible sections.
-   Fully configurable via command-line arguments.

### <span style='color: #8E44AD;'>class</span> `DocstringStyler`

Provides methods to style parsed docstring components into Markdown.


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `style_params(params: List[dict], title: str) -> str`</summary>

Styles a list of parameters into a Markdown list.

</details>


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `style_returns(returns: Optional[dict]) -> str`</summary>

Styles the returns section into Markdown.

</details>

### <span style='color: #8E44AD;'>class</span> `MarkdownVisitor`

An AST visitor that traverses a Python file and builds a Markdown documentation string.


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `__init__(self, file_path: Path)`</summary>


</details>


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `visit_ClassDef(self, node: ast.ClassDef)`</summary>

Processes a class definition.

</details>


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `visit_FunctionDef(self, node: ast.FunctionDef)`</summary>

Processes a function or method definition.

</details>


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef)`</summary>

Processes an async function or method definition.

</details>


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `get_markdown(self) -> str`</summary>

Returns the accumulated Markdown content.

</details>


### <span style='color: #2980B9;'>def</span> `parse_python_file(file_path: Path) -> str`

Parses a Python file and returns its documentation in Markdown.



### <span style='color: #2980B9;'>def</span> `main()`

Main function to run the documentation generator.



---

## Module: `open_ticket_ai\scripts\doc_generation\translate_docs.py`



### <span style='color: #2980B9;'>def</span> `translate_text(content: str, target_lang: str, model: str, api_key: str) -> str`

Translate markdown *content* to *target_lang* using OpenRouter.

**Parameters:**

- **`content`** () - The markdown content to translate.
- **`target_lang`** () - Target language code (e.g., 'de', 'en').
- **`model`** () - OpenRouter model identifier.
- **`api_key`** () - OpenRouter API key.

**Returns:** () - Translated markdown content.



### <span style='color: #2980B9;'>def</span> `process_file(path: Path, root: Path, languages: List[str], model: str, api_key: str, out_dir: Path) -> None`

Translate a single Markdown *path* and write results under *out_dir*.

**Parameters:**

- **`path`** () - Path to the markdown file to translate.
- **`root`** () - Root directory of the documentation.
- **`languages`** () - List of target language codes.
- **`model`** () - OpenRouter model identifier.
- **`api_key`** () - OpenRouter API key.
- **`out_dir`** () - Base output directory for translations.



### <span style='color: #2980B9;'>def</span> `main() -> None`

Main entry point for translating Markdown documentation using OpenRouter.
Parses command-line arguments for the translation process, including the input
directory of Markdown documents, target languages, OpenRouter model, and output
directory. Then, iterates over the input directory, processing each Markdown file
using the provided arguments.

**Returns:** () - None



---

## Module: `open_ticket_ai\scripts\license_script.py`



### <span style='color: #2980B9;'>def</span> `find_start_of_code(lines)`

Return the index of the first non-comment line.

**Parameters:**

- **`lines`** (`list`) - List of strings representing lines in a file.

**Returns:** (`int`) - Index of the first line that is not a comment or whitespace.



### <span style='color: #2980B9;'>def</span> `read_file(filepath)`

Read all lines from ``filepath``.

**Parameters:**

- **`filepath`** (`str`) - Path to the file to read.

**Returns:** (`list`) - List of strings representing lines in the file.



### <span style='color: #2980B9;'>def</span> `write_file(filepath, lines)`

Write ``lines`` to ``filepath``.

**Parameters:**

- **`filepath`** (`str`) - Path to the file to write.
- **`lines`** (`list`) - List of strings to write to the file.



### <span style='color: #2980B9;'>def</span> `update_license_in_files(directory)`

Insert the license notice at the top of all ``.py`` files.
Walks through all Python files in the specified directory and replaces
any existing license notice with the new license notice. Handles empty
files and files containing only comments appropriately.

**Parameters:**

- **`directory`** (`str`) - Path to the directory containing files to update.



---

## Module: `open_ticket_ai\src\ce\app.py`


### <span style='color: #8E44AD;'>class</span> `App`

Main application entry point.


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `__init__(self, config: OpenTicketAIConfig, validator: OpenTicketAIConfigValidator, orchestrator: Orchestrator)`</summary>

Initialize the application.

**Parameters:**

- **`config`** () - Loaded configuration for the application.
- **`validator`** () - Validator used to check the configuration.
- **`orchestrator`** () - Orchestrator used to run attribute predictors.

</details>


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `run(self)`</summary>

Validate configuration and start the scheduler loop.
This method:
1. Validates the application configuration
2. Sets up scheduled jobs using the orchestrator
3. Enters an infinite loop to run pending scheduled tasks

</details>


---

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

## Module: `open_ticket_ai\src\ce\core\dependency_injection\abstract_container.py`


### <span style='color: #8E44AD;'>class</span> `AbstractContainer`

Abstract interface for dependency containers.


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `get_instance(self, provider_key: str, subclass_of: type[T]) -> T`</summary>

Retrieve an instance from the container.
The instance is retrieved based on the provider key and must be a subclass of the given type.

**Parameters:**

- **`provider_key`** () - The key identifying the provider for the instance.
- **`subclass_of`** () - The class (or type) of the instance to be retrieved. The type T must be a subclass of
`RegistryProvidableInstance`.

**Returns:** () - An instance of the type specified by `subclass_of` (or a subclass).

</details>


---

## Module: `open_ticket_ai\src\ce\core\dependency_injection\container.py`

### ⚠️ Error parsing `open_ticket_ai\src\ce\core\dependency_injection\container.py`

```
'DocstringRaises' object has no attribute 'default'
```


---

## Module: `open_ticket_ai\src\ce\core\dependency_injection\create_registry.py`



### <span style='color: #2980B9;'>def</span> `create_registry() -> Registry`

Create the default class registry.



---

## Module: `open_ticket_ai\src\ce\core\dependency_injection\registry.py`


### <span style='color: #8E44AD;'>class</span> `Registry`

Simple class registry used for dependency lookup.


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `__init__(self)`</summary>

Create an empty registry.

</details>


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `register_all(self, instance_classes: list[Type[RegistryProvidableInstance]]) -> None`</summary>

Register multiple classes at once.

</details>


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `register(self, instance_class: type[T]) -> None`</summary>

Register a single class with an optional key.

</details>


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `get(self, registry_instance_key: str, instance_class: type[T]) -> type[T]`</summary>

Retrieve a registered class and validate its type.

</details>


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `contains(self, registry_instance_key: str) -> bool`</summary>

Check whether a key is registered under a compatible type.

</details>


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `get_registry_types_descriptions(self) -> str`</summary>

Return a list of all registered types and descriptions.

</details>


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `get_all_registry_keys(self) -> list[str]`</summary>

Return a list of all registered keys.

</details>


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `get_type_from_key(self, registry_instance_key: str) -> type[RegistryProvidableInstance]`</summary>

Get the type of a registered instance by its key.

</details>


---

## Module: `open_ticket_ai\src\ce\core\mixins\registry_instance_config.py`


### <span style='color: #8E44AD;'>class</span> `RegistryInstanceConfig`

Base configuration for registry instances.


---

## Module: `open_ticket_ai\src\ce\core\mixins\registry_providable_instance.py`


### <span style='color: #8E44AD;'>class</span> `RegistryProvidableInstance`

Base class for objects that can be provided by a registry.
This class provides common functionality for registry-managed objects including
configuration storage, pretty printing of configuration, and provider registration.

**Parameters:**

- **`console`** (`Console`) - Rich console instance for output formatting.
- **`config`** (`RegistryInstanceConfig`) - Configuration object for this instance.


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `__init__(self, config: RegistryInstanceConfig, console: Console | None)`</summary>

Store the configuration and pretty print it.

</details>


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `get_provider_key(cls) -> str`</summary>

Return the provider key for the class.
This key is used to register and retrieve instances from the registry.

</details>


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `get_description() -> str`</summary>

Return a human readable description for the class.

</details>


---

## Module: `open_ticket_ai\src\ce\core\util\create_json_config_schema.py`


### <span style='color: #8E44AD;'>class</span> `RootConfig`

Wrapper model used for schema generation.


---

## Module: `open_ticket_ai\src\ce\core\util\path_util.py`

### ⚠️ Error parsing `open_ticket_ai\src\ce\core\util\path_util.py`

```
'DocstringRaises' object has no attribute 'default'
```


---

## Module: `open_ticket_ai\src\ce\core\util\pretty_print_config.py`



### <span style='color: #2980B9;'>def</span> `pretty_print_config(config: BaseModel, console: Console)`

Pretty print a pydantic model using ``rich``.
This function converts a Pydantic BaseModel to a dictionary, serializes it to YAML,
and prints it to the console using rich's syntax highlighting.

**Parameters:**

- **`config`** (`BaseModel`) - The Pydantic model configuration to display.
- **`console`** (`Console`) - The rich console instance for output rendering.



---

## Module: `open_ticket_ai\src\ce\main.py`

Open Ticket AI CLI entry point.
This module provides the command-line interface for the Open Ticket AI application.
It configures logging levels and launches the main application.


### <span style='color: #2980B9;'>def</span> `main(verbose: bool, debug: bool)`

Configure logging based on CLI options.

**Parameters:**

- **`verbose`** (`bool`) - Enable INFO-level logging when True.
- **`debug`** (`bool`) - Enable DEBUG-level logging when True.



### <span style='color: #2980B9;'>def</span> `start()`

Initialize the container and start the application.



---

## Module: `open_ticket_ai\src\ce\run\ai_models\hf_local_ai_inference_service.py`


### <span style='color: #8E44AD;'>class</span> `HFAIInferenceService`

A class representing a Hugging Face AI model.
This class is a placeholder for future implementation of Hugging Face AI model functionalities.
Currently, it does not contain any methods or properties.


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `__init__(self, config: RegistryInstanceConfig)`</summary>

Initializes the HFAIInferenceService with configuration.

**Parameters:**

- **`config`** (`RegistryInstanceConfig`) - Configuration instance for the service.

</details>


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `process(self, context: PipelineContext) -> PipelineContext`</summary>

Processes pipeline context by storing prepared data as model result.

**Parameters:**

- **`context`** (`PipelineContext`) - The pipeline context containing data to process.

**Returns:** (`PipelineContext`) - The updated pipeline context with model result stored.

</details>


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `get_description() -> str`</summary>

Provides a description of the service.

**Returns:** (`str`) - Description text for the Hugging Face AI model service.

</details>


---

## Module: `open_ticket_ai\src\ce\run\fetchers\basic_ticket_fetcher.py`


### <span style='color: #8E44AD;'>class</span> `BasicTicketFetcher`

Simple fetcher that loads ticket data using the ticket system adapter.


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `__init__(self, config: RegistryInstanceConfig, ticket_system: TicketSystemAdapter)`</summary>

Initializes the BasicTicketFetcher with configuration and ticket system adapter.

**Parameters:**

- **`config`** () - The configuration instance for the fetcher.
- **`ticket_system`** () - The adapter for interacting with the ticket system.

</details>


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `process(self, context: PipelineContext) -> PipelineContext`</summary>

Fetches ticket data and updates the pipeline context.
Retrieves the ticket using the ticket ID from the context and updates
the context's data dictionary with the ticket information.

**Parameters:**

- **`context`** () - The pipeline context containing the ticket ID.

**Returns:** (`PipelineContext`) - The updated pipeline context with ticket data.

</details>


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `get_description() -> str`</summary>

Provides a description of this pipe's functionality.

**Returns:** (`str`) - A description of the pipe.

</details>


---

## Module: `open_ticket_ai\src\ce\run\modifiers\generic_ticket_updater.py`


### <span style='color: #8E44AD;'>class</span> `GenericTicketUpdater`

Update a ticket in the ticket system using data from the context.


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `__init__(self, config: RegistryInstanceConfig, ticket_system: TicketSystemAdapter)`</summary>

Initializes the GenericTicketUpdater with configuration and ticket system adapter.

**Parameters:**

- **`config`** () - Configuration instance for the pipeline component.
- **`ticket_system`** () - Adapter for interacting with the ticket system.

</details>


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `process(self, context: PipelineContext) -> PipelineContext`</summary>

Processes the pipeline context to update the ticket if update data exists.
Retrieves update data from the context and updates the ticket in the ticket system
if update data is present. Returns the context unchanged.

**Parameters:**

- **`context`** () - The pipeline context containing data and ticket information.

**Returns:** () - The original pipeline context after processing.

</details>


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `get_description() -> str`</summary>


</details>


---

## Module: `open_ticket_ai\src\ce\run\orchestrator.py`

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

## Module: `open_ticket_ai\src\ce\run\pipeline\context.py`


### <span style='color: #8E44AD;'>class</span> `PipelineContext`

Context object passed between pipeline stages.

**Parameters:**

- **`ticket_id`** (`str`) - The ID of the ticket being processed.
- **`data`** (`dict[str, Any]`) (default: `an empty dictionary`) - A dictionary to hold arbitrary data for the pipeline stages. Defaults to an empty dictionary.


---

## Module: `open_ticket_ai\src\ce\run\pipeline\pipe.py`


### <span style='color: #8E44AD;'>class</span> `Pipe`

Interface for all pipeline components.


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `process(self, context: PipelineContext) -> PipelineContext`</summary>

Process ``context`` and return it.

</details>


---

## Module: `open_ticket_ai\src\ce\run\pipeline\pipeline.py`


### <span style='color: #8E44AD;'>class</span> `Pipeline`

Composite pipe executing a sequence of pipes.


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `__init__(self, config: PipelineConfig, pipes: List[Pipe])`</summary>

Initializes the Pipeline with configuration and component pipes.

**Parameters:**

- **`config`** () - Configuration settings for the pipeline.
- **`pipes`** () - Ordered list of Pipe instances to execute sequentially.

</details>


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `execute(self, context: PipelineContext) -> PipelineContext`</summary>

Executes all pipes in the pipeline sequentially.
Processes the context through each pipe in the defined order, passing
the output of one pipe as input to the next.

**Parameters:**

- **`context`** () - The initial pipeline context containing data to process.

**Returns:** () - The final context after processing through all pipes.

</details>


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `process(self, context: PipelineContext) -> PipelineContext`</summary>

Processes context through the entire pipeline.
This method implements the Pipe interface by delegating to execute().

**Parameters:**

- **`context`** () - The pipeline context to process.

**Returns:** () - The modified context after pipeline execution.

</details>


---

## Module: `open_ticket_ai\src\ce\run\preparers\subject_body_preparer.py`


### <span style='color: #8E44AD;'>class</span> `SubjectBodyPreparer`

Extract and concatenate the ticket subject and body.


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `__init__(self, config: RegistryInstanceConfig)`</summary>

Initializes the SubjectBodyPreparer with configuration.

**Parameters:**

- **`config`** (`RegistryInstanceConfig`) - Configuration parameters for the preparer.

</details>


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `process(self, context: PipelineContext) -> PipelineContext`</summary>

Processes ticket data to prepare subject and body content.
Extracts subject and body fields from context data, repeats the subject
as specified in configuration, and concatenates with the body. Stores
the result in context under 'prepared_data' key.

**Parameters:**

- **`context`** (`PipelineContext`) - Pipeline context containing ticket data.

**Returns:** (`PipelineContext`) - Updated context with prepared data.

</details>


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `get_description() -> str`</summary>

Provides a description of the pipe's functionality.

**Returns:** (`str`) - Description of the pipe's purpose.

</details>


---

## Module: `open_ticket_ai\src\ce\ticket_system_integration\otobo_adapter.py`


### <span style='color: #8E44AD;'>class</span> `OTOBOAdapter`

Adapter for OTOBO ticket system integration.
This class provides methods to interact with the OTOBO API.


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `get_description() -> str`</summary>

Return a description of the adapter's functionality.

**Returns:** (`str`) - A description of the OTOBO adapter.

</details>


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `__init__(self, config: SystemConfig, otobo_client: OTOBOClient)`</summary>

Initialize the OTOBO adapter with configuration and client.

**Parameters:**

- **`config`** (`SystemConfig`) - System configuration object.
- **`otobo_client`** (`OTOBOClient`) - Client for interacting with OTOBO API.

</details>


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>async def</span> `find_tickets(self, query: dict) -> list[dict]`</summary>

Return all tickets matching ``query``.

**Parameters:**

- **`query`** (`dict`) - Search parameters for tickets.

**Returns:** (`list[dict]`) - List of tickets matching the query.

</details>


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>async def</span> `find_first_ticket(self, query: dict) -> dict | None`</summary>

Return the first ticket found for ``query`` if available.

**Parameters:**

- **`query`** (`dict`) - Search parameters for tickets.

**Returns:** () - dict | None: First matching ticket dictionary or None if none found.

</details>


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>async def</span> `update_ticket(self, ticket_id: str, data: dict) -> dict`</summary>

Update ``ticket_id`` with ``data`` and return the updated record.

**Parameters:**

- **`ticket_id`** (`str`) - ID of the ticket to update.
- **`data`** (`dict`) - Update parameters for the ticket.

**Returns:** (`dict`) - Updated ticket record.

</details>


---

## Module: `open_ticket_ai\src\ce\ticket_system_integration\otobo_adapter_config.py`


### <span style='color: #8E44AD;'>class</span> `OTOBOAdapterConfig`

Configuration model for OTOBO adapter.

**Parameters:**

- **`server_address`** (`str`) - The base URL of the OTOBO server.
- **`webservice_name`** (`str`) - The name of the web service to use.
- **`search_operation_url`** (`str`) - The URL for the search operation.
- **`update_operation_url`** (`str`) - The URL for the update operation.
- **`get_operation_url`** (`str`) - The URL for the get operation.
- **`username`** (`str`) - The username for authentication.
- **`password_env_var`** (`str`) - The environment variable that contains the password.


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `__str__(self)`</summary>

Return a string representation of the configuration.

</details>


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `password(self) -> str`</summary>

Retrieves the password from the environment variable specified in the configuration.

**Returns:** (`str`) - The password for authentication.

</details>


---

## Module: `open_ticket_ai\src\ce\ticket_system_integration\otobo_adapter_test.py`



### <span style='color: #2980B9;'>def</span> `adapter_and_client()`

Fixture that provides an instance of OTOBOAdapter and a mocked OTOBOClient.

**Returns:** (`tuple`) - A tuple containing:
adapter (OTOBOAdapter): Configured OTOBOAdapter instance
client (AsyncMock): Mocked OTOBOClient instance



### <span style='color: #2980B9;'>def</span> `test_config_str_and_password(monkeypatch)`

Test OTOBOAdapterConfig string representation and password retrieval from environment.
Verifies:
    1. The __str__ method excludes the password value
    2. Password is correctly retrieved from environment variable



### <span style='color: #2980B9;'>def</span> `test_config_password_missing_env(monkeypatch)`

Test OTOBOAdapterConfig raises error when password environment variable is missing.
Verifies:
    Accessing password property raises ValueError when env var doesn't exist



### <span style='color: #2980B9;'>def</span> `test_find_tickets(adapter_and_client)`

Test find_tickets correctly processes search queries and returns results.
Verifies:
    1. Query parameters are correctly passed to OTOBO client
    2. Results are properly converted to dictionaries



### <span style='color: #2980B9;'>def</span> `test_find_first_ticket(adapter_and_client)`

Test find_first_ticket returns first match or None when no tickets found.
Verifies:
    1. Returns first ticket when matches exist
    2. Returns None when no tickets match the query



### <span style='color: #2980B9;'>def</span> `test_update_ticket(adapter_and_client)`

Test update_ticket correctly formats payload and processes response.
Verifies:
    1. Update parameters are correctly converted to OTOBO format
    2. Response data is properly returned



---

## Module: `open_ticket_ai\src\ce\ticket_system_integration\ticket_system_adapter.py`


### <span style='color: #8E44AD;'>class</span> `TicketSystemAdapter`

An abstract base class for ticket system adapters.
This class defines the
interface that all ticket system adapters must implement.


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `__init__(self, config: SystemConfig)`</summary>

Initialize the adapter with system configuration.

</details>


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>async def</span> `update_ticket(self, ticket_id: str, data: dict) -> dict | None`</summary>

Update a ticket in the system.

**Parameters:**

- **`ticket_id`** () - Ticket identifier.
- **`data`** () - Attributes to update.

**Returns:** (`Optional[dict]`) - Updated ticket information.

</details>


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>async def</span> `find_tickets(self, query: dict) -> list[dict]`</summary>

Search for tickets matching ``query``.

**Parameters:**

- **`query`** () - Search parameters for the ticket system.

**Returns:** (`list[dict]`) - Matching tickets.

</details>


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>async def</span> `find_first_ticket(self, query: dict) -> dict | None`</summary>

Return the first ticket that matches ``query`` if any.

**Parameters:**

- **`query`** () - Search parameters for the ticket system.

**Returns:** (`Optional[dict]`) - The first matching ticket or None if no ticket is found.

</details>


---

## Module: `open_ticket_ai\tests\experimental\test_anonymize_data.py`



### <span style='color: #2980B9;'>def</span> `test_remove_personal_info(text)`

Tests that the anonymize_text function removes all specified personal information.
This test is parameterized with various text examples containing personal data such as names,
addresses, email addresses, phone numbers, IBANs, and credit card details. It verifies that
after processing by anonymize_text, none of the forbidden personal information strings remain.

**Parameters:**

- **`text`** (`str`) - Input text containing personal information to be anonymized.



---

## Module: `open_ticket_ai\tests\scripts\test_doc_generation\test_plantuml_compile.py`



### <span style='color: #2980B9;'>def</span> `test_compile_plantuml_diagrams_missing_dir(tmp_path: Path)`

Tests the behavior of compile_plantuml_diagrams when given a non-existent directory.
This test verifies that the function handles missing directories gracefully by:
1. Not raising any exceptions when called with a non-existent path
2. Ensuring the directory remains non-existent after the function call

**Parameters:**

- **`tmp_path`** () - A pytest fixture providing a temporary directory path object.



---

## Module: `open_ticket_ai\tests\scripts\test_license_script.py`



### <span style='color: #2980B9;'>def</span> `setup_test_directory(tmp_path)`

Sets up a temporary directory with various files for testing.



### <span style='color: #2980B9;'>def</span> `test_find_start_of_code(lines, expected_index)`

Tests the find_start_of_code function with various line inputs.

**Parameters:**

- **`lines`** () - List of strings representing lines of a file.
- **`expected_index`** () - The expected index where the code starts.



### <span style='color: #2980B9;'>def</span> `test_update_license_in_files(setup_test_directory)`

Tests the update_license_in_files function by updating files in a test directory.
It checks that:
  - Python files get the new license notice at the top and retain their original content.
  - Already licensed files are updated without duplicating the license.
  - Non-Python files are not modified.

**Parameters:**

- **`setup_test_directory`** () - Pytest fixture that sets up a temporary test directory.



---

## Module: `open_ticket_ai\tests\src\core\config_test.py`



### <span style='color: #2980B9;'>def</span> `minimal_config_dict()`

Build the smallest valid dict for ``OpenTicketAIConfig``.
The config now follows the new pipes and filters structure with
``pipelines`` instead of ``attribute_predictors``.


### <span style='color: #8E44AD;'>class</span> `TestSchedulerConfig`

Test cases for validating the SchedulerConfig model.


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `test_valid_scheduler_config(self)`</summary>

Tests that a valid scheduler configuration is parsed correctly.

</details>


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `test_scheduler_config_invalid_interval_raises_validation_error(self, interval)`</summary>

Tests that invalid interval values raise a ValidationError.

</details>


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `test_scheduler_config_invalid_unit_raises_validation_error(self)`</summary>

Tests that an invalid time unit raises a ValidationError.

</details>

### <span style='color: #8E44AD;'>class</span> `TestOpenTicketAIConfig`

Test cases for validating the OpenTicketAIConfig model.


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `test_empty_list_for_core_components_raises_validation_error(self, list_name, minimal_config_dict)`</summary>

Tests that empty lists for required components raise ValidationError.

</details>


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `test_valid_open_ticket_ai_config_parses_correctly(self, minimal_config_dict)`</summary>

Tests that a valid configuration is parsed correctly with all components.

</details>


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `test_invalid_cross_reference_raises_value_error(self, list_name_to_alter, pipe_index, expected_error_message_part, minimal_config_dict)`</summary>

Tests that invalid component references in pipelines raise ValueError.

</details>


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `test_duplicate_ids_in_component_list_allowed_by_basemodel_but_picked_by_set_logic(self, minimal_config_dict)`</summary>

Tests duplicate component ID behavior and cross-reference resolution.

</details>

### <span style='color: #8E44AD;'>class</span> `TestLoadConfig`

Test cases for the load_config function.


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `test_load_config_missing_root_key_raises_key_error(self, tmp_path)`</summary>

Tests that missing root key 'open_ticket_ai' raises KeyError.

</details>


---

## Module: `open_ticket_ai\tests\src\core\test_di_container.py`




---

## Module: `open_ticket_ai\tests\src\core\util_test.py`


### <span style='color: #8E44AD;'>class</span> `DummyModel`

A dummy Pydantic model for testing purposes.

**Parameters:**

- **`foo`** (`int`) - An integer attribute for testing.
- **`bar`** (`str`) - A string attribute for testing.


### <span style='color: #2980B9;'>def</span> `test_find_project_root_returns_project_directory()`

Tests that find_project_root correctly identifies the project root directory.
Verifies:
    - The found directory has the expected name
    - The current test file resides within the found directory
    - The expected config file exists in the root directory



### <span style='color: #2980B9;'>def</span> `test_find_project_root_invalid_name_raises()`

Tests that find_project_root raises FileNotFoundError with invalid project name.



### <span style='color: #2980B9;'>def</span> `test_pretty_print_config_outputs_yaml()`

Tests that pretty_print_config outputs configuration as expected YAML.
Verifies:
    - Output contains exactly one element
    - Output element is a Syntax object
    - Output YAML matches the expected serialized configuration



### <span style='color: #2980B9;'>def</span> `test_root_config_schema_contains_open_ticket_ai()`

Tests that the generated JSON schema contains the expected 'open_ticket_ai' property.



### <span style='color: #2980B9;'>def</span> `test_schema_file_written(tmp_path, monkeypatch)`

Tests that the JSON schema file is correctly generated and written.

**Parameters:**

- **`tmp_path`** () - Pytest fixture for temporary directory
- **`monkeypatch`** () - Pytest fixture for modifying environment



---

## Module: `open_ticket_ai\tests\src\run\fetchers\test_fetchers.py`


### <span style='color: #8E44AD;'>class</span> `DummyFetcher`

A dummy fetcher for testing purposes.
This fetcher does not fetch any real data but simply sets a dummy flag in the context.


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `__init__(self, cfg, ticket_system)`</summary>

Initializes the DummyFetcher.

**Parameters:**

- **`cfg`** () - The configuration for the fetcher.
- **`ticket_system`** () - A mock ticket system object for testing.

</details>


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `process(self, context: PipelineContext) -> PipelineContext`</summary>

Processes the pipeline context by setting a dummy flag.

**Parameters:**

- **`context`** () - The pipeline context.

**Returns:** (`PipelineContext`) - The updated pipeline context with a dummy flag set to True.

</details>


### <span style='color: #2980B9;'>def</span> `test_dummy_fetcher_process_populates_context()`

Tests that the DummyFetcher process method populates the context with a dummy flag.



### <span style='color: #2980B9;'>def</span> `test_basic_ticket_fetcher_fetches_ticket()`

Tests that the BasicTicketFetcher fetches a ticket and populates the context.



### <span style='color: #2980B9;'>def</span> `test_basic_ticket_fetcher_description()`

Tests the description of the BasicTicketFetcher.



---

## Module: `open_ticket_ai\tests\src\run\pipeline\test_pipeline.py`




---

## Module: `open_ticket_ai\tests\src\run\test_ai_models.py`


### <span style='color: #8E44AD;'>class</span> `DummyService`

A dummy service for testing that simulates an AI inference service.
This class extends the Pipe abstract base class and implements a simple
process method that generates a dummy result based on input context.

**Parameters:**

- **`ai_inference_config`** () - Configuration for the dummy service.


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `__init__(self, cfg)`</summary>

Initializes the DummyService with given configuration.

**Parameters:**

- **`cfg`** () - Configuration object for the service.

</details>


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `process(self, context: PipelineContext) -> PipelineContext`</summary>

Processes input context by generating a dummy model result.

**Parameters:**

- **`context`** () - The pipeline context containing input data.

**Returns:** (`PipelineContext`) - Updated context with dummy model result added.

</details>


### <span style='color: #2980B9;'>def</span> `example_config()`

Fixture providing a dummy AI inference service configuration.

**Returns:** (`AIInferenceServiceConfig`) - Configuration instance for testing.



### <span style='color: #2980B9;'>def</span> `test_service_process_sets_result(example_config)`

Tests that DummyService correctly sets model_result in context.



### <span style='color: #2980B9;'>def</span> `test_hf_service_description()`

Tests that Hugging Face service description contains expected text.



### <span style='color: #2980B9;'>def</span> `test_hf_service_process_returns_context(example_config)`

Tests that Hugging Face service returns context with model result.



---

## Module: `open_ticket_ai\tests\src\run\test_modifiers.py`


### <span style='color: #8E44AD;'>class</span> `DummyModifier`

A dummy modifier class for testing purposes.
This modifier sets a flag in the pipeline context to indicate modification.

**Parameters:**

- **`modifier_config`** () - Configuration for the modifier.
- **`ticket_system`** () - The ticket system interface.


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `__init__(self, cfg, ticket_system)`</summary>

Initializes the DummyModifier instance.

**Parameters:**

- **`cfg`** () - Configuration object for the modifier.
- **`ticket_system`** () - The ticket system interface to use.

</details>


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `process(self, context: PipelineContext) -> PipelineContext`</summary>

Processes the pipeline context by setting a modification flag.

**Parameters:**

- **`context`** () - The pipeline context containing ticket data.

**Returns:** () - The modified pipeline context.

</details>


### <span style='color: #2980B9;'>def</span> `test_modifier_initialization_calls_pretty_print()`

Tests that modifier initialization calls the pretty print function.
Verifies that during initialization of a modifier, the configuration
pretty print function is called exactly once with the correct config.



### <span style='color: #2980B9;'>def</span> `test_generic_ticket_updater_calls_update()`

Tests that GenericTicketUpdater correctly calls the adapter's update method.
Verifies that when processing a context with update data, the adapter's
update_ticket method is called with the correct ticket ID and data.



---

## Module: `open_ticket_ai\tests\src\run\test_pipeline.py`


### <span style='color: #8E44AD;'>class</span> `DummyPreparer`

A dummy implementation of a data preparer for testing purposes.
This class simulates the behavior of preparing input data by applying
a simple transformation.


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `prepare(self, data)`</summary>

Transforms input data by wrapping a specific value in a string.

**Parameters:**

- **`data`** (`dict`) - Input data dictionary expected to contain a key 'v'.

**Returns:** (`str`) - A formatted string containing the value from data['v'].

</details>

### <span style='color: #8E44AD;'>class</span> `DummyAI`

A dummy implementation of an AI model for testing purposes.
This class simulates the behavior of generating responses from prompts
by returning a formatted version of the input prompt.


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `generate_response(self, prompt)`</summary>

Generates a simulated AI response based on the input prompt.

**Parameters:**

- **`prompt`** (`str`) - The input prompt for the AI model.

**Returns:** (`str`) - A formatted string containing the input prompt.

</details>

### <span style='color: #8E44AD;'>class</span> `DummyModifier`

A dummy implementation of a result modifier for testing purposes.
This class simulates modifying model results and tracks the last arguments
passed to the modify method.


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `__init__(self)`</summary>

Initializes the DummyModifier instance.
Sets up an instance variable to track the last arguments used in modify calls.

</details>


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `modify(self, ticket_id: str, model_result)`</summary>

Simulates modifying a model result and stores the input arguments.

**Parameters:**

- **`ticket_id`** (`str`) - Identifier for the ticket being processed.
- **`model_result`** () - The result from the model that would be modified.

**Returns:** (`str`) - A fixed string indicating completion.

</details>


---

## Module: `open_ticket_ai\tests\src\run\test_preparers\test_data_preparer.py`


### <span style='color: #8E44AD;'>class</span> `DummyPreparer`

A dummy implementation of a Pipe for testing preparer functionality.
This class simulates a preparer step in the pipeline by copying a value
from the context data under a specific key.

**Parameters:**

- **`preparer_config`** (`PreparerConfig`) - Configuration settings for the preparer.


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `__init__(self, cfg)`</summary>

Initializes the DummyPreparer with the given configuration.

**Parameters:**

- **`cfg`** (`PreparerConfig`) - Configuration object for the preparer.

</details>


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `process(self, context: PipelineContext) -> PipelineContext`</summary>

Processes pipeline context by copying data to 'prepared_data' field.
Copies the value from context.data['key'] to context.data['prepared_data'].

**Parameters:**

- **`context`** (`PipelineContext`) - The pipeline context containing ticket data.

**Returns:** (`PipelineContext`) - The updated context with 'prepared_data' added.

</details>


### <span style='color: #2980B9;'>def</span> `test_preparer_process_updates_context()`

Tests that DummyPreparer correctly updates context data.
Verifies:
    1. The preparer's configuration is properly printed during initialization
    2. The process method correctly copies 'key' value to 'prepared_data'



---

## Module: `open_ticket_ai\tests\src\run\test_preparers\test_subject_body_preparer.py`



### <span style='color: #2980B9;'>def</span> `test_subject_body_preparer_process_concatenates_fields()`

Tests the SubjectBodyPreparer's process method.
This test verifies that:
1. During initialization, the preparer calls pretty_print_config with its config
2. The process method correctly concatenates 'subject' and 'body' fields from context data



---

## Module: `open_ticket_ai\tests\src\test_app_main.py`


### <span style='color: #8E44AD;'>class</span> `TestAppRun`

Test suite for the App.run() method functionality.


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `test_run_validation_passes(self, monkeypatch)`</summary>

Tests that App.run() executes validation and scheduling when validation passes.
Ensures:
    - Validator is called exactly once
    - Orchestrator sets schedules exactly once
    - Console output occurs as expected

</details>


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `test_run_validation_error_logs(self, monkeypatch, caplog)`</summary>

Tests that App.run() logs validation errors appropriately.
Ensures:
    - Validation errors are logged at ERROR level
    - Orchestrator still attempts to set schedules after validation failure

</details>

### <span style='color: #8E44AD;'>class</span> `TestMainModule`

Test suite for main module functionality.


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `test_main_sets_logging_level(self, monkeypatch)`</summary>

Tests that main() correctly sets logging verbosity levels.
Verifies:
    - Logging level is set to INFO when verbose=True

</details>


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `test_start_creates_container_and_runs_app(self, monkeypatch, capsys)`</summary>

Tests the full application startup sequence.
Ensures:
    - Dependency container is initialized
    - App instance is retrieved and executed
    - Expected console output (figlet art) is present

</details>


---
