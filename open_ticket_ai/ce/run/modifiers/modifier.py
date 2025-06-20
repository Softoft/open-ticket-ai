import abc

from open_ticket_ai.ce.core.mixins.description_mixin import DescriptionMixin


class Modifier(DescriptionMixin, abc.ABC):
    """
    Abstract base class for all modifiers.
    Modifiers are used to modify or enhance data in some way.
    """

    @abc.abstractmethod
    def modify(self, ticket_id: str, model_result: str | int):
        """
        Abstract method to modify data.
        Implementations should define how to modify the data.
        """
        pass