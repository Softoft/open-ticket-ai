# FILE_PATH: open_ticket_ai\src\ce\run\pipeline\pipeline.py
from __future__ import annotations

from typing import List

from .context import PipelineContext
from .pipe import Pipe
from ...core.config.config_models import PipelineConfig


class Pipeline(Pipe):
    """Composite pipe executing a sequence of pipes.

    The Pipeline class represents a composite pipe that executes a sequence of
    individual pipes in a defined order. It implements the Pipe interface and
    processes data by sequentially passing a context object through each
    component pipe.

    Attributes:
        pipes: An ordered list of Pipe instances to execute sequentially.
    """

    def __init__(self, config: PipelineConfig, pipes: List[Pipe]):
        """Initializes the Pipeline with configuration and component pipes.

        Args:
            config: Configuration settings for the pipeline.
            pipes: Ordered list of Pipe instances to execute sequentially.
        """
        super().__init__(config)
        self.pipes = pipes

    def execute(self, context: PipelineContext) -> PipelineContext:
        """Executes all pipes in the pipeline sequentially.

        Processes the context through each pipe in the defined order, passing
        the output of one pipe as input to the next.

        Args:
            context: The initial pipeline context containing data to process.

        Returns:
            The final context after processing through all pipes.
        """
        current = context
        for pipe in self.pipes:
            current = pipe.process(current)
        return current

    def process(self, context: PipelineContext) -> PipelineContext:
        """Processes context through the entire pipeline.

        This method implements the Pipe interface by delegating to execute().

        Args:
            context: The pipeline context to process.

        Returns:
            The modified context after pipeline execution.
        """
        return self.execute(context)
