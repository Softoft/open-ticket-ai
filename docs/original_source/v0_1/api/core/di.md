# Documentation for `**/ce/core/dependency_injection/**/*.py`

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
