import os
from typing import Any, Dict, List

import yaml
from pydantic import BaseModel, Field, HttpUrl, field_validator, model_validator

from registry import does_registry_contain


class SystemConfig(BaseModel):
    name: str = Field(..., min_length=1)
    base_url: HttpUrl
    username: str = Field(..., min_length=1)
    password_env_var: str = Field(..., min_length=1)
    incoming_queue: str = Field(..., min_length=1)

    @classmethod
    @field_validator("type", mode="after")
    def validate_adapter_type(cls, v: str) -> str:
        if not does_registry_contain(v):
            raise ValueError(f"Adapter '{v}' is not registered")
        return v


class RegistryInstanceConfig(BaseModel):
    id: str = Field(..., min_length=1)
    type: str = Field(..., min_length=1)
    params: Dict[str, Any] = Field(default_factory=dict)

    @classmethod
    @field_validator("type", mode="after")
    def validate_preparer_type(cls, v: str) -> str:
        if not does_registry_contain(v):
            raise ValueError(f"Preparer '{v}' is not registered")
        return v


class FetcherConfig(RegistryInstanceConfig):
    interval_secs: int = Field(..., gt=0)
    filters: List[Dict[str, Any]] = Field(default_factory=list)
    limit: int = Field(..., ge=1)


class PreparerConfig(RegistryInstanceConfig):
    pass


class ModifierConfig(RegistryInstanceConfig):
    pass


class ModelSpec(RegistryInstanceConfig):
    pass


class AttributePredictors(RegistryInstanceConfig):
    fetcher_id: str = Field(..., min_length=1)
    preparer_id: str = Field(..., min_length=1)
    attribute_predictor_id: ModelSpec
    modifier_id: str = Field(..., min_length=1)
    output_attr: str = Field(..., min_length=1)
    mapping: Dict[str, List[Any]] = Field(default_factory=dict)


class OpenTicketAIConfig(BaseModel):
    hf_token_env_var: str = Field(..., min_length=1)
    system: SystemConfig
    fetchers: List[FetcherConfig] = Field(..., min_length=1)
    data_preparers: List[PreparerConfig] = Field(..., min_length=1)
    modifiers: List[ModifierConfig] = Field(..., min_length=1)
    attribute_predictors: List[AttributePredictors] = Field(..., min_length=1)

    @property
    def hf_token(self) -> str:
        return os.getenv(self.hf_token_env_var)

    @classmethod
    @model_validator(mode="after")
    def cross_validate_references(cls, values: Dict[str, Any]) -> Dict[str, Any]:
        fetcher_ids = {f.id for f in values.get("fetchers", [])}
        preparer_ids = {p.id for p in values.get("data_preparers", [])}
        modifier_ids = {m.id for m in values.get("modifiers", [])}

        for feature in values["attribute_predictors"]:
            if feature.fetcher_id not in fetcher_ids:
                raise ValueError(f"Feature '{feature.id}' refs unknown fetcher '{feature.fetcher_id}'")
            if feature.preparer_id not in preparer_ids:
                raise ValueError(f"Feature '{feature.id}' refs unknown preparer '{feature.preparer_id}'")
            if feature.modifier_id not in modifier_ids:
                raise ValueError(f"Feature '{feature.id}' refs unknown modifier '{feature.modifier_id}'")
        return values


def load_config(path: str) -> OpenTicketAIConfig:
    """
    Load and validate config. Optionally inject a custom Registry.
    """
    raw = yaml.safe_load(open(path))
    cfg = raw.get('open_ticket_ai')
    if cfg is None:
        raise KeyError("Missing 'open_ticket_ai' root key in config file")
    return OpenTicketAIConfig(**cfg)
