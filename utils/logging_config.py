"""
Module for configuring the ClearData logger.

This module sets up a logger with colored output for the console and file logging.
Log messages are formatted with color codes based on their level, and timestamps
are displayed in yellow without milliseconds.

Author: Lázaro Bustio Martínez
Date: 2024-08-01
Version: 1.0
Email: lbustio@gmail.com
"""


import logging
import os
from utils.constants import RESET, LIGHT_BLUE, WHITE, LOG_COLORS


class ColoredFormatter(logging.Formatter):
    """
    Custom formatter to add color to log messages based on their level for console output.
    """

    def format(self, record):
        level_color = LOG_COLORS.get(record.levelname, RESET)
        reset = RESET

        log_message = super().format(record)

        try:
            parts = log_message.split(' - ')
            timestamp = parts[0]
            levelname = parts[1]
            message = parts[2]

            timestamp_colored = LIGHT_BLUE + timestamp + reset
            levelname_colored = level_color + levelname + reset
            message_colored = WHITE + message + reset

            return f"{timestamp_colored} - {levelname_colored} - {message_colored}"
        except IndexError:
            return f"{RESET} - {level_color}{record.levelname}{RESET} - {record.getMessage()}"


class PlainFormatter(logging.Formatter):
    """
    Formatter to format log messages without colors for file output.
    """

    def format(self, record):
        return super().format(record)


def setup_logger():
    """
    Sets up the logger with colored output for the console and file logging.
    """

    if not os.path.exists('logs'):
        os.makedirs('logs')

    logger = logging.getLogger('ClearData')
    logger.setLevel(logging.DEBUG)

    try:
        # File handler for logging to a file
        file_handler = logging.FileHandler('logs/clear_data.log')
        file_handler.setLevel(logging.DEBUG)

        # Console handler for colored output
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)

        # Formatters
        console_formatter = ColoredFormatter('%(asctime)s - %(levelname)s - %(message)s')
        console_formatter.datefmt = '%Y-%m-%d %H:%M:%S'  
        file_formatter = PlainFormatter('%(asctime)s - %(levelname)s - %(message)s')
        file_formatter.datefmt = '%Y-%m-%d %H:%M:%S'

        # Apply formatters to handlers
        file_handler.setFormatter(file_formatter)
        console_handler.setFormatter(console_formatter)

        # Add handlers to the logger
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
    except Exception as e:
        print(f"Failed to set up logger: {e}")

    return logger


# Initialize the logger when this module is imported
logger = setup_logger()
