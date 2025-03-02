"""Division plugin"""
from .plugin_base import CalculatorPlugin

class DividePlugin(CalculatorPlugin):
    def get_command(self):
        return "divide"
    
    def get_description(self):
        return "Divide first number by second"
    
    def execute(self, a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b