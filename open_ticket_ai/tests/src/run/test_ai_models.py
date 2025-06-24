from unittest.mock import patch

import pytest

from open_ticket_ai.src.ce.core.config.config_models import AIInferenceServiceConfig
from open_ticket_ai.src.ce.run.pipeline.pipe import Pipe
from open_ticket_ai.src.ce.run.ai_models.hf_local_ai_inference_service import (
    HFAIInferenceService,
)
from open_ticket_ai.src.ce.run.pipeline.context import PipelineContext


class DummyService(Pipe):
    """A dummy service for testing that simulates an AI inference service.

    This class extends the Pipe abstract base class and implements a simple
    process method that generates a dummy result based on input context.

    Attributes:
        ai_inference_config: Configuration for the dummy service.
    """

    def __init__(self, cfg):
        """Initializes the DummyService with given configuration.

        Args:
            cfg: Configuration object for the service.
        """
        super().__init__(cfg)
        self.ai_inference_config = cfg

    def process(self, context: PipelineContext) -> PipelineContext:
        """Processes input context by generating a dummy model result.

        Args:
            context: The pipeline context containing input data.

        Returns:
            PipelineContext: Updated context with dummy model result added.
        """
        context.data["model_result"] = f"dummy:{context.data.get('prepared_data')}"
        return context


@pytest.fixture
def example_config():
    """Fixture providing a dummy AI inference service configuration.

    Returns:
        AIInferenceServiceConfig: Configuration instance for testing.
    """
    return AIInferenceServiceConfig(id="dummy", provider_key="dummy_provider")


def test_service_process_sets_result(example_config):
    """Tests that DummyService correctly sets model_result in context."""
    svc = DummyService(example_config)
    ctx = PipelineContext(ticket_id="1", data={"prepared_data": "hi"})
    out = svc.process(ctx)
    assert out.data["model_result"] == "dummy:hi"


def test_hf_service_description():
    """Tests that Hugging Face service description contains expected text."""
    assert "Hugging Face" in HFAIInferenceService.get_description()


def test_hf_service_process_returns_context(example_config):
    """Tests that Hugging Face service returns context with model result."""
    svc = HFAIInferenceService(example_config)
    ctx = PipelineContext(ticket_id="1", data={"prepared_data": "hi"})
    out = svc.process(ctx)
    assert out.data["model_result"] == "hi"