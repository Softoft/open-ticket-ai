# Documentation for `**/ce/core/util/**/*.py`

## Module: `open_ticket_ai\src\ce\core\util\create_json_config_schema.py`


### <span style='color: #8E44AD;'>class</span> `RootConfig`

Wrapper model used for schema generation.


---

## Module: `open_ticket_ai\src\ce\core\util\path_util.py`



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
