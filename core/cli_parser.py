"""
Module for parsing command-line arguments and executing commands in the DataSphere CLI.

Author: Lázaro Bustio Martínez
Date: 2024-08-01
Version: 1.0
Email: lbustio@gmail.com
"""

import argparse
import pandas as pd
from core.plugin_manager import PluginManager
from core.logging_config import logger
from utils.strings_utils import get_file_extension
from utils.file_utils import validate_file_path

# Instantiate the PluginManager
plugin_manager = PluginManager()

# Global variable to keep track of the state
state = {
    'data_loaded': False,
    'data': None,
    'analysis_results': None
}

def parse_arguments():
    """
    Parses command-line arguments for the DataSphere CLI.
    
    Parses arguments in the format `command=value` for flexibility.
    
    Returns:
        dict: The parsed command-line arguments as a dictionary.
    """
    parser = argparse.ArgumentParser(description='DataSphere CLI')
    parser.add_argument('commands', type=str, help='Commands in the format command=value')

    args = parser.parse_args()
    
    # Split commands based on '=' and parse them
    command_list = args.commands.split(' ')
    parsed_commands = {}
    for command in command_list:
        if '=' in command:
            cmd, value = command.split('=', 1)
            parsed_commands[cmd.lower()] = value

    return parsed_commands

def execute_commands(commands):
    """
    Executes commands in sequence, ensuring dependencies are met.
    
    Args:
        commands (dict): The parsed command-line arguments as a dictionary.
    
    Returns:
        int: An exit code (0 for success, 1 for error).
    """
    try:
        # Load data command
        if 'load_data' in commands:
            path = commands['load_data'].lower()
            if not validate_file_path(path):
                logger.error(f"File path '{path}' is invalid.")
                return 1
            file_extension = get_file_extension(path)
            plugin_name = f"{file_extension}_loader"
            plugin_manager.load_plugin('data_io', plugin_name)
            plugin = plugin_manager.get_plugin(plugin_name)
            if plugin:
                if file_extension == 'xlsx':
                    sheet_name = commands.get('sheet_name')  # Get the sheet name if provided
                    # Set configuration for the plugin
                    plugin._config['sheet_name'] = sheet_name or 0  # Default to the first sheet
                state['data'] = plugin.load(path)
                if state['data'] is None:
                    logger.error("Failed to load data.")
                    return 1
                state['data_loaded'] = True
                logger.info("Data loaded successfully.")
            else:
                logger.error(f"Plugin '{plugin_name}' not found.")
                return 1
        
        if 'visualize' in commands:
            if not state['data_loaded']:
                logger.error("Data must be loaded before visualization.")
                return 1
            
            plugin_name = commands['visualize'].lower()
            plugin_manager.load_plugin('visualization', plugin_name)
            plugin = plugin_manager.get_plugin(plugin_name)
            if plugin:
                max_row = int(commands.get('max_row', 10))  # Default to 10 if not specified
                row_selection = commands.get('row_selection', 'top')  # Default to 'top' if not specified
                class_column = commands.get('class_column')  # This is optional
                class_value = commands.get('class_value')  # New parameter for by_class command

                # Set configuration for the plugin
                plugin._config['max_rows'] = max_row
                plugin._config['row_selection'] = row_selection
                
                # Call the visualize method with the correct arguments
                plugin.visualize(state['data'], class_column, class_value)
                logger.info("Data visualization completed.")
            else:
                logger.error(f"Plugin '{plugin_name}' not found.")
                return 1
        
        # Analysis command
        if 'analyze' in commands:
            if not state['data_loaded']:
                logger.error("Data must be loaded before analysis.")
                return 1

            plugin_name = commands.get('analyze')
            if not plugin_name:
                logger.error("An analysis plugin must be specified.")
                return 1
            plugin_manager.load_plugin('analysis', plugin_name)
            plugin = plugin_manager.get_plugin(plugin_name)
            if plugin:
                state['analysis_results'] = plugin.analyze(state['data'])
                if state['analysis_results'] is None:
                    logger.error("Analysis failed.")
                    return 1
                logger.info("Data analysis completed.")
            else:
                logger.error(f"Plugin '{plugin_name}' not found.")
                return 1
        
        # Save command
        if 'save' in commands:
            if state['analysis_results'] is None:
                logger.error("Results must be analyzed before saving.")
                return 1

            path = commands.get('save')
            if not path:
                logger.error("Save path must be specified.")
                return 1
            try:
                with open(path, 'w') as file:
                    file.write(str(state['analysis_results']))
                logger.info(f"Results saved to {path}.")
            except Exception as e:
                logger.error(f"Failed to save results: {e}")
                return 1
        
        # Help command
        if 'help' in commands:
            logger.info("Displaying help information.")
            if len(commands) > 1:
                command = list(commands.keys())[1]
                logger.info(f"Showing help for command: {command}")
                # Add specific help details for each command
            else:
                logger.info("Showing general help information.")
                logger.info("Available commands:")
                logger.info("  load_data=<path> [sheet_name=<name>] - Load data from the specified file path. Specify sheet name for XLSX files.")
                logger.info("  visualize=<plugin> [max_row=<number>] [row_selection=<top|bottom|random|by_class>] [class_column=<column>] [class_value=<value>] - Visualize data using the specified plugin.")
                logger.info("  analyze=<plugin> - Analyze data using the specified plugin.")
                logger.info("  save=<path> - Save analysis results to the specified file path.")
                logger.info("  help [command] - Show this help message or help for a specific command.")
            return 0

    except FileNotFoundError as e:
        logger.error(f"File not found: {e}")
        return 1
    except ValueError as e:
        logger.error(f"Value error: {e}")
        return 1
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        return 1

    return 0
