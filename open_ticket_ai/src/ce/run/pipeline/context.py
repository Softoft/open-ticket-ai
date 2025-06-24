from typing import Any, Dict

from pydantic import BaseModel


class PipelineContext(BaseModel):
    """Context object passed between pipeline stages."""

    ticket_id: str
    data: dict[str, Any] = {}
