from unittest.mock import MagicMock

from open_ticket_ai.src.ce.run.pipeline.context import PipelineContext
from open_ticket_ai.src.ce.run.pipeline.pipe import Pipe
from open_ticket_ai.src.ce.run.pipeline.pipeline import Pipeline


def test_pipeline_executes_pipes_in_order():
    ctx1 = PipelineContext(ticket_id="T1")

    pipe1 = MagicMock(spec=Pipe)
    ctx2 = PipelineContext(ticket_id="T1", data={"step": 1})
    pipe1.process.return_value = ctx2

    pipe2 = MagicMock(spec=Pipe)
    ctx3 = PipelineContext(ticket_id="T1", data={"step": 2})
    pipe2.process.return_value = ctx3

    pipeline = Pipeline(config=MagicMock(), pipes=[pipe1, pipe2])

    result = pipeline.execute(ctx1)

    pipe1.process.assert_called_once_with(ctx1)
    pipe2.process.assert_called_once_with(ctx2)
    assert result == ctx3
