from types import SimpleNamespace
from unittest.mock import MagicMock

from pydantic import BaseModel

from open_ticket_ai.src.ce.run.orchestrator import Orchestrator
from open_ticket_ai.src.ce.run.pipeline import Pipeline


class DummyConfig(BaseModel):
    pass


def test_process_ticket_runs_pipeline():
    fetcher = MagicMock()
    fetcher.fetch_data.return_value = {"t": "data"}
    pipeline = MagicMock(spec=Pipeline)
    pipeline.execute.return_value = "result"

    container = SimpleNamespace(get_fetcher=lambda fid: fetcher)
    orch = Orchestrator(DummyConfig(), container)

    result = orch.process_ticket("T1", "fetcher_id", pipeline)

    fetcher.fetch_data.assert_called_once_with(ticket_id="T1")
    pipeline.execute.assert_called_once()
    assert result == "result"
