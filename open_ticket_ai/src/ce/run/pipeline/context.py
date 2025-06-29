# FILE_PATH: open_ticket_ai\src\ce\run\pipeline\context.py
from typing import Any, Optional

from pydantic import BaseModel

from open_ticket_ai.src.ce.run.pipeline.status import PipelineStatus


class PipelineContext(BaseModel):
    """Context object passed between pipeline stages.

    This class serves as a container for sharing state and data across different stages
    of a processing pipeline. It uses Pydantic for data validation and serialization.

    Attributes:
        ticket_id (str): The unique identifier of the ticket being processed through
            the pipeline stages.
        data (dict[str, Any]): A flexible dictionary for storing arbitrary data exchanged
            between pipeline stages. Defaults to an empty dictionary.
    """

    ticket_id: str
    data: dict[str, Any] = {}
    status: PipelineStatus = PipelineStatus.RUNNING
    error_message: Optional[str] = None
    failed_pipe: Optional[str] = None

    def stop_pipeline(self):
        """A convenience method for pipes to signal a controlled stop."""
        self.status = PipelineStatus.STOPPED
