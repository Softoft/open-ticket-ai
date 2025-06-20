import abc

from open_ticket_ai.ce.core.mixins.description_mixin import DescriptionMixin


class DataPreparer(DescriptionMixin, abc.ABC):
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
