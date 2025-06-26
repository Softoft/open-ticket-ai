from typing import Any

from pydantic import BaseModel, Field


class RegistryInstanceConfig(BaseModel):
    """Base configuration for registry instances.

    This class defines the core configuration structure required for initializing
    and managing registry instances. Each registry instance must have a unique
    identifier, a provider key, and can include additional provider-specific
    parameters.

    Attributes:
        id: A unique string identifier for the registry instance. Must be at least
            1 character long.
        params: A dictionary of additional configuration parameters specific to the
                registry provider. Defaults to an empty dictionary.
        provider_key: A string key identifying the provider implementation for this
                      registry instance. Must be at least 1 character long.

    Example:
        ```python
        config = RegistryInstanceConfig(
            id="docker-registry-1",
            provider_key="dockerhub",
            params={"base_url": "https://index.docker.io/v1/"}
        )
        ```
    """
    id: str = Field(..., min_length=1, description="The unique identifier for the registry instance.")
    params: dict[str, Any] = Field(default_factory=dict, description="Additional parameters for the registry instance configuration.")
    provider_key: str = Field(..., min_length=1, description="The key identifying the provider for the registry instance.")