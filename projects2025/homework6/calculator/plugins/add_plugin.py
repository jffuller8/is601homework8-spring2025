"""Addition plugin"""
from .plugin_base import CalculatorPlugin

class AddPlugin(CalculatorPlugin):
    def get_command(self):
        return "add"
    
    def get_description(self):
        return "Add two numbers"
    
    def execute(self, a: float, b: float) -> float:
        return a + b