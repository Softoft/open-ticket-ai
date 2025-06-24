import abc

from injector import inject

from open_ticket_ai.src.ce.core.config.config_models import FetcherConfig
from open_ticket_ai.src.ce.core.mixins.configurable_mixin import ConfigurableMixin
from open_ticket_ai.src.ce.core.mixins.description_mixin import DescriptionMixin


class DataFetcher(ConfigurableMixin, DescriptionMixin, abc.ABC):
    """Base class for all data fetchers."""
    @inject
    def __init__(self, config: FetcherConfig):
        """Store fetcher configuration."""

        super().__init__(config)
        self.fetcher_config = config

    @abc.abstractmethod
    def fetch_data(self, *args, **kwargs) -> dict:
        """
        Abstract method to fetch data.
        Implementations should define how to fetch data.
        """
        pass
