import os
import fnmatch
from core.logging_config import logger

def validate_file_path(path):
    """
    Validates if the file exists and is readable.
    
    Args:
        path (str): The path to the file.
    
    Returns:
        bool: True if file exists and is readable, otherwise False.
    """
    if os.path.isfile(path) and os.access(path, os.R_OK):
        return True
    else:
        return False