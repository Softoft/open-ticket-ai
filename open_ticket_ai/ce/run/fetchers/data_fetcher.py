import abc


class DataFetcher(abc.ABC):
    @abc.abstractmethod
    def fetch_data(self, *args, **kwargs):
        """
        Abstract method to fetch data.
        Implementations should define how to fetch data.
        """
        pass