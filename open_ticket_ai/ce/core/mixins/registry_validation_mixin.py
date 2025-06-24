from typing import Callable

from pydantic import BaseModel, Field, field_validator

from open_ticket_ai.ce.core import registry


# noinspection PyNestedDecorators
class Registerable(BaseModel):
    # point to the real registry by default
    provider_key: str = Field(..., min_length=1)
