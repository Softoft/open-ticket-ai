import abc

from open_ticket_ai.ce.core.mixins.description_mixin import DescriptionMixin


class BaseAIModel(DescriptionMixin, abc.ABC):
    """
    Base class for AI models.
    This class should be inherited by all AI model implementations.
    """

    def __init__(self, model_name: str):
        self.model_name = model_name

    def generate_response(self, prompt: str) -> str:
        """
        Generate a response based on the provided prompt.
        This method should be overridden by subclasses.
        """
        raise NotImplementedError("Subclasses must implement this method.")