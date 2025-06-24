import logging
import pytest

from open_ticket_ai.src.ce.core.config.config_models import AIInferenceServiceConfig
from open_ticket_ai.src.ce.run.ai_models.ai_inference_service import AIInferenceService
from open_ticket_ai.src.ce.run.ai_models.hf_local_ai_inference_service import HFAIInferenceService


class DummyService(AIInferenceService):
    """Simple subclass used for testing."""

    def generate_response(self, prompt: str) -> str:
        return f"dummy:{prompt}"


@pytest.fixture
def example_config():
    return AIInferenceServiceConfig(id="dummy", provider_key="dummy_provider")


def test_ai_inference_service_is_abstract(example_config):
    with pytest.raises(TypeError):
        AIInferenceService(example_config)  # type: ignore[abstract]


def test_subclass_initialization_assigns_config(example_config):
    svc = DummyService(example_config)
    assert svc.ai_inference_config is example_config
    assert isinstance(svc._logger, logging.Logger)
    assert svc.generate_response("hi") == "dummy:hi"


def test_hf_service_description():
    assert (
        HFAIInferenceService.get_description()
        == "Hugging Face AI Model - Placeholder for future implementation"
    )


def test_hf_service_generate_response_returns_none(example_config):
    svc = HFAIInferenceService(example_config)
    assert svc.generate_response("hello") is None
