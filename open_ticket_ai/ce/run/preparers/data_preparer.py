import abc

from injector import inject

from open_ticket_ai.ce.core.config_models import PreparerConfig
from open_ticket_ai.ce.core.mixins.description_mixin import DescriptionMixin


class DataPreparer(DescriptionMixin, abc.ABC):
    """
    Abstract base class for data preparers.
    """
    @inject
    def __init__(self, config: PreparerConfig):
        """
        Initializes the DataPreparer with a configuration.

        :param config: Configuration for the data preparer.
        """
        self.preparer_config = config

    @abc.abstractmethod
    def prepare(self) -> str:
        """
        Prepare the data for processing.

        :return: The input tokens
        """
        pass
