# FILE_PATH: open_ticket_ai\src\ce\run\pipe_implementations\generic_ticket_updater.py
from open_ticket_ai.src.ce.core.config.config_models import ProvidableConfig

from open_ticket_ai.src.ce.run.pipe_implementations.empty_data_model import EmptyDataModel
from open_ticket_ai.src.ce.run.pipeline.context import PipelineContext
from open_ticket_ai.src.ce.run.pipeline.pipe import Pipe
from open_ticket_ai.src.ce.ticket_system_integration.ticket_system_adapter import (
    TicketSystemAdapter,
)
from open_ticket_ai.src.ce.ticket_system_integration.unified_models import UnifiedTicket


class GenericTicketUpdater(Pipe[UnifiedTicket, EmptyDataModel]):
    """Update a ticket in the ticket system using data from the context.

    This pipe component is responsible for updating tickets in an external ticket tracking
    system (like Jira, ServiceNow, etc.) using data generated during the pipeline execution.
    It checks the pipeline context for update instructions and delegates the actual update
    operation to the configured ticket system adapter.

    Attributes:
        modifier_config: Configuration settings for the ticket updater.
        ticket_system: Adapter instance for interacting with the external ticket system.
    """

    def __init__(self, config: ProvidableConfig, ticket_system: TicketSystemAdapter):
        """Initializes the `GenericTicketUpdater` with configuration and ticket system adapter.

        Args:
            config: Configuration instance containing settings for the pipeline component.
            ticket_system: Adapter object that handles communication with the external ticket system.
        """
        super().__init__(config)
        self.modifier_config = config
        self.ticket_system = ticket_system

    def process(self, context: PipelineContext[UnifiedTicket]) -> PipelineContext[EmptyDataModel]:
        """Processes the pipeline context to update the ticket if update data exists.

        Retrieves update data from `context.data` (of type `UnifiedTicket`) and updates the ticket
        in the ticket system if update data is present (truthy). Returns the context unchanged.

        Args:
            context (PipelineContext[UnifiedTicket]): The pipeline context containing data and
                ticket information.

        Returns:
            PipelineContext[EmptyDataModel]: The original pipeline context after processing
                (unchanged).
        """
        update_data: UnifiedTicket = context.data
        if update_data:
            self.ticket_system.update_ticket(context.ticket_id, update_data)
        return context

    @staticmethod
    def get_description() -> str:
        """Provides a description of the pipe's purpose.

        Returns:
            str: A string describing the pipe's functionality.
        """
        return "Updates the ticket in the ticket system using data stored in the context."