import abc

from injector import inject

from open_ticket_ai.ce.core.config.config_models import PreparerConfig
from open_ticket_ai.ce.core.mixins.configurable_mixin import ConfigurableMixin
from open_ticket_ai.ce.core.mixins.description_mixin import DescriptionMixin


class DataPreparer(ConfigurableMixin, DescriptionMixin, abc.ABC):
    """
    Abstract base class for data preparers.
    """

    @inject
    def __init__(self, config: PreparerConfig, *args, **kwargs):
        """Initialize the preparer with its configuration."""
        super().__init__(config)
        self.preparer_config = config

    @abc.abstractmethod
    def prepare(self, data: dict) -> str:
        """Prepare ``data`` for processing.

        Args:
            data: Raw ticket data.

        Returns:
            str: The prepared input string.
        """
        pass
