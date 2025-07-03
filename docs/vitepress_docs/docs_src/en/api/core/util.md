---
description: Official documentation for OpenTicketAI's core utility modules. Learn
  how to generate a `config.schema.json` for configuration validation and autocompletion,
  and discover other Python utilities for managing project settings.
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

- **``open_ticket_ai``** (``OpenTicketAIConfig``) - The main configuration object containing all
settings and parameters for the OpenTicketAI system.


---

## Module: `open_ticket_ai\src\ce\core\util\path_util.py`



---

## Module: `open_ticket_ai\src\ce\core\util\pretty_print_config.py`



---
