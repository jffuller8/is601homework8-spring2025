"""Test record generation"""
from calculator import Calculator
import pytest

def test_generate_records(num_records):
    """Test generating multiple calculator records"""
    # Clear existing history
    Calculator._history.clear()
    
    # Generate records using different operations
    for i in range(num_records):
        Calculator.add(i, 1)
        Calculator.subtract(i, 1)
        Calculator.multiply(i, 2)
        if i != 0:  # Avoid divide by zero
            Calculator.divide(i, 1)
    
    # Get and display history
    history = Calculator.get_history()
    print(f"\nGenerated {len(history)} records:")
    for record in history:
        print(record)
    
    # Verify records were created
    assert len(history) > 0