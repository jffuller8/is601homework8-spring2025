"""Test command pattern implementation"""
import pytest
from calculator.commands import (
    Command, AddCommand, SubtractCommand,
    MultiplyCommand, DivideCommand
)

def test_abstract_execute():
    """Test that execute method is abstract"""
    class TestCommand(Command):
        pass
        
    with pytest.raises(TypeError):
        TestCommand()

def test_add_command():
    """Test add command"""
    command = AddCommand(5, 3)
    assert command.execute() == 8
    assert command.a == 5
    assert command.b == 3

def test_subtract_command():
    """Test subtract command"""
    command = SubtractCommand(5, 3)
    assert command.execute() == 2
    assert command.a == 5
    assert command.b == 3

def test_multiply_command():
    """Test multiply command"""
    command = MultiplyCommand(5, 3)
    assert command.execute() == 15
    assert command.a == 5
    assert command.b == 3

def test_divide_command():
    """Test divide command"""
    command = DivideCommand(6, 2)
    assert command.execute() == 3
    assert command.a == 6
    assert command.b == 2

def test_divide_by_zero_command():
    """Test divide by zero raises error"""
    command = DivideCommand(5, 0)
    with pytest.raises(ZeroDivisionError):
        command.execute()

def test_command_abstract_class():
    """Test that Command class is abstract"""
    with pytest.raises(TypeError):
        Command()