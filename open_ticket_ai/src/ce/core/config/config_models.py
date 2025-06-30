# FILE_PATH: open_ticket_ai\src\ce\core\config\config_models.py
# In open_ticket_ai/src/ce/core/config/config_models.py

from typing import Any, Self

from pydantic import BaseModel, Field, model_validator


class ProvidableConfig(BaseModel):
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
        config = ProvidableConfig(
            id="docker-registry-1",
            provider_key="dockerhub",
        )
        ```
    """
    id: str = Field(..., min_length=1, description="The unique identifier for the registry instance.")
    params: dict[str, Any] = Field(
        default_factory=dict,
        description="Additional parameters for the registry instance configuration.",
    )
    provider_key: str = Field(
        ...,
        min_length=1,
        description="The key identifying the provider for the registry instance.",
    )


class SystemConfig(ProvidableConfig):
    """Configuration for the ticket system adapter.

    Attributes:
        params (dict[str, Any]): A dictionary of parameters specific to the ticket system adapter.
    """
    params: dict[str, Any] = Field(default_factory=dict)


class FetcherConfig(ProvidableConfig):
    """Configuration for data fetchers.

    This class represents the configuration for a data fetcher component. It inherits all attributes
    from `ProvidableConfig`.
    """


class PreparerConfig(ProvidableConfig):
    """Configuration for data preparers.

    This class represents the configuration for a data preparer component. It inherits all attributes
    from `ProvidableConfig`.
    """


class ModifierConfig(ProvidableConfig):
    """Configuration for modifiers.

    This class represents the configuration for a modifier component. It inherits all attributes
    from `ProvidableConfig`.
    """


class AIInferenceServiceConfig(ProvidableConfig):
    """Configuration for AI inference services.

    This class represents the configuration for an AI inference service component. It inherits all attributes
    from `ProvidableConfig`.
    """


class SchedulerConfig(BaseModel):
    """Configuration for scheduling recurring tasks.

    Attributes:
        interval (int): The interval of time to wait between runs. Must be at least 1.
        unit (str): The unit of time for the interval (e.g., 'minutes', 'hours'). Must be non-empty.
    """
    interval: int = Field(..., ge=1)
    unit: str = Field(..., min_length=1)


# NEW: This class replaces AttributePredictorConfig
class PipelineConfig(ProvidableConfig):
    """Configuration for a single pipeline workflow.

    Attributes:
        schedule (SchedulerConfig): The scheduling configuration for this pipeline.
        pipes (list[str]): Ordered list of all pipe component IDs to execute, starting with a fetcher.
            The list must have at least one element.
    """
    schedule: SchedulerConfig
    # REMOVED fetcher_id. The pipes list is now the complete workflow.
    pipes: list[str] = Field(
        ...,
        min_length=1,
        description="Ordered list of all pipe component IDs to execute, starting with a fetcher.",
    )

    def validate_pipe_ids_are_registered(self, all_pipe_ids: set[str]) -> None:
        """Validate that all pipe IDs in this pipeline exist.

        Args:
            all_pipe_ids (set[str]): A set of all registered pipe component IDs.

        Raises:
            ValueError: If any pipe ID in this pipeline is not found in `all_pipe_ids`.
        """
        for pipe_id in self.pipes:
            if pipe_id not in all_pipe_ids:
                raise ValueError(
                    f"Pipeline '{self.id}' references unknown pipe component '{pipe_id}'",
                )


# UPDATED: The root configuration model
class OpenTicketAIConfig(BaseModel):
    """Root configuration model for Open Ticket AI.

    Attributes:
        system (SystemConfig): Configuration for the ticket system adapter.
        fetchers (list[FetcherConfig]): List of data fetcher configurations. Must be non-empty.
        data_preparers (list[PreparerConfig]): List of data preparer configurations. Must be non-empty.
        ai_inference_services (list[AIInferenceServiceConfig]): List of AI inference service configurations. Must be non-empty.
        modifiers (list[ModifierConfig]): List of modifier configurations. Must be non-empty.
        pipelines (list[PipelineConfig]): List of pipeline configurations. Must be non-empty.
    """
    system: SystemConfig
    fetchers: list[FetcherConfig] = Field(..., min_length=1)
    data_preparers: list[PreparerConfig] = Field(..., min_length=1)
    ai_inference_services: list[AIInferenceServiceConfig] = Field(..., min_length=1)
    modifiers: list[ModifierConfig] = Field(..., min_length=1)
    pipelines: list[PipelineConfig] = Field(..., min_length=1)

    @model_validator(mode='after')
    def cross_validate_references(self) -> Self:
        """Validate that all pipeline references to components exist.

        This method is called by Pydantic during model validation. It checks that every pipe ID
        referenced in every pipeline exists in the set of all registered component IDs.

        Returns:
            Self: The validated model instance.

        Raises:
            ValueError: If any pipeline references a pipe ID that is not registered.
        """

        all_pipe_ids = {ric.id for ric in self.get_all_register_instance_configs()}

        for pipeline in self.pipelines:
            pipeline.validate_pipe_ids_are_registered(all_pipe_ids)
        return self

    def get_all_register_instance_configs(self) -> list[ProvidableConfig]:
        """Return all registered instances in the configuration.

        The returned list includes all instances of fetchers, data preparers, AI inference services,
        modifiers, and pipelines.

        Returns:
            list[ProvidableConfig]: A list of all registered instance configurations.
        """
        return (
            self.fetchers +
            self.data_preparers +
            self.ai_inference_services +
            self.modifiers +
            self.pipelines
        )


def load_config(path: str) -> OpenTicketAIConfig:
    """Load a YAML configuration file from the given path.

    The configuration file must have a root key 'open_ticket_ai' containing the configuration.

    Args:
        path (str): The path to the YAML configuration file.

    Returns:
        OpenTicketAIConfig: The loaded configuration.

    Raises:
        OSError: If there is an error opening the file (e.g., file not found, permission denied).
        yaml.YAMLError: If there is an error parsing the YAML.
        KeyError: If the root key 'open_ticket_ai' is missing.
        pydantic.ValidationError: If the configuration data does not match the expected schema.
    """
    import yaml

    with open(path, encoding="utf-8") as fh:
        data = yaml.safe_load(fh)

    if "open_ticket_ai" not in data:
        raise KeyError("Missing 'open_ticket_ai' root key")

    return OpenTicketAIConfig(**data["open_ticket_ai"])