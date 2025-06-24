import logging

from open_ticket_ai.src.ce.core import AbstractContainer
from open_ticket_ai.src.ce.core.config.config_models import OpenTicketAIConfig
from open_ticket_ai.src.ce.core.mixins.configurable_mixin import ConfigurableMixin



class Orchestrator(ConfigurableMixin):
    """Coordinate attribute prediction scheduling."""

    def __init__(self, config: OpenTicketAIConfig, container: AbstractContainer):
        """Create the orchestrator and prepare predictors."""

        super().__init__(config)
        self.config = config
        self.attribute_predictors = []
        self._logger = logging.getLogger(__name__)
        for predictor in config.attribute_predictors:
            self.attribute_predictors.append(container.get_predictor(predictor.id))

    def set_schedules(self):
        """Register schedules for all configured predictors."""

        for predictor in self.attribute_predictors:
            predictor.set_schedule()
            print(f"Scheduled {predictor.get_description()}")
