"""Base plugin interface"""
from abc import ABC, abstractmethod

class CalculatorPlugin(ABC):
    """Abstract base class for calculator plugins"""
    
    @abstractmethod
    def get_command(self):
        """Return the command name"""
        pass
    
    @abstractmethod
    def get_description(self):
        """Return command description"""
        pass
    
    @abstractmethod
    def execute(self, a: float, b: float) -> float:
        """Execute the command"""
        pass