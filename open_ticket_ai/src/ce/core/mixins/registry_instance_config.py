from typing import Any

from pydantic import BaseModel, Field


class RegistryInstanceConfig(BaseModel):
    """Base configuration for registry instances."""
    id: str = Field(..., min_length=1)
    params: dict[str, Any] = Field(default_factory=dict)
    provider_key: str = Field(..., min_length=1)
