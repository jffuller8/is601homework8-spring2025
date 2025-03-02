"""Test REPL functionality"""
from calculator.repl import CalculatorREPL
from unittest.mock import patch

def test_repl_initialization():
    """Test REPL initializes with correct commands"""
    repl = CalculatorREPL()
    assert 'add' in repl.plugins
    assert 'subtract' in repl.plugins
    assert 'multiply' in repl.plugins
    assert 'divide' in repl.plugins

def test_plugins_execution():
    """Test plugins execute correctly"""
    repl = CalculatorREPL()
    result = repl.plugins['add'].execute(5, 3)
    assert result == 8

def test_exit_repl():
    """Test exit functionality"""
    repl = CalculatorREPL()
    assert repl.running is True
    repl.exit_repl()
    assert repl.running is False

def test_show_menu(capsys):
    """Test menu display"""
    repl = CalculatorREPL()
    repl.show_menu()
    captured = capsys.readouterr()
    assert "Available Commands" in captured.out
    assert "add" in captured.out
    assert "multiply" in captured.out
    assert "divide" in captured.out

@patch('builtins.input')
def test_run_calculations(mock_input):
    """Test REPL with multiple operations"""
    mock_input.side_effect = [
        'add', '5', '3',      # Add operation
        'exit'                # Exit command
    ]
    repl = CalculatorREPL()
    with patch('builtins.print'):  # Suppress output during test
        repl.run()
    assert not repl.running  # Verify REPL was stopped

@patch('builtins.input')
def test_invalid_operation(mock_input):
    """Test handling of invalid operations"""
    mock_input.side_effect = [
        'invalid',   # Invalid operation
        'exit'       # Exit command
    ]
    repl = CalculatorREPL()
    with patch('builtins.print'):
        repl.run()
    assert not repl.running

@patch('builtins.input')
def test_invalid_number(mock_input):
    """Test handling of invalid number input"""
    mock_input.side_effect = [
        'add', 'abc', '3',   # Invalid number input
        'exit'               # Exit command
    ]
    repl = CalculatorREPL()
    with patch('builtins.print'):
        repl.run()
    assert not repl.running