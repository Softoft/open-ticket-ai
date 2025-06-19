import abc


class DataPreparer(abc.ABC):
    """
    Abstract base class for data preparers.
    """

    @abc.abstractmethod
    def prepare(self) -> str:
        """
        Prepare the data for processing.

        :return: The input tokens
        """
        pass
