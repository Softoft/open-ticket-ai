from unittest.mock import patch

import pytest

from open_ticket_ai.src.ce.core.config.config_models import AIInferenceServiceConfig
from open_ticket_ai.src.ce.run.pipeline.pipe import Pipe
from open_ticket_ai.src.ce.run.ai_models.hf_local_ai_inference_service import (
    HFAIInferenceService,
)
from open_ticket_ai.src.ce.run.pipeline.context import PipelineContext


class DummyService(Pipe):
    def __init__(self, cfg):
        super().__init__(cfg)
        self.ai_inference_config = cfg

    def process(self, context: PipelineContext) -> PipelineContext:
        context.data["model_result"] = f"dummy:{context.data.get('prepared_data')}"
        return context


@pytest.fixture
def example_config():
    return AIInferenceServiceConfig(id="dummy", provider_key="dummy_provider")


def test_service_process_sets_result(example_config):
    svc = DummyService(example_config)
    ctx = PipelineContext(ticket_id="1", data={"prepared_data": "hi"})
    out = svc.process(ctx)
    assert out.data["model_result"] == "dummy:hi"


def test_hf_service_description():
    assert "Hugging Face" in HFAIInferenceService.get_description()


def test_hf_service_process_returns_context(example_config):
    svc = HFAIInferenceService(example_config)
    ctx = PipelineContext(ticket_id="1", data={"prepared_data": "hi"})
    out = svc.process(ctx)
    assert out.data["model_result"] == "hi"
