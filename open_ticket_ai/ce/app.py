import time

import schedule
from injector import inject

from open_ticket_ai.ce.core.config_models import OpenTicketAIConfig
from open_ticket_ai.ce.core.config_validator import OpenTicketAIConfigValidator
from open_ticket_ai.ce.core.container import DIContainer
from open_ticket_ai.ce.run.orchestrator import Orchestrator


class App:
    @inject
    def __init__(
            self,
            config: OpenTicketAIConfig,
            validator: OpenTicketAIConfigValidator,
            orchestrator: Orchestrator
    ):
        self.config = config
        self.validator = validator
        self.orchestrator = orchestrator

    def run(self):
        self.validator.validate_registry()

        self.orchestrator.set_schedules()
        while True:
            schedule.run_pending()
            time.sleep(1)


if __name__ == "__main__":
    container = DIContainer()
    app: App = container.get(App)
    app.run()
