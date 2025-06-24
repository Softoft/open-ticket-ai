# In open_ticket_ai/src/ce/core/config/config_models.py

from typing import Any, Self

from pydantic import BaseModel, Field, model_validator

from open_ticket_ai.src.ce.core.mixins.registry_instance_config import RegistryInstanceConfig


class SystemConfig(RegistryInstanceConfig):
    """Configuration for the ticket system adapter."""
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
    """Configuration for scheduling recurring tasks."""
    interval: int = Field(..., ge=1)
    unit: str = Field(..., min_length=1)


# NEW: This class replaces AttributePredictorConfig
class PipelineConfig(RegistryInstanceConfig):
    """Configuration for a single pipeline workflow."""
    schedule: SchedulerConfig
    # REMOVED fetcher_id. The pipes list is now the complete workflow.
    pipes: list[str] = Field(
        ...,
        min_length=1,
        description="Ordered list of all pipe component IDs to execute, starting with a fetcher."
    )

    def validate_pipe_ids_are_registered(self, all_pipe_ids: set[str]) -> None:
        """Validate that all pipe IDs in this pipeline exist."""
        for pipe_id in self.pipes:
            if pipe_id not in all_pipe_ids:
                raise ValueError(
                    f"Pipeline '{self.id}' references unknown pipe component '{pipe_id}'"
                )


# UPDATED: The root configuration model
class OpenTicketAIConfig(BaseModel):
    """Root configuration model for Open Ticket AI."""
    system: SystemConfig
    fetchers: list[FetcherConfig] = Field(..., min_length=1)
    data_preparers: list[PreparerConfig] = Field(..., min_length=1)
    ai_inference_services: list[AIInferenceServiceConfig] = Field(..., min_length=1)
    modifiers: list[ModifierConfig] = Field(..., min_length=1)
    pipelines: list[PipelineConfig] = Field(..., min_length=1)

    @model_validator(mode='after')
    def cross_validate_references(self) -> Self:
        """Validate that all pipeline references to components exist."""

        all_pipe_ids = {ric.id for ric in self.get_all_register_instance_configs()}

        for pipeline in self.pipelines:
            pipeline.validate_pipe_ids_are_registered(all_pipe_ids)
        return self

    def get_all_register_instance_configs(self) -> list[RegistryInstanceConfig]:
        """Return all registered instances in the configuration."""
        return (
            self.fetchers +
            self.data_preparers +
            self.ai_inference_services +
            self.modifiers +
            self.pipelines
        )


# load_config function remains the same
def load_config(path: str) -> OpenTicketAIConfig:
    # ... no change here
    pass
