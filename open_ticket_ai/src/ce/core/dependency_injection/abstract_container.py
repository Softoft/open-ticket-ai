import abc

from open_ticket_ai.src.ce.core.mixins.registry_providable_instance import \
    RegistryProvidableInstance


class AbstractContainer(abc.ABC):
    """Abstract interface for dependency containers."""

    @abc.abstractmethod
    def get_instance[T: RegistryProvidableInstance](self, provider_key: str,
                                                    subclass_of: type[T]) -> T:
        """Retrieve an instance from the container.

        The instance is retrieved based on the provider key and must be a subclass of the given type.

        Args:
            provider_key: The key identifying the provider for the instance.
            subclass_of: The class (or type) of the instance to be retrieved. The type T must be a subclass of
                `RegistryProvidableInstance`.

        Returns:
            An instance of the type specified by `subclass_of` (or a subclass).
        """
        pass
