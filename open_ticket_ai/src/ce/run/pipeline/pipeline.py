# FILE_PATH: open_ticket_ai\src\ce\run\pipeline\pipeline.py
from __future__ import annotations

import logging  # Use logging for errors
from typing import List

from .context import PipelineContext
from .pipe import Pipe
from .status import PipelineStatus  # Import the status enum
from ...core.config.config_models import PipelineConfig

# It's good practice to have a logger
logger = logging.getLogger(__name__)


class Pipeline(Pipe):
    def __init__(self, config: PipelineConfig, pipes: List[Pipe]):
        super().__init__(config)
        self.pipes = pipes

    def execute(self, context: PipelineContext) -> PipelineContext:
        """Executes all pipes sequentially, with error and stop handling."""

        # Ensure the context starts in a runnable state.
        if context.status not in [PipelineStatus.RUNNING, PipelineStatus.SUCCESS]:
            logger.warning(
                f"Pipeline for ticket {context.ticket_id} started with non-runnable status: {context.status.name}",
            )
            return context

        context.status = PipelineStatus.RUNNING

        for pipe in self.pipes:
            try:
                # Process the context with the current pipe
                context = pipe.process(context)

                # After processing, check if the pipe requested a stop
                if context.status == PipelineStatus.STOPPED:
                    logger.info(f"Pipeline stopped by '{pipe.__class__.__name__}' for ticket {context.ticket_id}.")
                    break  # Exit the loop for a controlled stop

            except Exception as e:
                # An unexpected error occurred in the pipe
                logger.error(
                    f"Pipeline failed at pipe '{pipe.__class__.__name__}' for ticket {context.ticket_id}.",
                    exc_info=True,
                )
                context.status = PipelineStatus.FAILED
                context.error_message = str(e)
                context.failed_pipe = pipe.__class__.__name__
                break  # Exit the loop on failure

        # If the loop completed without being stopped or failing, mark it as successful
        if context.status == PipelineStatus.RUNNING:
            context.status = PipelineStatus.SUCCESS

        return context

    def process(self, context: PipelineContext) -> PipelineContext:
        """Processes context through the entire pipeline."""
        return self.execute(context)
