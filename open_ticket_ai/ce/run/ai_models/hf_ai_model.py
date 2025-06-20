from open_ticket_ai.ce.run.ai_models.base_ai_model import BaseAIModel


class HFAIModel(BaseAIModel):
    """
    A class representing a Hugging Face AI model.

    This class is a placeholder for future implementation of Hugging Face AI model functionalities.
    Currently, it does not contain any methods or properties.
    """

    @staticmethod
    def get_description() -> str:
        return "Hugging Face AI Model - Placeholder for future implementation"

    def __init__(self, model_name: str):
        super().__init__(model_name)
