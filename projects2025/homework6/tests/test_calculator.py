"""Tests calculator operations"""

from calculator import Calculator

def test_basic_operations():
    """Test all basic calculator operations"""
    assert Calculator.add(2, 2) == 4
    assert Calculator.subtract(4, 2) == 2
    assert Calculator.multiply(3, 3) == 9
    assert Calculator.divide(6, 2) == 3

def test_divide_by_zero():
    """Test division by zero error"""
    try:
        Calculator.divide(5, 0)
        assert False
    except ZeroDivisionError:
        assert True

def test_history():
    """Test calculation history"""
    Calculator._history.clear()  # Reset history # pylint: disable=W0212
    Calculator.add(2, 2)
    Calculator.multiply(3, 3)
    assert len(Calculator.get_history()) == 2
    assert Calculator.get_last_calculation() == "3 * 3 = 9"
