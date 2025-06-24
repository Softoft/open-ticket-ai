from types import SimpleNamespace
from unittest.mock import MagicMock

from open_ticket_ai.src.ce.run.pipeline import (
    Pipeline,
    PipelineContext,
    DataPreparerPipe,
    AIInferencePipe,
    ModifierPipe,
)


class DummyPreparer:
    def prepare(self, data):
        return f"prep({data['v']})"


class DummyAI:
    def generate_response(self, prompt):
        return f"ai:{prompt}"


class DummyModifier:
    def __init__(self):
        self.called_with = None

    def modify(self, ticket_id: str, model_result):
        self.called_with = (ticket_id, model_result)
        return "done"


def test_pipeline_executes_in_order():
    preparer = DummyPreparer()
    ai = DummyAI()
    modifier = DummyModifier()

    pipeline = Pipeline([
        DataPreparerPipe(preparer),
        AIInferencePipe(ai),
        ModifierPipe(modifier),
    ])

    context = PipelineContext(ticket_id="T99", data={"v": 1})
    result = pipeline.execute(context)

    assert result.prepared_data == "prep(1)"
    assert result.model_result == "ai:prep(1)"
    assert modifier.called_with == ("T99", "ai:prep(1)")
