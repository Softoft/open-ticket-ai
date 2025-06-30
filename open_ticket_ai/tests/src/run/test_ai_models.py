# FILE_PATH: open_ticket_ai\tests\src\run\test_ai_models.py

import pytest
import sys

from unittest.mock import MagicMock, patch

from open_ticket_ai.src.ce.core.config.config_models import AIInferenceServiceConfig
from open_ticket_ai.src.ce.run.pipe_implementations.hf_local_ai_inference_service import (
    HFLocalAIInferenceService,
)
from open_ticket_ai.src.ce.run.pipeline.context import PipelineContext
from open_ticket_ai.src.ce.run.pipeline.pipe import Pipe


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
    return AIInferenceServiceConfig(
        id="dummy",
        provider_key="HFAIInferenceService",
        params={
            "input_field": "subject_body_combined",
            "hf_model": "dummy-model",
            "hf_token_env_var": "HF_TOKEN",
            "result_field": "queue_classification",
        },
    )


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
    """Tests the get_description method of HFLocalAIInferenceService.

    Verifies that the service description contains the expected "Hugging Face" identifier.
    This ensures the correct service type is being used in the pipeline.
    """
    assert "Hugging Face" in HFLocalAIInferenceService.get_description()


def test_hf_service_process_returns_context(example_config, monkeypatch):
    """Tests the process method of the Hugging Face AI inference service.

    This test verifies that:
        - The service correctly processes input context using Hugging Face transformers
        - Required dependencies (tokenizer, model) are initialized properly
        - The Hugging Face pipeline is called with expected parameters
        - Inference results are stored in the context at the configured field

    Steps:
        1. Mock Hugging Face components (tokenizer, model, pipeline)
        2. Set environment variable for Hugging Face token
        3. Initialize service with example configuration
        4. Process sample context through service
        5. Verify tokenizer/model initialization and pipeline calls
        6. Assert results are stored in context

    Args:
        example_config: Pytest fixture providing AI service configuration
        monkeypatch: Pytest fixture for modifying environment and attributes
    """
    fake_pipeline = MagicMock(return_value=[{"label": "A", "score": 0.9}])
    import types, importlib.machinery
    stub = types.ModuleType("openai")
    stub.__spec__ = importlib.machinery.ModuleSpec("openai", loader=None)
    monkeypatch.setitem(sys.modules, "openai", stub)
    with patch(
        "open_ticket_ai.src.ce.core.mixins.registry_providable_instance.pretty_print_config"
    ), patch(
        "transformers.AutoTokenizer.from_pretrained",
        return_value=MagicMock(),
    ) as tok, patch(
        "transformers.AutoModelForSequenceClassification.from_pretrained",
        return_value=MagicMock(),
    ) as model, patch(
        "transformers.pipelines.pipeline",
        return_value=fake_pipeline,
    ) as pipe:
        monkeypatch.setenv("HF_TOKEN", "t")
        svc = HFAIInferenceService(example_config)
        ctx = PipelineContext(
            ticket_id="1", data={"subject_body_combined": "hi"}
        )
        out = svc.process(ctx)

    tok.assert_called_once_with("dummy-model", token="t")
    model.assert_called_once_with("dummy-model", token="t")
    pipe.assert_called_once()
    assert out.data["queue_classification"] == fake_pipeline.return_value