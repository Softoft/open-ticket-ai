"""Top level orchestration utilities."""

from __future__ import annotations

import logging

import schedule

from open_ticket_ai.src.ce.core.config.config_models import OpenTicketAIConfig
from open_ticket_ai.src.ce.core.dependency_injection.abstract_container import (
    AbstractContainer,
)
from open_ticket_ai.src.ce.run.pipeline.context import PipelineContext
from open_ticket_ai.src.ce.run.pipeline.pipeline import Pipeline


class Orchestrator:
    """Execute ticket processing pipelines."""

    def __init__(self, config: OpenTicketAIConfig, container: AbstractContainer):
        """Initialize the Orchestrator with configuration and DI container.

        Args:
            config: Configuration settings for the orchestrator.
            container: Dependency injection container providing pipeline instances.
        """
        self.config = config
        self.container = container
        self._logger = logging.getLogger(__name__)
        self._pipelines: dict[str, Pipeline] = {}

    def process_ticket(self, ticket_id: str, pipeline: Pipeline) -> PipelineContext:
        """Fetch data and run ``pipeline`` for ``ticket_id``."""
        return pipeline.execute(PipelineContext(ticket_id=ticket_id))

    def build_pipelines(self) -> None:
        """Instantiate pipeline objects using the DI container."""
        for pipeline_cfg in self.config.pipelines:
            self._pipelines[pipeline_cfg.id] = self.container.get_pipeline(pipeline_cfg.id)

    def set_schedules(self) -> None:
        """Schedule pipeline execution according to configuration."""
        self.build_pipelines()
        for pipeline_cfg in self.config.pipelines:
            pipeline = self._pipelines[pipeline_cfg.id]
            sched = getattr(
                schedule.every(pipeline_cfg.schedule.interval), pipeline_cfg.schedule.unit
            )
            sched.do(pipeline.execute, PipelineContext(ticket_id=""))