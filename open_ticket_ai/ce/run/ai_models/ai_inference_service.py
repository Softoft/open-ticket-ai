import abc
import logging

from injector import inject

from open_ticket_ai.ce.core.config.config_models import AIInferenceServiceConfig
from open_ticket_ai.ce.core.mixins.configurable_mixin import ConfigurableMixin
from open_ticket_ai.ce.core.mixins.description_mixin import DescriptionMixin


class AIInferenceService(ConfigurableMixin, DescriptionMixin, abc.ABC):
    """
    Base class for AI ai_inference_service.
    This class should be inherited by all AI model implementations.
    """

    @inject
    def __init__(self, config: AIInferenceServiceConfig, *args, **kwargs):
        """Initialize the inference service with its configuration."""

        super().__init__(config)
        self._logger = logging.getLogger(__name__)
        self.ai_inference_config = config
        self._logger.info(f"Initialized AIInferenceService with config: {self.ai_inference_config.model_dump()}")
    @abc.abstractmethod
    def generate_response(self, prompt: str) -> str:
        """Generate a model response for the given prompt."""
        pass
