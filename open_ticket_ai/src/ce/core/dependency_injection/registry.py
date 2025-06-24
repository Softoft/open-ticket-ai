# --- registry + decorator ---------------------------------------------
from typing import Type

from open_ticket_ai.src.ce.core.mixins.registry_providable_instance import \
    RegistryProvidableInstance


class Registry:
    """Simple class registry used for dependency lookup."""

    def __init__(self):
        """Create an empty registry."""
        super().__init__()
        self._registry: list[type[RegistryProvidableInstance]] = []

    def register_all(self, instance_classes: list[Type[RegistryProvidableInstance]]) -> None:
        """Register multiple classes at once."""
        for instance_class in instance_classes:
            self.register(instance_class)

    def register[T: RegistryProvidableInstance](self, instance_class: type[T]) -> None:
        """Register a single class with an optional key."""
        self._registry.append(instance_class)

    def get[T: RegistryProvidableInstance](self,
                                           registry_instance_key: str,
                                           instance_class: type[T]
                                           ) -> type[T]:
        """Retrieve a registered class and validate its type."""
        if registry_instance_key not in self._registry:
            raise KeyError(f"Registry instance key '{registry_instance_key}' not found.")
        registered_class = self._registry[registry_instance_key]
        if not issubclass(registered_class, instance_class):
            raise TypeError(
                f"Registered class {registered_class} is not a subclass of {instance_class}.")
        return registered_class

    def contains(self, registry_instance_key: str) -> bool:
        """Check whether a key is registered under a compatible type."""
        return registry_instance_key in self.get_all_registry_keys()

    def get_registry_types_descriptions(self) -> str:
        """Return a list of all registered types and descriptions."""
        return ("\n".join(
            [f"{registry_instance.get_provider_key()}: {registry_instance.get_description()}" for
             registry_instance in self._registry]
        ) or "No registered types found.")

    def get_all_registry_keys(self) -> list[str]:
        """Return a list of all registered keys."""
        return [instance.get_provider_key() for instance in self._registry]

    def get_type_from_key(self, registry_instance_key: str) -> type[RegistryProvidableInstance]:
        """Get the type of a registered instance by its key."""
        for instance in self._registry:
            if instance.get_provider_key() == registry_instance_key:
                return instance
        raise KeyError(f"Registry instance key '{registry_instance_key}' not found.")
