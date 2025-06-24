from open_ticket_ai.src.ce.core.mixins.registry_instance_config import RegistryInstanceConfig
from open_ticket_ai.src.ce.run.pipeline.context import PipelineContext
from open_ticket_ai.src.ce.run.pipeline.pipe import Pipe
from open_ticket_ai.src.ce.ticket_system_integration.ticket_system_adapter import \
    TicketSystemAdapter


class DataFetcher(Pipe):
    """Base class for all data fetchers."""

    def __init__(self, config: RegistryInstanceConfig, ticket_system: TicketSystemAdapter):
        """
        Initialize the data fetcher with a configuration.

        :param config: Configuration for the data fetcher.
        """
        super().__init__(config)
        self.config = config
        self.ticket_system = ticket_system

    def process(self, context: PipelineContext) -> PipelineContext:
        pass
