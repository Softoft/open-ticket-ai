"""Defines the Pipeline class for executing a sequence of pipes.

The Pipeline is a specialized Pipe that runs multiple pipes in sequence. It manages the context
and status throughout the execution, handling errors and stop requests appropriately.
"""

from __future__ import annotations

import logging  # Use logging for errors
from typing import List

from .context import PipelineContext
from .pipe import Pipe
from .status import PipelineStatus  # Import the status enum
from ...core.config.config_models import PipelineConfig

# It's good practice to have a logger
logger = logging.getLogger(__name__)


class Pipeline(Pipe[None, None]):
    """A pipeline that executes a sequence of pipes sequentially.

    This class manages the execution flow of multiple pipes, handling status transitions,
    error propagation, and stop requests during processing.

    Attributes:
        pipes: List of Pipe objects to execute in sequence.
    """

    def __init__(self, config: PipelineConfig, pipes: List[Pipe]):
        """Initializes the Pipeline with configuration and pipe sequence.

        Args:
            config: Configuration settings for the pipeline.
            pipes: Ordered list of Pipe instances to execute.
        """
        super().__init__(config)
        self.pipes = pipes

    def execute(self, context: PipelineContext) -> PipelineContext:
        """Executes all pipes sequentially with error handling and status propagation.

        Processes each pipe in sequence while:
        - Validating input data using each pipe's input model
        - Handling STOPPED status requests from pipes
        - Catching and logging exceptions during pipe execution
        - Updating context status appropriately (RUNNING, SUCCESS, FAILED, STOPPED)

        Args:
            context: The pipeline context containing execution state and data.

        Returns:
            Updated PipelineContext reflecting final execution state after processing.

        Notes:
            - Starts execution only if context status is RUNNING or SUCCESS
            - Sets context to RUNNING at start of execution
            - Breaks processing loop on STOPPED status or uncaught exception
            - Automatically sets status to SUCCESS if all pipes complete without errors
        """
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
                pipe_input = pipe.InputDataT.model_validate(context)
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
        """Processes context through the entire pipeline sequence.

        Implements the abstract method from the Pipe base class. Delegates to
        the `execute()` method for actual pipeline processing.

        Args:
            context: The pipeline context containing execution state and data.

        Returns:
            Updated PipelineContext after processing through all pipes.
        """
        return self.execute(context)