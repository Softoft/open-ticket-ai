import abc


class AttributePredictor(abc.ABC):
    """
    Base class for attribute predictors.
    """

    @abc.abstractmethod
    def predict_attribute(self) -> str | int:
        pass
