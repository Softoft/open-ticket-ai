import abc

from injector import inject

from open_ticket_ai.ce.core.config_models import FetcherConfig
from open_ticket_ai.ce.core.mixins.description_mixin import DescriptionMixin


class DataFetcher(DescriptionMixin, abc.ABC):
    @inject
    def __init__(self, config: FetcherConfig):
        self.fetcher_config = config

    @abc.abstractmethod
    def fetch_data(self, *args, **kwargs):
        """
        Abstract method to fetch data.
        Implementations should define how to fetch data.
        """
        pass
