import abc

from open_ticket_ai.ce.core.mixins.description_mixin import DescriptionMixin


class AttributePredictor(DescriptionMixin, abc.ABC):
    """
    Base class for attribute predictors.
    """

    @abc.abstractmethod
    def predict_attribute(self) -> str | int:
        pass
