"""
Module for managing plugins in the ClearData CLI.

Author: Lázaro Bustio Martínez
Date: 2024-08-01
Version: 1.0
Email: lbustio@gmail.com
"""

from core.logging_config import logger
import importlib.util

class PluginManager:
    """
    Manages loading, removing, and retrieving plugins.

    Attributes:
        plugins (dict): A dictionary to store loaded plugin instances by name.
    """

    def __init__(self):
        """Initializes the PluginManager with an empty dictionary of plugins."""
        self.plugins = {}

    def load_plugin(self, plugin_type, plugin_name):
        """
        Loads a plugin of a specific type.

        Args:
            plugin_type (str): The type of the plugin (e.g., 'data_io').
            plugin_name (str): The name of the plugin to load.

        Raises:
            ModuleNotFoundError: If the plugin module cannot be found.
            AttributeError: If the plugin class cannot be found in the module.
            Exception: For other unexpected errors during plugin loading.
        """

        module_path = f"plugins.{plugin_type}.{plugin_name}"
        
        try:
            # Log the attempt to load the plugin
            logger.info(f"Attempting to load plugin '{plugin_name}' of type '{plugin_type}' from '{module_path}'.")

            # Import the plugin module dynamically
            spec = importlib.util.find_spec(module_path)
            if spec is None:
                raise ModuleNotFoundError(f"Module '{module_path}' not found.")

            # Get the file location of the module (for debugging)
            file_location = spec.origin if spec.origin else f"Unknown location for plugin '{module_path}'"
            logger.info(f"Plugin {plugin_name} located at: '{file_location}'")

            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            
            # Retrieve the plugin class from the module
            plugin_class = getattr(module, plugin_name)

            # Create an instance of the plugin class and store it
            current_plugin = plugin_class()
            self.plugins[plugin_name] = current_plugin 
            logger.info(f"Plugin '{plugin_name}' of type '{plugin_type}' loaded successfully.")
            
        except ModuleNotFoundError as e:
            logger.error(f"Error loading the plugin '{plugin_name}' in type '{plugin_type}': {str(e)}")
        except AttributeError as e:
            logger.error(f"Error: Plugin class '{plugin_name.capitalize()}' not found in module '{plugin_name}'. Error loading plugin '{plugin_name}': {str(e)}")
        except Exception as e:
            logger.error(f"Error loading plugin '{plugin_name}': {str(e)}")

    def remove_plugin(self, plugin_name):
        """
        Removes a loaded plugin.

        Args:
            plugin_name (str): The name of the plugin to remove.

        Raises:
            KeyError: If the plugin is not found in the loaded plugins.
        """

        if plugin_name in self.plugins:
            del self.plugins[plugin_name]
            logger.info(f"Plugin '{plugin_name}' removed successfully.")
        else:
            logger.error(f"Error: Plugin '{plugin_name}' is not loaded.")

    def get_plugin(self, plugin_name):
        """
        Retrieves a loaded plugin instance.

        Args:
            plugin_name (str): The name of the plugin to retrieve.

        Returns:
            object: The plugin instance if found, None otherwise.
        """

        plugin = self.plugins.get(plugin_name, None)
        if plugin:
            logger.info(f"Plugin '{plugin_name}' retrieved successfully.")
        else:
            logger.warning(f"Plugin '{plugin_name}' not found.")
        return plugin
