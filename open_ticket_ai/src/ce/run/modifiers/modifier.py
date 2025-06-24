import abc

from injector import inject

from open_ticket_ai.src.ce.core.config.config_models import ModifierConfig
from open_ticket_ai.src.ce.core.mixins.configurable_mixin import ConfigurableMixin
from open_ticket_ai.src.ce.core.mixins.description_mixin import DescriptionMixin


class Modifier(ConfigurableMixin, DescriptionMixin, abc.ABC):
    """
    Abstract base class for all modifiers.
    Modifiers are used to modify or enhance data in some way.
    """
    @inject
    def __init__(self, config: ModifierConfig,  *args, **kwargs):
        """Initialize the modifier with its configuration."""
        super().__init__(config)
        self.modifier_config = config

    @abc.abstractmethod
    def modify(self, original_data: dict, model_result: str | int):
        """Modify ``original_data`` based on ``model_result``."""

        pass
