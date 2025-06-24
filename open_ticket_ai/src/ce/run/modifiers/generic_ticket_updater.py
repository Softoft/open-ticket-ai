from open_ticket_ai.src.ce.core.mixins.registry_instance_config import (
    RegistryInstanceConfig,
)
from open_ticket_ai.src.ce.run.pipeline.context import PipelineContext
from open_ticket_ai.src.ce.run.pipeline.pipe import Pipe
from open_ticket_ai.src.ce.ticket_system_integration.ticket_system_adapter import TicketSystemAdapter


class GenericTicketUpdater(Pipe):
    """Update a ticket in the ticket system using data from the context."""

    def __init__(self, config: RegistryInstanceConfig, ticket_system: TicketSystemAdapter):
        super().__init__(config)
        self.modifier_config = config
        self.ticket_system = ticket_system

    def process(self, context: PipelineContext) -> PipelineContext:
        update_data = context.data.get("update_data")
        if update_data:
            self.ticket_system.update_ticket(context.ticket_id, update_data)
        return context

    @staticmethod
    def get_description() -> str:
        return "Updates the ticket in the ticket system using data stored in the context."
