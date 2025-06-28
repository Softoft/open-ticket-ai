# In open_ticket_ai/src/ce/core/config/config_models.py

from typing import Any, Self

from pydantic import BaseModel, Field, model_validator

from open_ticket_ai.src.ce.core.mixins.registry_instance_config import RegistryInstanceConfig


class SystemConfig(RegistryInstanceConfig):
    """Configuration for the ticket system adapter.

    Attributes:
        params (dict[str, Any]): A dictionary of parameters specific to the ticket system adapter.
    """
    params: dict[str, Any] = Field(default_factory=dict)


class FetcherConfig(RegistryInstanceConfig):
    """Configuration for data fetchers."""


class PreparerConfig(RegistryInstanceConfig):
    """Configuration for data preparers."""


class ModifierConfig(RegistryInstanceConfig):
    """Configuration for modifiers."""


class AIInferenceServiceConfig(RegistryInstanceConfig):
    """Configuration for AI inference services."""


class SchedulerConfig(BaseModel):
    """Configuration for scheduling recurring tasks.

    Attributes:
        interval (int): The interval of time to wait between runs. Must be at least 1.
        unit (str): The unit of time for the interval (e.g., 'minutes', 'hours'). Must be non-empty.
    """
    interval: int = Field(..., ge=1)
    unit: str = Field(..., min_length=1)


# NEW: This class replaces AttributePredictorConfig
class PipelineConfig(RegistryInstanceConfig):
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
        description="Ordered list of all pipe component IDs to execute, starting with a fetcher."
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
                    f"Pipeline '{self.id}' references unknown pipe component '{pipe_id}'"
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

    def get_all_register_instance_configs(self) -> list[RegistryInstanceConfig]:
        """Return all registered instances in the configuration.

        The returned list includes all instances of fetchers, data preparers, AI inference services,
        modifiers, and pipelines.

        Returns:
            list[RegistryInstanceConfig]: A list of all registered instance configurations.
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

    with open(path, "r", encoding="utf-8") as fh:
        data = yaml.safe_load(fh)

    if "open_ticket_ai" not in data:
        raise KeyError("Missing 'open_ticket_ai' root key")

    return OpenTicketAIConfig(**data["open_ticket_ai"])