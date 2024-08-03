"""
Module for parsing command-line arguments and executing commands in the DataSphere CLI.

This module handles command-line interface (CLI) operations for the DataSphere application. 
It parses user commands, loads data using plugins, visualizes data, performs analysis, 
and saves results. It uses the PluginManager to manage plugins and relies on utility 
functions for file validation and extension extraction.

Author: Lázaro Bustio Martínez
Date: 2024-08-01
Version: 1.0
Email: lbustio@gmail.com
"""

import argparse
from collections import defaultdict
from .plugin_manager import PluginManager
from .logging_config import logger
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

import argparse
from collections import defaultdict
import logging

# Configurar el logger
logger = logging.getLogger('DataSphere')

def parse_arguments():
    """
    Parses command-line arguments for the DataSphere CLI.
    
    Parses arguments in the format `command=value` for flexibility.
    
    Returns:
        dict: The parsed command-line arguments as a dictionary.
    """
    parser = argparse.ArgumentParser(description='DataSphere CLI')
    parser.add_argument('commands', type=str, help='Commands in the format command=value')

    try:
        args = parser.parse_args()
    except Exception as e:
        logger.error(f"Error parsing arguments: {e}", exc_info=True)
        return {}

    command_list = args.commands.split()

    parsed_commands = defaultdict(list)
    for command in command_list:
        try:
            if '=' in command:
                cmd, value = command.split('=', 1)
                parsed_commands[cmd.lower()].append(value)
            else:
                logger.warning(f"Ignoring invalid command format: {command}")
        except ValueError as e:
            logger.error(f"Error processing command '{command}': {e}" , exc_info=True)

    return dict(parsed_commands)



def execute_commands(commands):
    """
    Executes commands in sequence, ensuring dependencies are met.

    Args:
        commands (dict): The parsed command-line arguments as a dictionary.

    Returns:
        int: An exit code (0 for success, 1 for error).
    """
    try:
        # Initialize command execution state
        command_status = 0

        # Initialize the state dictionary if not already defined
        if 'state' not in globals():
            global state
            state = {
                'data': None,
                'data_loaded': False,
                'analysis_results': None
            }

        # Iterate over each command and execute
        for command, values in commands.items():
            if command == 'load_data':
                # Handle data loading
                for path in values:
                    path = path.lower()
                    if not validate_file_path(path):
                        logger.error(f"File path '{path}' is invalid.")
                        return 1
                    file_extension = get_file_extension(path)
                    plugin_name = f"{file_extension}_loader"
                    plugin_manager.load_plugin('data_io', plugin_name)
                    plugin = plugin_manager.get_plugin(plugin_name)
                    if plugin:
                        if file_extension == 'xlsx':
                            sheet_name = commands.get('sheet_name', [None])[0]
                            plugin._config['sheet_name'] = sheet_name or 0
                        state['data'] = plugin.load(path)
                        if state['data'] is None:
                            logger.error("Failed to load data.")
                            command_status = 1
                        else:
                            state['data_loaded'] = True
                            logger.info("Data loaded successfully.")
                    else:
                        logger.error(f"Plugin '{plugin_name}' not found.")
                        command_status = 1

            elif command == 'visualize':
                # Ensure data is loaded before visualization
                if not state.get('data_loaded', False):
                    logger.error("Data must be loaded before visualization.")
                    return 1

                # Handle multiple visualization plugins
                for plugin_names in values:
                    plugin_names = plugin_names.split(',')
                    for plugin_name in plugin_names:
                        plugin_name = plugin_name.strip().lower()
                        logger.info(f"Preparing to visualize data using plugin: '{plugin_name}'")

                        # Load and configure the visualization plugin
                        plugin_manager.load_plugin('visualization', plugin_name)
                        plugin = plugin_manager.get_plugin(plugin_name)
                        if plugin:
                            max_row = int(commands.get('max_row', [len(state['data'])])[0])
                            row_selection = commands.get('row_selection', ['top'])[0]
                            class_column = commands.get('class_column', [None])[0]
                            class_value = commands.get('class_value', [None])[0]
                            plugin._config['max_rows'] = max_row
                            plugin._config['row_selection'] = row_selection

                            # Call the visualize method
                            plugin.visualize(state['data'], class_column, class_value)
                            logger.info(f"Data visualization completed using {plugin_name}.")
                        else:
                            logger.error(f"Plugin '{plugin_name}' not found.")
                            command_status = 1

            elif command == 'analyze':
                # Ensure data is loaded before analysis
                if not state.get('data_loaded', False):
                    logger.error("Data must be loaded before analysis.")
                    return 1

                # Handle analysis
                for plugin_name in values:
                    if not plugin_name:
                        logger.error("An analysis plugin must be specified.")
                        command_status = 1
                    else:
                        logger.info(f"Preparing to analyze data using plugin: {plugin_name}")

                        plugin_manager.load_plugin('analysis', plugin_name)
                        plugin = plugin_manager.get_plugin(plugin_name)
                        if plugin:
                            state['analysis_results'] = plugin.analyze(state['data'])
                            if state['analysis_results'] is None:
                                logger.error("Analysis failed.")
                                command_status = 1
                            else:
                                logger.info("Data analysis completed.")
                        else:
                            logger.error(f"Plugin '{plugin_name}' not found.")
                            command_status = 1

            elif command == 'save':
                # Ensure analysis results are available before saving
                if state.get('analysis_results') is None:
                    logger.error("Results must be analyzed before saving.")
                    return 1

                # Handle saving results
                for path in values:
                    if not path:
                        logger.error("Save path must be specified.")
                        command_status = 1
                    else:
                        logger.info(f"Preparing to save results to path: {path}")
                        try:
                            with open(path, 'w') as file:
                                file.write(str(state['analysis_results']))
                            logger.info(f"Results saved to {path}.")
                        except Exception as e:
                            logger.error(f"Failed to save results: {e}")
                            command_status = 1

            elif command == 'help':
                # Display help information
                logger.info("Displaying help information.")
                if len(values) > 0:
                    for sub_command in values:
                        logger.info(f"Showing help for command: {sub_command}")
                        # Add specific help details for each command
                else:
                    logger.info("Showing general help information.")
                    logger.info("Available commands:")
                    logger.info("  load_data=<path> [sheet_name=<name>] - Load data from the specified file path. Specify sheet name for XLSX files.")
                    logger.info("  visualize=<plugin>[,<plugin>...] [max_row=<number>] [row_selection=<top|bottom|random|by_class>] [class_column=<column>] [class_value=<value>] - Visualize data using the specified plugins.")
                    logger.info("  analyze=<plugin> - Analyze data using the specified plugin.")
                    logger.info("  save=<path> - Save analysis results to the specified file path.")
                    logger.info("  help [command] - Show this help message or help for a specific command.")

            else:
                logger.error(f"Unknown command: {command}")
                command_status = 1

        return command_status

    except FileNotFoundError as e:
        logger.error(f"File not found: {e}")
        return 1
    except ValueError as e:
        logger.error(f"Value error: {e}")
        return 1
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        return 1

