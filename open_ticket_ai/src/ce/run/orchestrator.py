"""Top level orchestration utilities."""
from __future__ import annotations

import logging

from open_ticket_ai.src.ce.core.config.config_models import OpenTicketAIConfig
from open_ticket_ai.src.ce.core.dependency_injection.abstract_container import AbstractContainer
from open_ticket_ai.src.ce.run.pipeline.context import PipelineContext
from open_ticket_ai.src.ce.run.pipeline.pipeline import Pipeline


class Orchestrator:
    """Execute ticket processing pipelines."""

    def __init__(self, config: OpenTicketAIConfig, container: AbstractContainer):
        self.config = config
        self.container = container
        self._logger = logging.getLogger(__name__)

    def process_ticket(self, ticket_id: str,
                       pipeline: Pipeline) -> PipelineContext:
        """Fetch data and run ``pipeline`` for ``ticket_id``."""
        return pipeline.execute(PipelineContext(ticket_id=ticket_id))
