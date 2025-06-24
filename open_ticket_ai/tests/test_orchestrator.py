import importlib
from types import SimpleNamespace

from pydantic import BaseModel
import pytest

import open_ticket_ai.src.ce.core as core
from open_ticket_ai.src.ce.core.dependency_injection.abstract_container import AbstractContainer
import open_ticket_ai.src.ce.core.util.pretty_print_config as pp

# disable pretty printing during tests
pp.pretty_print_config = lambda cfg: None


class DummyPredictorCfg(BaseModel):
    id: str


class DummyConfig(BaseModel):
    attribute_predictors: list[DummyPredictorCfg]


class DummyPredictor:
    def __init__(self, desc: str):
        self.desc = desc
        self.set_schedule_called = False

    def set_schedule(self):
        self.set_schedule_called = True

    def get_description(self) -> str:
        return self.desc


@pytest.fixture(autouse=True)
def provide_abstract_container(monkeypatch):
    monkeypatch.setattr(core, "AbstractContainer", AbstractContainer, raising=False)
    yield


def make_config(ids):
    return DummyConfig(attribute_predictors=[DummyPredictorCfg(id=i) for i in ids])


def test_initializes_attribute_predictors(monkeypatch):
    from open_ticket_ai.src.ce.run.orchestrator import Orchestrator

    calls = []

    def fake_get_predictor(pid):
        calls.append(pid)
        return f"predictor_{pid}"

    container = SimpleNamespace(get_predictor=fake_get_predictor)
    cfg = make_config(["a", "b", "c"])

    orch = Orchestrator(cfg, container)

    assert calls == ["a", "b", "c"]
    assert orch.attribute_predictors == ["predictor_a", "predictor_b", "predictor_c"]


def test_set_schedules_calls_all_predictors(monkeypatch, capsys):
    from open_ticket_ai.src.ce.run.orchestrator import Orchestrator

    predictors = {
        "x": DummyPredictor("X desc"),
        "y": DummyPredictor("Y desc"),
    }

    def fake_get_predictor(pid):
        return predictors[pid]

    container = SimpleNamespace(get_predictor=fake_get_predictor)
    cfg = make_config(["x", "y"])

    orch = Orchestrator(cfg, container)
    orch.set_schedules()

    assert predictors["x"].set_schedule_called is True
    assert predictors["y"].set_schedule_called is True

    out = capsys.readouterr().out
    assert "Scheduled X desc" in out
    assert "Scheduled Y desc" in out
