from open_ticket_ai.ce.run.attribute_predictors.attribute_predictor import AttributePredictor

class PriorityPredictor(AttributePredictor):
    """
    PriorityPredictor returns the priority ID (0=low,1=medium,2=high).
    """

    def run_attribute_prediction(self):
        print("Running priority prediction...")

    @staticmethod
    def get_description() -> str:
        return "Priority Predictor - Predicts the priority of a ticket based on its attributes."

