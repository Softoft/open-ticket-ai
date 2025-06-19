# tests/core/config_test.py

import yaml
import pytest
from pydantic import ValidationError

from open_ticket_ai.ce.core import registry, config_models
from open_ticket_ai.ce.core.config_models import RegistryValidationMixin


def make_minimal_config_dict():
    """
    Build the smallest valid dict for OpenTicketAIConfig,
    with one fetcher, one preparer, one modifier and one predictor.
    """
    return {
        "system": {
            "type": "dummy_sys",
            "params": {}
        },
        "fetchers": [
            {
                "id": "fetch1",
                "type": "dummy_fetcher",
                "params": {}
            }
        ],
        "data_preparers": [
            {
                "id": "prep1",
                "type": "dummy_preparer",
                "params": {}
            }
        ],
        "models": [
            {
                "id": "model1",
                "type": "dummy_model",
                "params": {}
            }
        ],
        "modifiers": [
            {
                "id": "mod1",
                "type": "dummy_modifier",
                "params": {}
            }
        ],
        "attribute_predictors": [
            {
                "id": "pred1",
                "type": "dummy_predictor",
                "fetcher_id": "fetch1",
                "preparer_id": "prep1",
                "model_id": "model1",
                "modifier_id": "mod1",
                "output_attr": "some_field",
                "params": {}
            }
        ]
    }


# ─── RegistryValidationMixin via SystemConfig ──────────────────────────────────────────

def test_systemconfig_allows_registered_type():
    RegistryValidationMixin._set_registry_check(lambda v: v == "ok_sys")
    sc = config_models.SystemConfig(type="ok_sys", params={"foo": 1})
    assert sc.type == "ok_sys"
    assert sc.params == {"foo": 1}


def test_systemconfig_rejects_unregistered():
    RegistryValidationMixin._set_registry_check(lambda v: False)
    with pytest.raises(ValidationError) as exc:
        config_models.SystemConfig(type="bad", params={})
    assert "Type 'bad' is not registered" in str(exc.value)


# ─── RegistryInstanceConfig subclasses ────────────────────────────────────────────────

@pytest.mark.parametrize("cls_name", [
    "FetcherConfig",
    "PreparerConfig",
    "ModifierConfig",
    "ModelSpec",
])
def test_registry_instance_config_types(cls_name):
    cls = getattr(config_models, cls_name)
    # only 'good' passes
    RegistryValidationMixin._set_registry_check(lambda v: v == "good")
    inst = cls(id="i1", type="good", params={"a": True})
    assert inst.id == "i1"
    assert inst.type == "good"

    # 'bad' should be rejected
    with pytest.raises(ValidationError) as exc:
        cls(id="i1", type="bad", params={})
    assert "Type 'bad' is not registered" in str(exc.value)


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


# ─── AttributePredictors missing/extra fields ───────────────────────────────────────────

def test_attribute_predictor_requires_output_attr():
    RegistryValidationMixin._set_registry_check(lambda v: True)
    cfg = make_minimal_config_dict()
    # remove required output_attr
    del cfg["attribute_predictors"][0]["output_attr"]
    with pytest.raises(ValidationError) as exc:
        config_models.OpenTicketAIConfig(**cfg)
    # note capital "Field required"
    assert "Field required" in str(exc.value)


def test_attribute_predictor_params_default():
    RegistryValidationMixin._set_registry_check(lambda v: True)
    cfg = make_minimal_config_dict()
    # omit params → should default to {}
    del cfg["attribute_predictors"][0]["params"]
    loaded = config_models.OpenTicketAIConfig(**cfg)
    assert loaded.attribute_predictors[0].params == {}


# ─── cross_validate_references ────────────────────────────────────────────────────────

def test_cross_validate_references_success():
    RegistryValidationMixin._set_registry_check(lambda v: True)
    cfg = make_minimal_config_dict()
    otc = config_models.OpenTicketAIConfig(**cfg)
    assert otc.fetchers[0].id == "fetch1"
    assert otc.attribute_predictors[0].fetcher_id == "fetch1"


@pytest.mark.parametrize("field,bad,errmsg", [
    ("fetcher_id",  "X", "unknown fetcher"),
    ("preparer_id", "Y", "unknown preparer"),
    ("modifier_id", "Z", "unknown modifier"),
])
def test_cross_validate_references_failure(field, bad, errmsg):
    RegistryValidationMixin._set_registry_check(lambda v: True)
    cfg = make_minimal_config_dict()
    cfg["attribute_predictors"][0][field] = bad
    # The model_validator raises a plain ValueError
    with pytest.raises(ValueError) as exc:
        config_models.OpenTicketAIConfig(**cfg)
    assert errmsg in str(exc.value)


# ─── OpenTicketAIConfig list‐length validations ───────────────────────────────────────

@pytest.mark.parametrize("list_name", [
    "fetchers", "data_preparers", "modifiers", "attribute_predictors"
])
def test_open_ticket_ai_empty_list_fails(list_name):
    RegistryValidationMixin._set_registry_check(lambda v: True)
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
    assert "Missing 'open_ticket_ai' root key" in str(exc.value)


def test_load_config_success(tmp_path):
    cfg = make_minimal_config_dict()
    path = tmp_path / "good.yaml"
    path.write_text(yaml.safe_dump({"open_ticket_ai": cfg}))

    loaded = config_models.load_config(str(path))
    assert isinstance(loaded, config_models.OpenTicketAIConfig)
    assert loaded.system.type == "dummy_sys"
    assert loaded.fetchers[0].id == "fetch1"
    assert loaded.attribute_predictors[0].output_attr == "some_field"
