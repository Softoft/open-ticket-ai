import abc

from open_ticket_ai.ce.core.mixins.description_mixin import DescriptionMixin


class AIInferenceService(DescriptionMixin, abc.ABC):
    """
    Base class for AI ai_inference_service.
    This class should be inherited by all AI model implementations.
    """

    def __init__(self):
        pass

    def generate_response(self, prompt: str) -> str:
        """
        Generate a response based on the provided prompt.
        This method should be overridden by subclasses.
        """
        raise NotImplementedError("Subclasses must implement this method.")