from typing import Any, Dict, Self

import yaml
from pydantic import BaseModel, Field, model_validator

from open_ticket_ai.ce.core.mixins.registry_validation_mixin import Registerable


class SystemConfig(Registerable):
    params: dict[str, Any] = Field(default_factory=dict)


class RegistryInstanceConfig(Registerable):
    id: str = Field(..., min_length=1)
    params: dict[str, Any] = Field(default_factory=dict)


class FetcherConfig(RegistryInstanceConfig):
    pass


class PreparerConfig(RegistryInstanceConfig):
    pass


class ModifierConfig(RegistryInstanceConfig):
    pass


class AIInferenceServiceConfig(RegistryInstanceConfig):
    pass


class SchedulerConfig(BaseModel):
    interval: int = Field(..., ge=1, description="Interval for the scheduler to run")
    unit: str = Field(..., min_length=1,
                      description="Unit of time for the interval (e.g., 'seconds', 'minutes', 'hours')")


class AttributePredictorsConfig(RegistryInstanceConfig):
    fetcher_id: str = Field(..., min_length=1)
    preparer_id: str = Field(..., min_length=1)
    ai_inference_service_id: str = Field(..., min_length=1, description="ID of the model to use for prediction")
    modifier_id: str = Field(..., min_length=1)
    params: Dict[str, Any] = Field(default_factory=dict)


# noinspection PyNestedDecorators
class OpenTicketAIConfig(BaseModel):
    system: SystemConfig = Field(..., description="System configuration")
    fetchers: list[FetcherConfig] = Field(..., min_length=1)
    data_preparers: list[PreparerConfig] = Field(..., min_length=1)
    ai_inference_services: list[AIInferenceServiceConfig] = Field(..., min_length=1)
    modifiers: list[ModifierConfig] = Field(..., min_length=1)
    attribute_predictors: list[AttributePredictorsConfig] = Field(..., min_length=1)

    @model_validator(mode='after')
    def cross_validate_references(self) -> Self:
        fetcher_ids = {f.id for f in self.fetchers}
        preparer_ids = {p.id for p in self.data_preparers}
        ai_inference_services_ids = {m.id for m in self.ai_inference_services}
        modifier_ids = {m.id for m in self.modifiers}

        for attribute_predictor in self.attribute_predictors:
            if attribute_predictor.fetcher_id not in fetcher_ids:
                raise ValueError(
                    f"attribute_predictor '{attribute_predictor.id}' refs unknown fetcher '{attribute_predictor.fetcher_id}'")
            if attribute_predictor.preparer_id not in preparer_ids:
                raise ValueError(
                    f"attribute_predictor '{attribute_predictor.id}' refs unknown preparer '{attribute_predictor.preparer_id}'")
            if attribute_predictor.ai_inference_service_id not in ai_inference_services_ids:
                raise ValueError(
                    f"attribute_predictor '{attribute_predictor.id}' refs unknown model '{attribute_predictor.ai_inference_service_id}'")
            if attribute_predictor.modifier_id not in modifier_ids:
                raise ValueError(
                    f"attribute_predictor '{attribute_predictor.id}' refs unknown modifier '{attribute_predictor.modifier_id}'")
        return self


def load_config(path: str) -> OpenTicketAIConfig:
    """
    Load and validate config. Optionally inject a custom Registry.
    """
    with open(path, encoding="utf-8") as f:
        raw = yaml.safe_load(f)
    cfg = raw.get('open_ticket_ai')
    if cfg is None:
        raise KeyError("Missing 'open_ticket_ai' root fetcher_key in config file")
    return OpenTicketAIConfig(**cfg)
