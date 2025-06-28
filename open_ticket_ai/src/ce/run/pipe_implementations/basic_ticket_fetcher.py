from open_ticket_ai.src.ce.core.mixins.registry_instance_config import (
    RegistryInstanceConfig,
)
from open_ticket_ai.src.ce.run.pipeline.pipe import Pipe
from open_ticket_ai.src.ce.run.pipeline.context import PipelineContext
from open_ticket_ai.src.ce.ticket_system_integration.ticket_system_adapter import TicketSystemAdapter


class BasicTicketFetcher(Pipe):
    """Simple fetcher that loads ticket data using the ticket system adapter.

    This pipe retrieves ticket information from an external ticket system using
    the provided adapter. It serves as a placeholder for more complex fetching
    implementations.

    Attributes:
        fetcher_config (`RegistryInstanceConfig`): Configuration instance for the fetcher.
        ticket_system (`TicketSystemAdapter`): Adapter for interacting with the ticket system.
    """

    def __init__(self, config: RegistryInstanceConfig, ticket_system: TicketSystemAdapter):
        """Initializes the BasicTicketFetcher with configuration and ticket system adapter.

        Args:
            config (`RegistryInstanceConfig`): The configuration instance for the fetcher.
            ticket_system (`TicketSystemAdapter`): The adapter for interacting with the ticket system.
        """
        super().__init__(config)
        self.fetcher_config = config
        self.ticket_system = ticket_system

    def process(self, context: PipelineContext) -> PipelineContext:
        """Fetches ticket data and updates the pipeline context.

        Retrieves the ticket using the ticket ID from the context. If found, updates
        the context's data dictionary with the ticket information. If no ticket is found,
        the context remains unchanged.

        Args:
            context (`PipelineContext`): The pipeline context containing the `ticket_id`.

        Returns:
            `PipelineContext`: The context object. If a ticket was found, its `data` dictionary
                contains the ticket information. Otherwise, returns the original context.
        """
        ticket = self.ticket_system.find_first_ticket({"TicketID": context.ticket_id})
        if ticket:
            context.data.update(ticket)
        return context

    @staticmethod
    def get_description() -> str:
        """Provides a static description of this pipe's functionality.

        Returns:
            str: A static description of the pipe's purpose and behavior.
        """
        return (
            "Basic ticket fetcher that retrieves ticket data from a source. "
            "It is a placeholder for a more complex implementation."
        )