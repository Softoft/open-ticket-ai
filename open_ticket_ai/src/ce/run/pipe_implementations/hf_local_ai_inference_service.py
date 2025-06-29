# FILE_PATH: open_ticket_ai\src\ce\run\pipe_implementations\hf_local_ai_inference_service.py
from __future__ import annotations

import os


from open_ticket_ai.src.ce.core.config.config_models import RegistryInstanceConfig
from open_ticket_ai.src.ce.run.pipeline.context import PipelineContext
from open_ticket_ai.src.ce.run.pipeline.pipe import Pipe


class HFAIInferenceService(Pipe):
    """Run text classification locally using a Hugging Face model."""

    def __init__(self, config: RegistryInstanceConfig):
        """Initialize the service and load the Hugging Face model."""
        super().__init__(config)
        self.ai_inference_config = config

        params = config.params
        self.input_field: str = params.get("input_field", "prepared_data")
        self.result_field: str = params.get("result_field", "model_result")
        self.model_name: str = params["hf_model"]
        token_env = params.get("hf_token_env_var")
        token = os.getenv(token_env) if token_env else None

        from transformers import (
            AutoModelForSequenceClassification,
            AutoTokenizer,
            pipeline,
        )

        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name, token=token)
        model = AutoModelForSequenceClassification.from_pretrained(self.model_name, token=token)
        self._pipeline = pipeline(
            "text-classification",
            model=model,
            tokenizer=self.tokenizer,
        )

    def process(self, context: PipelineContext) -> PipelineContext:
        """Run inference on the configured input field and store the result."""
        text = context.data.get(self.input_field, "")
        result = self._pipeline(text)
        context.data[self.result_field] = result
        return context

    @staticmethod
    def get_description() -> str:
        """
        Provides a description of the service.

        Returns:
            str: Description text for the Hugging Face AI model service.
        """
        return "Hugging Face AI Model"
