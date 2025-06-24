# tests/core/config_test.py

import yaml
import pytest
from pydantic import ValidationError

from open_ticket_ai.ce.core import registry, config_models
from open_ticket_ai.ce.core.mixins.registry_validation_mixin import Registerable


def make_minimal_config_dict():
    """
    Build the smallest valid dict for OpenTicketAIConfig,
    with one fetcher, one preparer, one modifier and one predictor.
    """
    return {
        "system": {
            "provider_key": "dummy_sys",
            "params": {}
        },
        "fetchers": [
            {
                "id": "fetch1",
                "provider_key": "dummy_fetcher",
                "params": {}
            }
        ],
        "data_preparers": [
            {
                "id": "prep1",
                "provider_key": "dummy_preparer",
                "params": {}
            }
        ],
        "ai_inference_services": [
            {
                "id": "model1",
                "provider_key": "dummy_model",
                "params": {}
            }
        ],
        "modifiers": [
            {
                "id": "mod1",
                "provider_key": "dummy_modifier",
                "params": {}
            }
        ],
        "attribute_predictors": [
            {
                "id": "pred1",
                "provider_key": "dummy_predictor",
                "fetcher_id": "fetch1",
                "preparer_id": "prep1",
                "ai_inference_service_id": "model1",
                "modifier_id": "mod1",
                "params": {}
            }
        ]
    }


# ─── SchedulerConfig validation ────────────────────────────────────────────────────────

def test_schedulerconfig_valid():
    sc = config_models.SchedulerConfig(interval=1, unit="seconds")
    assert sc.interval == 1
    assert sc.unit == "seconds"


@pytest.mark.parametrize("interval", [0, -5])
def test_schedulerconfig_invalid_interval(interval):
    with pytest.raises(ValidationError):
        config_models.SchedulerConfig(interval=interval, unit="minutes")


def test_schedulerconfig_invalid_unit():
    with pytest.raises(ValidationError):
        config_models.SchedulerConfig(interval=5, unit="")

# ─── OpenTicketAIConfig list‐length validations ───────────────────────────────────────

@pytest.mark.parametrize("list_name", [
    "fetchers", "data_preparers", "modifiers", "attribute_predictors"
])
def test_open_ticket_ai_empty_list_fails(list_name):
    cfg = make_minimal_config_dict()
    cfg[list_name] = []
    with pytest.raises(ValidationError):
        config_models.OpenTicketAIConfig(**cfg)


# ─── load_config() behavior ────────────────────────────────────────────────────────────

def test_load_config_missing_root(tmp_path):
    p = tmp_path / "c.yaml"
    p.write_text("something_else: {}")
    with pytest.raises(KeyError) as exc:
        config_models.load_config(str(p))
    assert "Missing 'open_ticket_ai' root fetcher_key" in str(exc.value)

