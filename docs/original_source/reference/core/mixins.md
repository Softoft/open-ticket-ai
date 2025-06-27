# Documentation for `**/ce/core/mixins/**/*.py`

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
