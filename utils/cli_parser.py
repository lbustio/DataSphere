"""
Module for parsing command-line arguments and executing commands in the ClearData CLI.

Author: Lázaro Bustio Martínez
Date: 2024-08-01
Version: 1.0
Email: lbustio@gmail.com
"""


import argparse
from core.plugin_manager import PluginManager
from utils.logging_config import logger
from utils.strings_utils import get_file_extension

# Instantiate the PluginManager
plugin_manager = PluginManager()


def parse_arguments():
    """
    Parses command-line arguments for the ClearData CLI.

    Defines subcommands for loading data (`load_data`), saving data (`save_data`), and running plugins (`run_plugin`).

    Returns:
        argparse.Namespace: The parsed command-line arguments.
    """

    parser = argparse.ArgumentParser(description='ClearData CLI')
    subparsers = parser.add_subparsers(dest='command')

    # Subcommand for loading data
    parser_load = subparsers.add_parser('load_data', help='Load data from file')
    parser_load.add_argument('path', type=str, help='Path to the data file')

    # Subcommand for saving data
    parser_save = subparsers.add_parser('save_data', help='Save data to file')
    parser_save.add_argument('path', type=str, help='Path to save the data file')
    parser_save.add_argument('data', type=str, help='Data to save')

    # Subcommand for running plugins
    parser_run = subparsers.add_parser('run_plugin', help='Run a plugin')
    parser_run.add_argument('name', type=str, help='Name of the plugin')
    parser_run.add_argument('params', type=str, help='Parameters for the plugin')

    return parser.parse_args()


def execute_command(args):
    """
    Executes the command based on the parsed arguments.

    Handles the 'load_data', 'save_data', and 'run_plugin' commands. If the command is not recognized,
    it logs an error.

    Args:
        args (argparse.Namespace): The parsed command-line arguments.

    Returns:
        int: An exit code (0 for success, 1 for error).
    """
    try:
        if args.command == 'load_data':
            # Get the file extension
            file_extension = get_file_extension(args.path)
            
            # Determine the appropriate plugin to use
            plugin_name = f"{file_extension}_loader"
            
            # Load the plugin
            plugin_manager.load_plugin('data_io', plugin_name)
            
            # Get the plugin instance
            plugin = plugin_manager.get_plugin(plugin_name)
            
            if plugin:
                # Call the plugin's method for loading data
                result = plugin.load(args.path)
            else:
                #logger.error(f"Plugin '{plugin_name}' not found.")
                return 1

        elif args.command == 'save_data':
            # result = save_data(args.path, args.data)  
            # TODO: Implement save_data functionality
            logger.info(f"Data saved successfully: {result}")  # Placeholder log

        elif args.command == 'run_plugin':
            # result = run_plugin(args.name, args.params) 
            # TODO: Implement run_plugin functionality
            logger.info(f"Plugin run successfully: {result}")  # Placeholder log

        else:
            logger.error("Unknown command. Please use 'load_data', 'save_data', or 'run_plugin'.")
            return 1

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
