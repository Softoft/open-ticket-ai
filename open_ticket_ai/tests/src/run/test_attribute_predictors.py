import builtins
from unittest.mock import MagicMock

import pytest

from open_ticket_ai.src.ce.core.config.config_models import AttributePredictorConfig, SchedulerConfig
from open_ticket_ai.src.ce.run.attribute_predictors.priority_predictor import PriorityPredictor
from open_ticket_ai.src.ce.run.attribute_predictors.queue_predictor import QueuePredictor
from open_ticket_ai.src.ce.run.attribute_predictors import attribute_predictor as ap_module


@pytest.fixture
def dummy_config():
    return AttributePredictorConfig(
        id="ap",
        provider_key="dummy",
        fetcher_id="fetcher",
        preparer_id="preparer",
        ai_inference_service_id="service",
        modifier_id="modifier",
        schedule=SchedulerConfig(interval=1, unit="seconds"),
    )


def make_predictor(predictor_cls, config):
    fetcher = MagicMock()
    preparer = MagicMock()
    ai_service = MagicMock()
    modifier = MagicMock()
    return predictor_cls(config, fetcher, preparer, ai_service, modifier), fetcher, preparer, ai_service, modifier


def test_set_schedule_registers_job(monkeypatch, dummy_config):
    pred, *_ = make_predictor(PriorityPredictor, dummy_config)

    class DummyJob:
        def __init__(self):
            self.do_called_with = None
            self.unit_accessed = False

        @property
        def seconds(self):
            self.unit_accessed = True
            return self

        def do(self, func):
            self.do_called_with = func

    dummy_job = DummyJob()

    every_mock = MagicMock(return_value=dummy_job)
    monkeypatch.setattr(ap_module.schedule, "every", every_mock)

    pred.run_attribute_prediction = MagicMock()

    pred.set_schedule()

    every_mock.assert_called_once_with(dummy_config.schedule.interval)
    assert dummy_job.unit_accessed
    assert callable(dummy_job.do_called_with)

    dummy_job.do_called_with()
    pred.run_attribute_prediction.assert_called_once_with()


def test_priority_predictor_pipeline(monkeypatch, dummy_config):
    pred, fetcher, preparer, ai_service, modifier = make_predictor(PriorityPredictor, dummy_config)
    fetcher.fetch_data.return_value = {"k": "v"}
    preparer.prepare.return_value = "prepared"
    ai_service.generate_response.return_value = 42

    pred.run_attribute_prediction()

    fetcher.fetch_data.assert_called_once_with()
    preparer.prepare.assert_called_once_with(fetcher.fetch_data.return_value)
    ai_service.generate_response.assert_called_once_with(preparer.prepare.return_value)
    modifier.modify.assert_called_once_with(fetcher.fetch_data.return_value, ai_service.generate_response.return_value)


def test_priority_predictor_description(dummy_config):
    assert "Priority Predictor" in PriorityPredictor.get_description()


def test_queue_predictor_prints(monkeypatch, dummy_config):
    pred, *_ = make_predictor(QueuePredictor, dummy_config)
    print_mock = MagicMock()
    monkeypatch.setattr(builtins, "print", print_mock)
    pred.run_attribute_prediction()
    print_mock.assert_called_once_with("Running queue prediction...")


def test_queue_predictor_description():
    assert "Queue Predictor" in QueuePredictor.get_description()
