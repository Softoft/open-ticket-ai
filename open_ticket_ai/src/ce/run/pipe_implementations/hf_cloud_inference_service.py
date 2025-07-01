from __future__ import annotations

import os
from typing import Optional

from huggingface_hub import get_inference_endpoint

from open_ticket_ai.src.ce.core.config.config_models import ProvidableConfig
from open_ticket_ai.src.ce.run.pipeline.context import PipelineContext
from open_ticket_ai.src.ce.run.pipeline.pipe import Pipe


class HFCloudInferenceService(Pipe):
    """Run inference on a Hugging Face Inference Endpoint."""

    def __init__(self, config: ProvidableConfig) -> None:
        super().__init__(config)
        params = config.params
        self.input_field: str = params.get("input_field", "prepared_data")
        self.result_field: str = params.get("result_field", "model_result")
        endpoint_identifier: str = params["hf_endpoint_name"]
        token_env: Optional[str] = params.get("hf_token_env_var")
        token = os.getenv(token_env) if token_env else None

        namespace: Optional[str] = None
        name = endpoint_identifier
        if "/" in endpoint_identifier:
            namespace, name = endpoint_identifier.split("/", 1)

        endpoint = get_inference_endpoint(name, namespace=namespace, token=token)
        self._client = endpoint.client

    def process(self, context: PipelineContext) -> PipelineContext:
        text = context.data.get(self.input_field, "")
        result = self._client.text_classification(text)
        context.data[self.result_field] = result
        return context

    @staticmethod
    def get_description() -> str:
        return "Hugging Face Inference Endpoint"
