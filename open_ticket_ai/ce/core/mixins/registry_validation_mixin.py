from pydantic import BaseModel, Field

from open_ticket_ai.ce.core import registry


# noinspection PyNestedDecorators
class Registerable(BaseModel):
    """Base model for registry-aware configuration objects."""

    # point to the real registry by default
    provider_key: str = Field(..., min_length=1)
