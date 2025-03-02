"""Main program entry point"""
import os
from dotenv import load_dotenv
from calculator import Calculator
from calculator.repl import CalculatorREPL
from calculator.logger import logger

# Load environment variables
load_dotenv()

def validate_number(value):
    """Validate if a string can be converted to a number"""
    try:
        float(value)
        return True
    except ValueError:
        return False

def format_result(number):
    """Format number to remove .0 if it's a whole number"""
    return str(int(number)) if number.is_integer() else str(number)

def perform_calculation(a: str, b: str, operation: str) -> str:
    """Perform calculation and return formatted result string"""
    logger.info(f"Calculation requested: {a} {operation} {b}")
    
    # Validate input numbers
    if not validate_number(a) or not validate_number(b):
        logger.warning(f"Invalid number input: {a} or {b}")
        return f"Invalid number input: {a} or {b} is not a valid number."
    
    # Convert strings to numbers
    num_a = float(a)
    num_b = float(b)
    
    try:
        if operation == 'add':
            result = Calculator.add(num_a, num_b)
        elif operation == 'subtract':
            result = Calculator.subtract(num_a, num_b)
        elif operation == 'multiply':
            result = Calculator.multiply(num_a, num_b)
        elif operation == 'divide':
            result = Calculator.divide(num_a, num_b)
        else:
            logger.warning(f"Unknown operation: {operation}")
            return f"Unknown operation: {operation}"
        
        logger.debug(f"Calculation result: {result}")
        return f"The result of {a} {operation} {b} is equal to {format_result(result)}"
    except ZeroDivisionError as e:
        logger.error(f"Division by zero: {a}/{b}")
        return f"An error occurred: {str(e)}"
    except Exception as e:
        logger.exception(f"Error in calculation: {str(e)}")
        return f"An error occurred: {str(e)}"

def main():
    """Main function to run the calculator"""
    # Get calculator name from environment variable
    calculator_name = os.getenv("CALCULATOR_NAME", "Calculator")
    env_name = os.getenv("ENV_NAME", "production")
    
    logger.info(f"Starting {calculator_name} in {env_name} environment")
    
    # First run the original test calculations
    print(f"Running {calculator_name}:")
    print(perform_calculation("5", "3", "add"))
    print(perform_calculation("1", "0", "divide"))
    
    print("\nStarting interactive calculator:")
    # Then start the interactive REPL
    repl = CalculatorREPL()
    try:
        repl.run()
    except KeyboardInterrupt:
        logger.info("Calculator terminated by user")
    except Exception as e:
        logger.exception(f"Unexpected error: {str(e)}")
    finally:
        logger.info("Calculator program ended")

if __name__ == "__main__":
    main()