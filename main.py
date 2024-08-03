"""
Main entry point for the ClearData CLI application. It handles command-line
argument parsing through `cli_parser` and manages execution and exit codes.

Author: Lázaro Bustio Martínez
Date: 2024-08-01
Version: 1.0
Email: lbustio@gmail.com
"""

import sys
import os
from core.cli_parser import execute_commands, parse_arguments
from utils.file_utils import verify_folder_structure

def main():
    """
    Main function to parse command-line arguments and execute the corresponding actions.
    It exits with the code returned by `execute_commands`.
    If no command is provided, it defaults to loading data and visualizing it.
    """
    # Ensure the directory structure is in place before executing any commands
    verify_folder_structure()

    # Check if any command-line arguments are provided
    if len(sys.argv) == 1:
        # Default action if no command is provided: load data and visualize it
        default_data_path = os.path.join('data', 'raw', 'sample.csv')
        sys.argv.append(f'load_data={default_data_path}')
        sys.argv.append('visualize=table_viewer')

    try:
        # Parse the command-line arguments
        args = parse_arguments()
        # Execute the commands based on parsed arguments
        exit_code = execute_commands(args)
    except Exception as e:
        # Handle any exceptions that occur and print the error message
        print(f"An error occurred: {e}", file=sys.stderr)
        exit_code = 1  # Set exit code to 1 to indicate an error

    sys.exit(exit_code)  # Exit the program with the specified exit code

if __name__ == '__main__':
    main()  # Call the main function if this script is executed directly