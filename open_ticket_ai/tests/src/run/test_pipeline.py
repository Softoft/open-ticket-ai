# FILE_PATH: open_ticket_ai\tests\src\run\test_pipeline.py
"""Module providing dummy implementations for pipeline components testing.

This module defines several classes that mimic the behavior of real pipeline components
(like data preparer, AI model, and result modifier) for the purpose of testing the pipeline
without the need for actual external services or complex setups.

The classes included are:

- `DummyPreparer`: Simulates data preparation by wrapping input values in a string.
- `DummyAI`: Simulates an AI model by returning formatted prompts as responses.
- `DummyModifier`: Simulates result modification and tracks call arguments.
"""



class DummyPreparer:
    """A dummy implementation of a data preparer for testing purposes.

    This class simulates the behavior of preparing input data by applying
    a simple transformation.
    """

    def prepare(self, data):
        """Transforms input data by wrapping a specific value in a string.

        Args:
            data (dict): Input data dictionary expected to contain a key 'v'.

        Returns:
            str: A formatted string containing the value from data['v'].
        """
        return f"prep({data['v']})"


class DummyAI:
    """A dummy implementation of an AI model for testing purposes.

    This class simulates the behavior of generating responses from prompts
    by returning a formatted version of the input prompt.
    """

    def generate_response(self, prompt):
        """Generates a simulated AI response based on the input prompt.

        Args:
            prompt (str): The input prompt for the AI model.

        Returns:
            str: A formatted string containing the input prompt.
        """
        return f"ai:{prompt}"


class DummyModifier:
    """A dummy implementation of a result modifier for testing purposes.

    This class simulates modifying model results and tracks the last arguments
    passed to the modify method.
    """

    def __init__(self):
        """Initializes the DummyModifier instance.

        Sets up an instance variable to track the last arguments used in modify calls.
        """
        self.called_with = None

    def modify(self, ticket_id: str, model_result):
        """Simulates modifying a model result and stores the input arguments.

        Args:
            ticket_id (str): Identifier for the ticket being processed.
            model_result (object): The result from the model that would be modified.

        Returns:
            str: A fixed string indicating completion.
        """
        self.called_with = (ticket_id, model_result)
        return "done"
