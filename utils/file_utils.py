"""
Module: utils.file_utils

Author: Lázaro Bustio Martínez
Date: 2024-08-01
Version: 1.0
Email: lbustio@gmail.com

Description:
This module provides utility functions for file handling. The `validate_file_path` function checks if a given file path refers to a file that exists and is readable. This ensures that operations on the file can proceed without encountering file-related errors.

"""

import os
import fnmatch
from core.logging_config import logger

def validate_file_path(path):
    """
    Validates if the file exists and is readable.

    This function checks whether the specified file path refers to a file that exists and whether it has read permissions. It is useful for ensuring that a file can be accessed before performing operations on it.

    Args:
        path (str): The path to the file. This should be a string representing the file's location in the filesystem.

    Returns:
        bool: True if the file exists and is readable, otherwise False.

    Raises:
        ValueError: If `path` is not a valid string or is empty.

    Example:
        >>> validate_file_path('/path/to/file.txt')
        True
        
        >>> validate_file_path('/path/to/nonexistent_file.txt')
        False
    """

    # Validate that path is a non-empty string
    if not isinstance(path, str) or not path.strip():
        raise ValueError("The file path must be a non-empty string.")
    
    # Check if the path refers to an existing file and if it is readable
    if os.path.isfile(path) and os.access(path, os.R_OK):
        return True
    else:
        return False

# The function now includes validation for the input `path`, 
# ensuring that only valid paths are processed and preventing potential errors.


def verify_folder_structure():
    """
    Ensure the working directory has the required folder structure.
    Create any missing directories and log the process.
    """
    
    # List of required folders for the project structure
    required_folders = [
        'core',                     # Core functionality and main logic of the application. 
        'data',                     # Folder containing all data files used in the project. 
        'data/raw',                 # Raw, unprocessed data files. 
        'data/processed',           # Data that has been cleaned or transformed for analysis. 
        'results',                  # Folder to store the results of analyses, model outputs, or other computations. 
        'results/visualization',    # Subfolder for storing visualizations generated from results. 
        'logs',                     # Logs for tracking application events, errors, and debugging information. 
        'plugins',                  # Folder for plugins or extensions that add functionality to the application. 
        'plugins/analysis',         # Plugins related to data analysis tasks. 
        'plugins/data_io',          # Plugins for data input/output operations. 
        'plugins/visualization',    # Plugins for creating visualizations of data. 
        'res',                      # Resource folder for static files like images, CSS, or HTML templates. 
        'scrapes',                  # Folder for storing data collected from web scraping activities. 
        'trash',                    # Folder for temporarily storing files marked for deletion. 
        'utils'                     # Utility functions and helper modules used across the project. 
    ]

    # Iterate over each required folder and create it if it doesn't exist
    for folder in required_folders:
        try:
            if not os.path.exists(folder):
                os.makedirs(folder)  # Create the folder and any necessary parent directories
                logger.info(f"Created missing directory: '{folder}'")  # Log directory creation
            else:
                logger.info(f"Directory already exists: '{folder}'")  # Log if directory exists
        except OSError as e:
            logger.error(f"Error creating directory '{folder}': {e}")  # Log error if creation fails

