import abc

import schedule

from open_ticket_ai.src.ce.core.config.config_models import PipelineConfig
from open_ticket_ai.src.ce.core.mixins.configurable_mixin import ConfigurableMixin
from open_ticket_ai.src.ce.core.mixins.description_mixin import DescriptionMixin
from open_ticket_ai.src.ce.run.ai_models.ai_inference_service import AIInferenceService
from open_ticket_ai.src.ce.run.fetchers.data_fetcher import DataFetcher
from open_ticket_ai.src.ce.run.modifiers.modifier import Modifier
from open_ticket_ai.src.ce.run.preparers.data_preparer import DataPreparer


class AttributePredictor(ConfigurableMixin, DescriptionMixin, abc.ABC):
    """
    Base class for attribute predictors.
    """

    def __init__(self, config: AttributePredictorConfig, fetcher: DataFetcher, preparer: DataPreparer,
                 ai_inference_service: AIInferenceService, modifier: Modifier, *args, **kwargs):
        """Initialize the predictor with its dependencies."""

        super().__init__(config)
        self.attribute_predictor_config = config
        self.fetcher = fetcher
        self.preparer = preparer
        self.ai_inference_service = ai_inference_service
        self.modifier = modifier

    def set_schedule(self):
        """Register a scheduled job for ``run_attribute_prediction``."""
        schedule_config = self.attribute_predictor_config.schedule
        getattr(schedule.every(schedule_config.interval), schedule_config.unit).do(
            lambda: self.run_attribute_prediction()
        )

    @abc.abstractmethod
    def run_attribute_prediction(self):
        """
        Abstract method to run attribute prediction.
        This method should be implemented by subclasses.
        """
        pass
