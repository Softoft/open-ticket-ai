import abc

from open_ticket_ai.ce.core.mixins.description_mixin import DescriptionMixin


class DataFetcher(DescriptionMixin, abc.ABC):
    @abc.abstractmethod
    def fetch_data(self, *args, **kwargs):
        """
        Abstract method to fetch data.
        Implementations should define how to fetch data.
        """
        pass