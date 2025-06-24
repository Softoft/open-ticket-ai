from open_ticket_ai.src.ce.run.modifiers.modifier import Modifier

class PriorityModifier(Modifier):
    """
    Modifier for changing the priority of a ticket.
    """

    @staticmethod
    def get_description() -> str:
        return "Modifies the priority of a ticket based on model predictions. " \
               "Accepts both string (e.g., 'High', 'Medium', 'Low') and integer (1, 2, 3) representations of priority."

    def modify(self, ticket_id: str, model_result: str | int) -> str | int:
        """
        Modify the priority of a ticket based on model prediction.

        Args:
            ticket_id: The ID of the ticket to modify
            model_result: The predicted priority level (could be string like "High"
                         or an integer like 1, 2, 3)

        Returns:
            str | int: The finalized priority level
        """
        # In a real implementation, additional validation or business rules might be applied here
        # For example, normalizing priority values, setting bounds, etc.

        return model_result

