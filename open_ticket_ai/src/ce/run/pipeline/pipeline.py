from __future__ import annotations

from typing import List

from .context import PipelineContext
from .pipe import Pipe
from ...core.config.config_models import PipelineConfig


class Pipeline(Pipe):
    """Composite pipe executing a sequence of pipes."""

    def __init__(self, config: PipelineConfig, pipes: List[Pipe]):
        super().__init__(config)
        self.pipes = pipes

    def execute(self, context: PipelineContext) -> PipelineContext:
        current = context
        for pipe in self.pipes:
            current = pipe.process(current)
        return current

    def process(self, context: PipelineContext) -> PipelineContext:
        return self.execute(context)
