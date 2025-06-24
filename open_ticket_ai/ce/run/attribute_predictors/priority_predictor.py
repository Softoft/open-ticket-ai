from open_ticket_ai.ce.run.attribute_predictors.attribute_predictor import AttributePredictor


class PriorityPredictor(AttributePredictor):
    """
    PriorityPredictor returns the priority ID (0=low,1=medium,2=high).
    """

    def run_attribute_prediction(self):
        """Fetch data, run the model and apply the modifier."""

        fetched_data: dict = self.fetcher.fetch_data()
        prepared_data: str = self.preparer.prepare(fetched_data)
        result = self.ai_inference_service.generate_response(prepared_data)
        self.modifier.modify(fetched_data, result)

    @staticmethod
    def get_description() -> str:
        return "Priority Predictor - Predicts the priority of a ticket based on its attributes."
