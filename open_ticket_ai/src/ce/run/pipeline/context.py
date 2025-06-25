from typing import Any, Dict

from pydantic import BaseModel


class PipelineContext(BaseModel):
    """Context object passed between pipeline stages.

    Attributes:
        ticket_id (str): The ID of the ticket being processed.
        data (dict[str, Any]): A dictionary to hold arbitrary data for the pipeline stages. Defaults to an empty dictionary.
    """

    ticket_id: str
    data: dict[str, Any] = {}