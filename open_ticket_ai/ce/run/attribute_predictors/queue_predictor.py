from open_ticket_ai.ce.run.attribute_predictors.attribute_predictor import AttributePredictor

class QueuePredictor(AttributePredictor):
    """
    QueuePredictor returns the queue ID (0–9).
    """

    def run_attribute_prediction(self):
        """Run the queue prediction pipeline."""

        print("Running queue prediction...")

    @staticmethod
    def get_description() -> str:
        return "Queue Predictor - Predicts the queue of a ticket based on its attributes."

