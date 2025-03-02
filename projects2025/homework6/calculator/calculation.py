"""Calculator class implementation with history tracking"""

from .operations import add, subtract, multiply, divide

class Calculator:
    """Calculator class with static methods for operations and calculation history"""
    _history = []

    @staticmethod
    def add(a: float, b: float) -> float:
        """Add two numbers and store in history"""
        result = add(a, b)
        Calculator._add_to_history(f"{a} + {b} = {result}")
        return result

    @staticmethod
    def subtract(a: float, b: float) -> float:
        """Subtract numbers and store in history"""
        result = subtract(a, b)
        Calculator._add_to_history(f"{a} - {b} = {result}")
        return result

    @staticmethod
    def multiply(a: float, b: float) -> float:
        """Multiply numbers and store in history"""
        result = multiply(a, b)
        Calculator._add_to_history(f"{a} * {b} = {result}")
        return result

    @staticmethod
    def divide(a: float, b: float) -> float:
        """Divide numbers and store in history"""
        result = divide(a, b)
        Calculator._add_to_history(f"{a} / {b} = {result}")
        return result

    @classmethod
    def _add_to_history(cls, calculation: str) -> None:
        """Add calculation to history"""
        cls._history.append(calculation)

    @classmethod
    def get_history(cls) -> list:
        """Get all calculations history"""
        return cls._history

    @classmethod
    def get_last_calculation(cls) -> str:
        """Get most recent calculation"""
        return cls._history[-1] if cls._history else None # pylint: disable=C0304
          