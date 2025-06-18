from src.ce.run.classification.attribute_classifiers.priority_classifier import PriorityClassifier
from src.ce.run.classification.attribute_classifiers.queue_classifier import QueueClassifier


class TicketClassifier:
    """
    Orchestrates both queue and priority predictions.
    """

    def __init__(
            self,
            queue_model_name: str,
            priority_model_name: str,
            subject_times: int = 2,
            max_length: int = 512,
    ):
        self.queue_clf = QueueClassifier(
            queue_model_name, subject_times, max_length
        )
        self.prio_clf = PriorityClassifier(
            priority_model_name, subject_times, max_length
        )

    def classify(self, ticket: dict) -> dict:
        """
        ticket: {"subject": str, "body": str}
        Returns {"queue": int, "priority": int}
        """
        return {
            "queue": self.queue_clf.classify(ticket),
            "priority": self.prio_clf.classify(ticket),
        }
