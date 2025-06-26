"""
This is the main_module of example_package.

It contains a class and a function for demonstration purposes.
"""

class Greeter:
    """
    A class that greets you.

    Attributes:
        name (str): The name of the person to greet.
    """
    def __init__(self, name: str):
        """
        Initializes the Greeter.

        Args:
            name: The name to use in greetings.
        """
        self.name = name

    def greet(self, loud: bool = False) -> str:
        """
        Generates a greeting message.

        Args:
            loud: If True, the greeting will be in uppercase.
                  Defaults to False.

        Returns:
            The greeting message.
        """
        message = f"Hello, {self.name}!"
        return message.upper() if loud else message

def simple_math_operation(x: int, y: int, operation: str = "add") -> float:
    """
    Performs a simple math operation.

    Args:
        x: The first number.
        y: The second number.
        operation: The operation to perform. Can be "add", "subtract",
                   "multiply", or "divide". Defaults to "add".

    Returns:
        The result of the operation.

    Raises:
        ValueError: If the operation is invalid or division by zero occurs.
    """
    if operation == "add":
        return float(x + y)
    elif operation == "subtract":
        return float(x - y)
    elif operation == "multiply":
        return float(x * y)
    elif operation == "divide":
        if y == 0:
            raise ValueError("Cannot divide by zero.")
        return float(x / y)
    else:
        raise ValueError(f"Unknown operation: {operation}")