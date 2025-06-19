import abc


class Modifier(abc.ABC):
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