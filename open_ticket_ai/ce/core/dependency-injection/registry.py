# --- registry + decorator ---------------------------------------------
from typing import Type

from open_ticket_ai.ce.core.mixins.description_mixin import DescriptionMixin


class Registry:
    """Simple class registry used for dependency lookup."""

    def __init__(self):
        """Create an empty registry."""
        super().__init__()
        self._registry: dict[str, Type[DescriptionMixin]] = {}

    def register_all(self, instance_classes: list[Type[DescriptionMixin]]) -> None:
        """Register multiple classes at once."""
        for instance_class in instance_classes:
            self.register(instance_class)

    def register[T](self, instance_class: type[T], registry_instance_key: str | None = None) -> None:
        """Register a single class with an optional key."""
        if registry_instance_key is None:
            registry_instance_key = instance_class.__name__
        self._registry[registry_instance_key] = instance_class

    def get[T](self, registry_instance_key: str, instance_class: type[T]) -> type[T]:
        """Retrieve a registered class and validate its type."""
        if registry_instance_key not in self._registry:
            raise KeyError(f"Registry instance key '{registry_instance_key}' not found.")
        registered_class = self._registry[registry_instance_key]
        if not issubclass(registered_class, instance_class):
            raise TypeError(f"Registered class {registered_class} is not a subclass of {instance_class}.")
        return registered_class

    def contains(self, registry_instance_key: str, subclass_of: type) -> bool:
        """Check whether a key is registered under a compatible type."""
        if registry_instance_key not in self._registry:
            return False
        registered_class = self._registry[registry_instance_key]
        if not issubclass(registered_class, subclass_of):
            return False
        return True

    def get_registry_types_descriptions(self, subclass_of: type[DescriptionMixin] = DescriptionMixin) -> str:
        """Return a list of all registered types and descriptions."""
        return "\n".join([f"{key}: {value.get_description()}" for key, value in self._registry.items()
                          if issubclass(value, subclass_of)]) or "No registered types found."
