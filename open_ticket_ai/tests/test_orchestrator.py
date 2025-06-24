from types import SimpleNamespace
from unittest.mock import MagicMock

import open_ticket_ai.src.ce.run.orchestrator as orchestrator_module
from open_ticket_ai.src.ce.run.orchestrator import Orchestrator
from open_ticket_ai.src.ce.run.pipeline.context import PipelineContext


def test_set_schedules_builds_and_schedules_pipelines(monkeypatch):
    pipeline_cfg = SimpleNamespace(id="p1", schedule=SimpleNamespace(interval=5, unit="minutes"))
    config = SimpleNamespace(pipelines=[pipeline_cfg])

    pipeline_instance = MagicMock()
    container = MagicMock(get_pipeline=MagicMock(return_value=pipeline_instance))

    every_result = SimpleNamespace()
    unit_result = MagicMock()
    setattr(every_result, pipeline_cfg.schedule.unit, MagicMock(return_value=unit_result))
    schedule_mock = MagicMock(every=MagicMock(return_value=every_result))
    monkeypatch.setattr(orchestrator_module, "schedule", schedule_mock)

    orch = Orchestrator(config, container)
    orch.set_schedules()

    container.get_pipeline.assert_called_once_with("p1")
    schedule_mock.every.assert_called_once_with(5)
    getattr(every_result, pipeline_cfg.schedule.unit).assert_called_once()
    unit_result.do.assert_called_once()
    call_args = unit_result.do.call_args.args
    assert call_args[0] == pipeline_instance.execute
    assert isinstance(call_args[1], PipelineContext)
