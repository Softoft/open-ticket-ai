from injector import inject

from open_ticket_ai.src.ce.core.mixins.registry_instance_config import RegistryInstanceConfig
from open_ticket_ai.src.ce.run.pipeline.context import PipelineContext
from open_ticket_ai.src.ce.run.pipeline.pipe import Pipe
from open_ticket_ai.src.ce.ticket_system_integration.ticket_system_adapter import \
    TicketSystemAdapter
from injector import inject

from open_ticket_ai.src.ce.core.mixins.registry_instance_config import RegistryInstanceConfig
from open_ticket_ai.src.ce.run.pipeline.pipe import Pipe
from open_ticket_ai.src.ce.ticket_system_integration.ticket_system_adapter import \
    TicketSystemAdapter


class Modifier(Pipe):
    """
    Abstract base class for all modifiers.
    Modifiers are used to modify or enhance data in some way.
    """

    def process(self, context: PipelineContext) -> PipelineContext:
        pass

    @inject
    def __init__(self, config: RegistryInstanceConfig, ticket_system: TicketSystemAdapter):
        """Initialize the modifier with its configuration."""
        super().__init__(config)
        self.ticket_system = ticket_system
