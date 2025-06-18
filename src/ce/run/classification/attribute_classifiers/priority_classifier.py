from src.ce.run.classification.base_classifier import BaseClassifier


class PriorityClassifier(BaseClassifier):
    """
    PriorityClassifier returns the priority ID (0=low,1=medium,2=high).
    """
    def __init__(
        self,
        model_name: str,
        subject_times: int = 3,
        max_length: int = 512,
    ):
        super().__init__(model_name, subject_times, max_length)
