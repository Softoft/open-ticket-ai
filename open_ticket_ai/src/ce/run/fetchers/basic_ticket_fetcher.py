from open_ticket_ai.src.ce.core.mixins.registry_instance_config import (
    RegistryInstanceConfig,
)
from open_ticket_ai.src.ce.run.pipeline.pipe import Pipe
from open_ticket_ai.src.ce.run.pipeline.context import PipelineContext
from open_ticket_ai.src.ce.ticket_system_integration.ticket_system_adapter import TicketSystemAdapter


class BasicTicketFetcher(Pipe):
    """Simple fetcher that loads ticket data using the ticket system adapter."""

    def __init__(self, config: RegistryInstanceConfig, ticket_system: TicketSystemAdapter):
        super().__init__(config)
        self.fetcher_config = config
        self.ticket_system = ticket_system

    def process(self, context: PipelineContext) -> PipelineContext:
        ticket = self.ticket_system.find_first_ticket({"TicketID": context.ticket_id})
        if ticket:
            context.data.update(ticket)
        return context

    @staticmethod
    def get_description() -> str:
        return (
            "Basic ticket fetcher that retrieves ticket data from a source. "
            "It is a placeholder for a more complex implementation."
        )
