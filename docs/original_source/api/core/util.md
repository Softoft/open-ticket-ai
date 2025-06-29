---
description: Explore the documentation for OpenTicketAI's core configuration utilities.
  Learn how to generate a `config.schema.json` from Pydantic models for validation
  and editor autocompletion, and how to pretty-print configurations as syntax-highlighted
  YAML for enhanced readability.
---
# Documentation for `**/ce/core/util/**/*.py`

## Module: `open_ticket_ai\src\ce\core\util\create_json_config_schema.py`

Module for generating the JSON schema of the OpenTicketAI configuration.
This module defines the `RootConfig` model, which is a wrapper around the main configuration
model `OpenTicketAIConfig`. The purpose of this wrapper is to facilitate the generation of
a JSON schema that describes the entire configuration structure.

When this module is run as a script, it will:
  1. Generate the JSON schema for the `RootConfig` model.
  2. Write the schema to a file named `config.schema.json` in the project's root directory.

The generated schema file can be used for validating configuration files or for providing
configuration autocompletion and documentation in editors.

### <span style='text-info'>class</span> `RootConfig`

Wrapper model used for schema generation.
This class serves as a container for the main configuration model of the OpenTicketAI system.
It is designed to be used for generating JSON schema representations of the configuration.

**Parameters:**

- **`open_ticket_ai`** (`OpenTicketAIConfig`) - The main configuration object containing all
settings and parameters for the OpenTicketAI system.


---

## Module: `open_ticket_ai\src\ce\core\util\path_util.py`



---

## Module: `open_ticket_ai\src\ce\core\util\pretty_print_config.py`

Module for pretty printing configuration objects.
This module provides functionality to display Pydantic configuration models in a
nicely formatted and syntax highlighted way using the `rich` library. It converts
Pydantic models to YAML format and applies syntax highlighting for improved readability.

Features:
- Converts Pydantic `BaseModel` instances to dictionaries
- Serializes configuration data to YAML format
- Applies YAML syntax highlighting using `rich`
- Prints highlighted output to console


### <span class='text-warning'>def</span> `pretty_print_config(config: BaseModel, console: Console)`

Pretty print a pydantic model using `rich`.
This function converts a Pydantic `BaseModel` to a dictionary, serializes it to YAML,
and prints it to the console using `rich`'s syntax highlighting. The output is formatted
with YAML syntax highlighting for improved readability.

The process involves:
    1. Converting the Pydantic model to a dictionary using `model_dump()`
    2. Serializing the dictionary to a YAML string
    3. Creating a rich `Syntax` object with YAML highlighting
    4. Printing the highlighted YAML to the console

Note that this function bypasses standard logging and outputs directly to the console
using `rich`'s printing capabilities for optimal formatting.

**Parameters:**

- **`config`** (``BaseModel``) - The Pydantic model configuration to display.
- **`console`** (``Console``) - The rich console instance for output rendering.



---
