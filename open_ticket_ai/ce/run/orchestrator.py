from open_ticket_ai.ce.core.abstract_container import AbstractContainer
from open_ticket_ai.ce.core.config_models import OpenTicketAIConfig


class Orchestrator:
    def __init__(self, config: OpenTicketAIConfig, container: AbstractContainer):
        self.config = config
        self.attribute_predictors = []
        for predictor in config.attribute_predictors:
            self.attribute_predictors.append(container.get_predictor(predictor.id))

    def set_schedules(self):
        print("Running orchestrator with config:", self.config)
        for predictor in self.attribute_predictors:
            predictor.set_schedule()
            print(f"Scheduled {predictor.get_description()}")
