import abc

from injector import inject

from open_ticket_ai.ce.core.config_models import PreparerConfig
from open_ticket_ai.ce.core.mixins.configurable_mixin import ConfigurableMixin
from open_ticket_ai.ce.core.mixins.description_mixin import DescriptionMixin


class DataPreparer(ConfigurableMixin, DescriptionMixin, abc.ABC):
    """
    Abstract base class for data preparers.
    """
    @inject
    def __init__(self, config: PreparerConfig,  *args, **kwargs):
        """
        Initializes the DataPreparer with a configuration.

        :param config: Configuration for the data preparer.
        """
        super().__init__(config)
        self.preparer_config = config

    @abc.abstractmethod
    def prepare(self) -> str:
        """
        Prepare the data for processing.

        :return: The input tokens
        """
        pass
