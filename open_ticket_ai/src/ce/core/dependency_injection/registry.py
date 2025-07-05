# FILE_PATH: open_ticket_ai\src\ce\core\dependency_injection\registry.py
# --- registry + decorator ---------------------------------------------
from typing import Type

from open_ticket_ai.src.ce.core.mixins.registry_providable_instance import (
    Providable,
)


class Registry:
    """
    A registry system for managing and retrieving classes that provide specific functionality.

    This registry allows classes to be registered and later retrieved by their unique keys.
    It enforces type checking during retrieval to ensure compatibility with expected interfaces.

    Attributes:
        _registry (list[type[Providable]]): Internal list storing registered classes.
    """

    def __init__(self):
        """Initializes an empty registry with no registered classes."""
        super().__init__()
        self._registry: list[type[Providable]] = []

    def register_all(self, instance_classes: list[Type[Providable]]) -> None:
        """
        Registers multiple classes in the registry simultaneously.

        Args:
            instance_classes (list[Type[Providable]]):
                List of classes to register. Each class must implement the `Providable` interface.
        """
        for instance_class in instance_classes:
            self.register(instance_class)

    def register[T: Providable](self, instance_class: type[T]) -> None:
        """
        Registers a single class in the registry.

        The class must implement the `Providable` interface which requires:
        - A `get_provider_key()` method returning a unique string identifier.
        - A `get_description()` method returning a descriptive string.

        Args:
            instance_class (type[T]):
                The class to register. Must be a subclass of `Providable`.
        """
        self._registry.append(instance_class)

    def get[T: Providable](
        self,
        registry_instance_key: str,
        instance_class: type[T]
    ) -> type[T]:
        """
        Retrieves a registered class by its key and validates its type.

        Args:
            registry_instance_key (str):
                The unique key identifying the class to retrieve.
            instance_class (type[T]):
                The expected class/interface type for validation.

        Returns:
            type[T]: The registered class matching the key.

        Raises:
            KeyError: If no class is registered under the specified key.
            TypeError: If the registered class is not a subclass of the expected type.
        """
        if registry_instance_key not in self._registry:
            raise KeyError(f"Registry instance key '{registry_instance_key}' not found.")
        registered_class = self._registry[registry_instance_key]
        if not issubclass(registered_class, instance_class):
            raise TypeError(
                f"Registered class {registered_class} is not a subclass of {instance_class}.",
            )
        return registered_class

    def contains(self, registry_instance_key: str) -> bool:
        """
        Checks if a key exists in the registry.

        Args:
            registry_instance_key (str): The key to check.

        Returns:
            bool: True if the key exists, False otherwise.
        """
        return registry_instance_key in self.get_all_registry_keys()

    def get_registry_types_descriptions(self) -> str:
        """
        Generates a formatted string listing all registered classes and their descriptions.

        The output format is:
        `key: description`
        One entry per line.

        Returns:
            str: Formatted string of all registered keys and descriptions,
                  or "No registered types found." if the registry is empty.
        """
        return ("\n".join(
            [f"{registry_instance.get_provider_key()}: {registry_instance.get_description()}" for
             registry_instance in self._registry],
        ) or "No registered types found.")

    def get_all_registry_keys(self) -> list[str]:
        """
        Retrieves all registered keys in the registry.

        Returns:
            list[str]: List of all registered keys.
        """
        return [instance.get_provider_key() for instance in self._registry]

    def get_type_from_key(self, registry_instance_key: str) -> type[Providable]:
        """
        Retrieves the class type associated with a registration key.

        Args:
            registry_instance_key (str): The key to look up.

        Returns:
            type[Providable]: The class registered under the key.

        Raises:
            KeyError: If the key is not found in the registry.
        """
        for instance in self._registry:
            if instance.get_provider_key() == registry_instance_key:
                return instance
        raise KeyError(f"Registry instance key '{registry_instance_key}' not found.")