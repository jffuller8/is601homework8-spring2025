"""Command Pattern Implementation for Calculator"""
from abc import ABC, abstractmethod
from calculator.calculation import Calculator

class Command(ABC):
    """Abstract command class"""
    @abstractmethod
    def execute(self):
        """Execute the command"""
        pass

class AddCommand(Command):
    """Command for addition"""
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        return Calculator.add(self.a, self.b)

class SubtractCommand(Command):
    """Command for subtraction"""
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        return Calculator.subtract(self.a, self.b)

class MultiplyCommand(Command):
    """Command for multiplication"""
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        return Calculator.multiply(self.a, self.b)

class DivideCommand(Command):
    """Command for division"""
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        return Calculator.divide(self.a, self.b)