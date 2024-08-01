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
from utils.logging_config import logger
from utils.cli_parser import execute_command, parse_arguments
from utils.file_utils import print_directory_structure, parse_gitignore

def main():
    """
    Main function to parse command-line arguments and execute the corresponding actions.
    It exits with the code returned by `execute_command`.
    If no command is provided, it defaults to loading data from a sample CSV file.
    """
    working_folder = os.getcwd()
    # gitignore_path = '.gitignore'
    # ignore_patterns = parse_gitignore(gitignore_path)

    # print(f"{working_folder}/")
    # print_directory_structure(working_folder, ignore_patterns)

    if len(sys.argv) == 1:
        # Default action if no command is provided
        sys.argv.extend(['load_data', 'data/raw/sample.csv'])

    args = parse_arguments()
    exit_code = execute_command(args)
    sys.exit(exit_code)

if __name__ == '__main__':
    main()