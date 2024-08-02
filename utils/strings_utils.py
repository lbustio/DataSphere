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

    Args:
        file_path (str): The path to the file.

    Returns:
        str: The file extension (without the leading dot), or an empty string if the file has no extension.
    """

    # TODO: Validar el path que esta ok
    _, file_extension = os.path.splitext(file_path)
    return file_extension.strip('.')
