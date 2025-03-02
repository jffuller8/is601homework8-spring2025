"""Plugin loader implementation"""
import os
import importlib
import inspect
from .plugins.plugin_base import CalculatorPlugin

class PluginLoader:
    """Load calculator plugins dynamically"""
    
    @classmethod
    def load_plugins(cls):
        """Load all plugins from the plugins directory"""
        plugins = {}
        plugin_dir = os.path.join(os.path.dirname(__file__), 'plugins')
        
        # Get all .py files in plugins directory
        for filename in os.listdir(plugin_dir):
            if filename.endswith('.py') and not filename.startswith('__'):
                # Import the module
                module_name = f"calculator.plugins.{filename[:-3]}"
                module = importlib.import_module(module_name)
                
                # Find plugin classes in the module
                for name, obj in inspect.getmembers(module):
                    if (inspect.isclass(obj) and 
                        issubclass(obj, CalculatorPlugin) and 
                        obj != CalculatorPlugin):
                        # Instantiate the plugin
                        plugin = obj()
                        plugins[plugin.get_command()] = plugin
        
        return plugins