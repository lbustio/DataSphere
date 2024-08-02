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

def main():
    """
    Main function to parse command-line arguments and execute the corresponding actions.
    It exits with the code returned by `execute_commands`.
    If no command is provided, it defaults to loading data and visualizing it.
    """
    if len(sys.argv) == 1:
        # Default action if no command is provided
        default_data_path = os.path.join('data', 'raw', 'sample.csv')
        sys.argv.append(f'load_data={default_data_path}')
        sys.argv.append('visualize=table_viewer')

    try:
        args = parse_arguments()
        exit_code = execute_commands(args)
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        exit_code = 1

    sys.exit(exit_code)

if __name__ == '__main__':
    main()
