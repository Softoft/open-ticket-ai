import abc

from open_ticket_ai.src.ce.core.mixins.registry_providable_instance import \
    RegistryProvidableInstance


class AbstractContainer(abc.ABC):
    """Abstract interface for dependency containers."""

    @abc.abstractmethod
    def get_instance[T: RegistryProvidableInstance](self, provider_key: str,
                                                    subclass_of: type[T]) -> T:
        pass
