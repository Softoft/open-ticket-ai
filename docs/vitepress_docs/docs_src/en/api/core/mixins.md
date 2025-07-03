---
description: Explore the documentation for the `Providable` base class in Python,
  a core mixin from the `open_ticket_ai` project. This class serves as a foundation
  for objects managed by a registry, providing essential functionality for configuration
  storage, provider key generation (`get_provider_key`), and descriptive information.
  Learn how to create registry-providable instances with built-in configuration and
  console handling for extensible systems.
---
# Documentation for `**/ce/core/mixins/**/*.py`

## Module: `open_ticket_ai\src\ce\core\mixins\registry_providable_instance.py`


### <span style='text-info'>class</span> `Providable`

Base class for objects that can be provided by a registry.
This class provides common functionality for registry-managed objects including
configuration storage, pretty printing of configuration, and provider registration.

**Parameters:**

- **`console`** (`Console`) - Rich console instance for output formatting.
- **`config`** (`ProvidableConfig`) - Configuration object for this instance.


::: details #### <Badge type="info" text="method"/> <span class='text-warning'>def</span> `__init__(self, config: ProvidableConfig, console: Console | None)`
Initializes the instance with configuration and console.
Stores the provided configuration and initializes a Rich Console instance if not provided.
Logs the initialization event and pretty-prints the configuration.

**Parameters:**

- **`config`** () - Configuration object for this instance.
- **`console`** () - Optional Rich Console instance for output formatting. If not provided,
a new Console instance will be created.

:::


::: details #### <Badge type="info" text="method"/> <span class='text-warning'>def</span> `get_provider_key(cls) -> str`
Return the provider key for the class.
This key is used to register and retrieve instances from the registry.

**Returns:** (`str`) - The class name used as the registry key.

:::


::: details #### <Badge type="info" text="method"/> <span class='text-warning'>def</span> `get_description() -> str`
Return a human readable description for the class.
This method should be overridden by subclasses to provide specific descriptions.
The base implementation returns a default placeholder message.

**Returns:** (`str`) - Human-readable description of the class.

:::


---
