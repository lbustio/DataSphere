"""
Module: utils.strings_utils

Author: Lázaro Bustio Martínez
Date: 2024-08-01
Version: 1.0
Email: lbustio@gmail.com
"""

import os

def get_file_extension(file_path):
    """
    Extracts the file extension from a file path.

    This function splits the given file path into its base name and extension. It then returns the file extension without the leading dot. If the file path does not have an extension, the function returns an empty string. If the input path is invalid, an appropriate error is raised.

    Args:
        file_path (str): The path to the file. This can be a relative or absolute path, including the filename.

    Returns:
        str: The file extension (without the leading dot). If the file has no extension, an empty string is returned.

    Raises:
        ValueError: If `file_path` is not a valid string or is empty.

    Example:
        >>> get_file_extension('/path/to/file.txt')
        'txt'
        
        >>> get_file_extension('/path/to/file')
        ''
    """

    # Validate that file_path is a non-empty string
    if not isinstance(file_path, str) or not file_path.strip():
        raise ValueError("The file path must be a non-empty string.")
    
    # Split the file path into root and extension
    _, file_extension = os.path.splitext(file_path)
    
    # Return the extension without the leading dot
    return file_extension.strip('.')

# The function now raises a ValueError if the file_path is not valid, 
# ensuring that only valid paths are processed.
