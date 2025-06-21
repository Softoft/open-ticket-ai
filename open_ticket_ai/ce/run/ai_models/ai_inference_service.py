import abc

from injector import inject

from open_ticket_ai.ce.core.config_models import AIInferenceServiceConfig
from open_ticket_ai.ce.core.mixins.description_mixin import DescriptionMixin


class AIInferenceService(DescriptionMixin, abc.ABC):
    """
    Base class for AI ai_inference_service.
    This class should be inherited by all AI model implementations.
    """

    @inject
    def __init__(self, config: AIInferenceServiceConfig):
        self.ai_inference_config = config

    @abc.abstractmethod
    def generate_response(self, prompt: str) -> str:
        pass
