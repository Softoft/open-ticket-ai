from typing import Any

from pydantic import BaseModel, Field


class RegistryInstanceConfig(BaseModel):
    """Base configuration for registry instances."""
    id: str = Field(..., min_length=1, description="The unique identifier for the registry instance.")
    params: dict[str, Any] = Field(default_factory=dict, description="Additional parameters for the registry instance configuration.")
    provider_key: str = Field(..., min_length=1, description="The key identifying the provider for the registry instance.")