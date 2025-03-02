"""Subtraction plugin"""
from .plugin_base import CalculatorPlugin

class SubtractPlugin(CalculatorPlugin):
    def get_command(self):
        return "subtract"
    
    def get_description(self):
        return "Subtract second number from first"
    
    def execute(self, a: float, b: float) -> float:
        return a - b