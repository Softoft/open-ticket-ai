from types import SimpleNamespace
from unittest.mock import MagicMock

from open_ticket_ai.src.ce.run.pipeline.context import PipelineContext
from open_ticket_ai.src.ce.run.pipeline.pipeline import Pipeline


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
