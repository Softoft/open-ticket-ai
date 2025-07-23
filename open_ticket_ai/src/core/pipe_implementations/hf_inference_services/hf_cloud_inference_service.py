from __future__ import annotations

from open_ticket_ai.src.core.config.config_models import ProvidableConfig
from open_ticket_ai.src.core.pipe_implementations.ai_text_model_input import TextAIModelInput
from open_ticket_ai.src.core.pipeline.context import PipelineContext
from open_ticket_ai.src.core.pipeline.pipe import Pipe


class HFLocalAIInferenceService(Pipe[TextAIModelInput,]):
    """A Hugging Face local AI inference service implementation.

    This class provides functionality to run inference using Hugging Face models
    locally. It processes text inputs from pipeline context data and stores
    inference results back in the context.

    Attributes:
        ai_inference_config (ProvidableConfig): Configuration for the service.
        input_field (str): Key in context data for input text.
        result_field (str): Key in context data to store inference results.
        model_name (str): Name of the Hugging Face model to use.
    """

    def __init__(self, config: ProvidableConfig):
        """Initializes the Hugging Face local inference service.

        Args:
            config (ProvidableConfig): Configuration instance containing service parameters.
        """

        super().__init__(config)
        self.ai_inference_config = config

        params = config.params
        self.input_field: str = params.get("input_field", "prepared_data")
        self.result_field: str = params.get("result_field", "model_result")
        self.model_name: str = params["hf_model"]
        token_env = params.get("hf_token_env_var")


    def process(self, context: PipelineContext) -> PipelineContext:
        """Processes pipeline context by running Hugging Face model inference.

        Retrieves input text from context data, runs model inference, and stores
        the result back in context data under the configured result field.

        Args:
            context (PipelineContext): Pipeline context containing data to process.

        Returns:
            PipelineContext: Updated context with inference results stored.

        Raises:
            KeyError: If the input field is missing from context data.
        """
        text = context.data.get(self.input_field, "")
        context.data[self.result_field] = result
        return context

    @staticmethod
    def get_description() -> str:
        """Provides a description of the service.

        Returns:
            str: Description text for the Hugging Face AI model service.
        """
        return "Hugging Face AI Cloud Model"
