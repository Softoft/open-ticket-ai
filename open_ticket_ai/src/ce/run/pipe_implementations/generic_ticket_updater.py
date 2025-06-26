from open_ticket_ai.src.ce.core.mixins.registry_instance_config import (
    RegistryInstanceConfig,
)
from open_ticket_ai.src.ce.run.pipeline.context import PipelineContext
from open_ticket_ai.src.ce.run.pipeline.pipe import Pipe
from open_ticket_ai.src.ce.ticket_system_integration.ticket_system_adapter import TicketSystemAdapter


class GenericTicketUpdater(Pipe):
    """Update a ticket in the ticket system using data from the context."""

    def __init__(self, config: RegistryInstanceConfig, ticket_system: TicketSystemAdapter):
        """Initializes the GenericTicketUpdater with configuration and ticket system adapter.

        Args:
            config: Configuration instance for the pipeline component.
            ticket_system: Adapter for interacting with the ticket system.
        """
        super().__init__(config)
        self.modifier_config = config
        self.ticket_system = ticket_system

    def process(self, context: PipelineContext) -> PipelineContext:
        """Processes the pipeline context to update the ticket if update data exists.

        Retrieves update data from the context and updates the ticket in the ticket system
        if update data is present. Returns the context unchanged.

        Args:
            context: The pipeline context containing data and ticket information.

        Returns:
            The original pipeline context after processing.
        """
        update_data = context.data.get("update_data")
        if update_data:
            self.ticket_system.update_ticket(context.ticket_id, update_data)
        return context

    @staticmethod
    def get_description() -> str:
        """Provides a description of the pipe's purpose.

        Returns:
            A string describing the pipe's functionality.
        """
        return "Updates the ticket in the ticket system using data stored in the context."