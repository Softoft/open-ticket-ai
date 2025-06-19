from src.ce.run.classification.base_classifier import BaseClassifier


class QueueClassifier(BaseClassifier):
    """
    QueueClassifier returns the queue ID (0–9).
    """
    def __init__(
        self,
        model_name: str,
        subject_times: int = 3,
        max_length: int = 512,
    ):
        super().__init__(model_name, subject_times, max_length)