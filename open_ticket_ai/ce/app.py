from injector import inject

from open_ticket_ai.ce.core.config_models import OpenTicketAIConfig
from open_ticket_ai.ce.core.config_validator import OpenTicketAIConfigValidator
from open_ticket_ai.ce.core.container import DIContainer


class App:
    @inject
    def __init__(
            self,
            config: OpenTicketAIConfig,
            validator: OpenTicketAIConfigValidator,
    ):
        self.config = config
        self.validator = validator

    def run(self):
        self.validator.validate_registry()

if __name__ == "__main__":
    container = DIContainer()
    app: App = container.get(App)
    app.run()