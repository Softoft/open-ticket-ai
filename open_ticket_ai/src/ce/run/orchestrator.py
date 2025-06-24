"""Top level orchestration utilities."""
from __future__ import annotations

import logging

from open_ticket_ai.src.ce.core import AbstractContainer
from open_ticket_ai.src.ce.core.config.config_models import OpenTicketAIConfig
from open_ticket_ai.src.ce.core.mixins.configurable_mixin import ConfigurableMixin
from open_ticket_ai.src.ce.run.fetchers.data_fetcher import DataFetcher
from open_ticket_ai.src.ce.run.pipeline import Pipeline, PipelineContext


class Orchestrator(ConfigurableMixin):
    """Execute ticket processing pipelines."""

    def __init__(self, config: OpenTicketAIConfig, container: AbstractContainer):
        super().__init__(config)
        self.config = config
        self.container = container
        self._logger = logging.getLogger(__name__)

    def process_ticket(self, ticket_id: str, fetcher_id: str, pipeline: Pipeline) -> PipelineContext:
        """Fetch data and run ``pipeline`` for ``ticket_id``."""
        fetcher: DataFetcher = self.container.get_fetcher(fetcher_id)
        data = fetcher.fetch_data(ticket_id=ticket_id)
        context = PipelineContext(ticket_id=ticket_id, data=data)
        return pipeline.execute(context)
