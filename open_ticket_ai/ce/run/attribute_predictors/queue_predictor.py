from open_ticket_ai.ce.run.attribute_predictors.attribute_predictor import AttributePredictor

class QueuePredictor(AttributePredictor):
    """
    QueuePredictor returns the queue ID (0–9).
    """

    @staticmethod
    def get_description() -> str:
        return "Queue Predictor - Predicts the queue of a ticket based on its attributes."

    def predict_attribute(self) -> str | int:
        pass

    def __init__(
            self,
    ):
        super().__init__()
