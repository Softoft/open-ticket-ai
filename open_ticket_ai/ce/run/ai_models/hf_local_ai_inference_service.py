from open_ticket_ai.ce.run.ai_models.ai_inference_service import AIInferenceService


class HFAIInferenceService(AIInferenceService):
    """
    A class representing a Hugging Face AI model.

    This class is a placeholder for future implementation of Hugging Face AI model functionalities.
    Currently, it does not contain any methods or properties.
    """

    def generate_response(self, prompt: str) -> str:
        pass

    @staticmethod
    def get_description() -> str:
        return "Hugging Face AI Model - Placeholder for future implementation"
