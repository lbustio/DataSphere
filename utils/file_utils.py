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
