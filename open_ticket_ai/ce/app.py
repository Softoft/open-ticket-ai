import logging
import time

import schedule
from injector import inject

from open_ticket_ai.ce.core.config_models import OpenTicketAIConfig
from open_ticket_ai.ce.core.config_validator import OpenTicketAIConfigValidator
from open_ticket_ai.ce.core.container import DIContainer
from open_ticket_ai.ce.run.orchestrator import Orchestrator
from rich.console import Console
import logging

console = Console()

class App:
    @inject
    def __init__(
            self,
            config: OpenTicketAIConfig,
            validator: OpenTicketAIConfigValidator,
            orchestrator: Orchestrator
    ):
        self._logger = logging.getLogger(__name__)
        self.config = config
        self.validator = validator
        self.orchestrator = orchestrator

    def run(self):
        try:
            self.validator.validate_registry()
        except ValueError as e:
            self._logger.error(f"Configuration validation failed: {e}")
        else:
            console.print("[bold green]Configuration validation passed![/bold green]")


        self.orchestrator.set_schedules()
        while True:
            schedule.run_pending()
            time.sleep(1)