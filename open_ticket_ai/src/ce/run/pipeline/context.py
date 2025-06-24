from dataclasses import dataclass
from typing import Any, Dict


@dataclass
class PipelineContext:
    """Context object passed between pipeline stages."""

    ticket_id: str
    data: Dict
    prepared_data: Any | None = None
    model_result: Any | None = None
