# FILE_PATH: open_ticket_ai\tests\src\run\test_ai_models.py
from unittest.mock import patch

import pytest

from open_ticket_ai.src.ce.core.config.config_models import AIInferenceServiceConfig
from open_ticket_ai.src.ce.run.pipe_implementations.hf_local_ai_inference_service import \
    HFAIInferenceService
from open_ticket_ai.src.ce.run.pipeline.pipe import Pipe
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
    """Tests the process method of DummyService.

    This test verifies that the DummyService correctly processes input context
    and sets the 'model_result' field in the context data.

    Steps:
        1. Initialize DummyService with example configuration
        2. Create PipelineContext with test data
        3. Process context through service
        4. Assert model_result matches expected format

    Args:
        example_config: Pytest fixture providing AI service configuration
    """
    svc = DummyService(example_config)
    ctx = PipelineContext(ticket_id="1", data={"prepared_data": "hi"})
    out = svc.process(ctx)
    assert out.data["model_result"] == "dummy:hi"


def test_hf_service_description():
    """Tests the get_description method of HFAIInferenceService.

    Verifies that the service description contains the expected "Hugging Face" identifier.
    This ensures the correct service type is being used in the pipeline.
    """
    assert "Hugging Face" in HFAIInferenceService.get_description()


def test_hf_service_process_returns_context(example_config):
    """Tests the process method of HFAIInferenceService.

    This test verifies that:
        1. The service correctly processes input context
        2. Returns a context containing model results
        3. Sets the model_result field appropriately

    Args:
        example_config: Pytest fixture providing AI service configuration
    """
    svc = HFAIInferenceService(example_config)
    ctx = PipelineContext(ticket_id="1", data={"prepared_data": "hi"})
    out = svc.process(ctx)
    assert out.data["model_result"] == "hi"
