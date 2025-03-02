"""REPL Implementation with Plugin Support"""
from .plugin_loader import PluginLoader
from .logger import logger

class CalculatorREPL:
    def __init__(self):
        """Initialize with plugins"""
        logger.debug("Initializing Calculator REPL")
        self.plugins = PluginLoader.load_plugins()
        logger.info(f"Loaded plugins: {list(self.plugins.keys())}")
        self.running = True
    
    def show_menu(self):
        """Display available commands"""
        logger.debug("Showing menu")
        print("\nAvailable Commands:")
        print("------------------")
        for command, plugin in self.plugins.items():
            print(f"{command:<8} - {plugin.get_description()}")
        print("menu     - Show this menu")
        print("exit     - Quit the calculator")
    
    def exit_repl(self):
        """Exit the REPL"""
        logger.info("Exiting calculator")
        self.running = False
    
    def run(self):
        """Run the REPL"""
        logger.info("Starting REPL")
        print("Welcome to Calculator!")
        self.show_menu()
        
        while self.running:
            try:
                # Read
                command = input("\nEnter command: ").lower().strip()
                logger.debug(f"User entered command: {command}")
                
                if command == 'exit':
                    self.exit_repl()
                    continue
                elif command == 'menu':
                    self.show_menu()
                    continue
                
                if command not in self.plugins:
                    logger.warning(f"Unknown command: {command}")
                    print("Unknown command. Type 'menu' for available commands.")
                    continue
                
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                logger.debug(f"Operation: {command} {a} {b}")
                
                # Execute plugin
                result = self.plugins[command].execute(a, b)
                logger.info(f"Calculation result: {command}({a},{b}) = {result}")
                print(f"Result: {result}")
                
            except ValueError as e:
                logger.error(f"Invalid input: {str(e)}")
                print("Invalid number input. Please try again.")
            except ZeroDivisionError as e:
                logger.error(f"Division by zero error: {str(e)}")
                print("Error: Cannot divide by zero")
            except Exception as e:
                logger.exception(f"Unexpected error: {str(e)}")
                print(f"An error occurred: {str(e)}")