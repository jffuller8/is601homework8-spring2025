"""Multiplication plugin"""
from .plugin_base import CalculatorPlugin

class MultiplyPlugin(CalculatorPlugin):
    def get_command(self):
        return "multiply"
    
    def get_description(self):
        return "Multiply two numbers"
    
    def execute(self, a: float, b: float) -> float:
        return a * b