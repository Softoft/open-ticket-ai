import abc

from injector import inject

from open_ticket_ai.ce.core.config_models import ModifierConfig
from open_ticket_ai.ce.core.mixins.description_mixin import DescriptionMixin


class Modifier(DescriptionMixin, abc.ABC):
    """
    Abstract base class for all modifiers.
    Modifiers are used to modify or enhance data in some way.
    """
    @inject
    def __init__(self, config: ModifierConfig):
        """
        Initializes the Modifier with a configuration.

        :param config: Configuration for the modifier.
        """
        self.modifier_config = config

    @abc.abstractmethod
    def modify(self, ticket_id: str, model_result: str | int):
        """
        Abstract method to modify data.
        Implementations should define how to modify the data.
        """
        pass