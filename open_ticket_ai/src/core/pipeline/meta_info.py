from typing import Optional

from pydantic import BaseModel

from open_ticket_ai.src.core.pipeline.status import PipelineStatus


class MetaInfo(BaseModel):
    """Stores metadata about the pipeline execution state.

    This model captures the current status of a pipeline along with any error
    information when failures occur.

    Attributes:
        status: Current execution status of the pipeline. Defaults to RUNNING.
        error_message: Detailed error message if the pipeline failed. None if successful.
        failed_pipe: Identifier of the specific pipe that caused failure. None if successful.
    """
    status: PipelineStatus = PipelineStatus.RUNNING
    error_message: Optional[str] = None
    failed_pipe: Optional[str] = None
