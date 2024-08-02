"""
Module for configuring the DataSphere logger.

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
import re
from utils.constants import RESET, LIGHT_BLUE, WHITE, LOG_COLORS

# Define color for magenta
MAGENTA = '\033[35m'

class ColoredFormatter(logging.Formatter):
    """
    Custom formatter to add color to log messages based on their level for console output.
    
    This formatter uses ANSI escape codes to add colors to log messages based on their 
    severity level. Timestamps, level names, and messages are colored differently to 
    improve readability in the console output.
    """

    def format(self, record):
        """
        Formats a log record with color codes for console output.

        Args:
            record (logging.LogRecord): The log record to format.

        Returns:
            str: The formatted log message with color codes.
        """
        level_color = LOG_COLORS.get(record.levelname, RESET)
        reset = RESET

        log_message = super().format(record)

        # Highlight text within single quotes in magenta
        log_message = re.sub(r"'(.*?)'", f"{MAGENTA}'\\1'{RESET}", log_message)

        try:
            # Split the log message into timestamp, levelname, and message
            parts = log_message.split(' - ')
            timestamp = parts[0]
            levelname = parts[1]
            message = parts[2]

            # Apply colors to different parts of the log message
            timestamp_colored = LIGHT_BLUE + timestamp + reset
            levelname_colored = level_color + levelname + reset
            message_colored = WHITE + message + reset

            return f"{timestamp_colored} - {levelname_colored} - {message_colored}"
        except IndexError:
            # Fallback format if splitting fails
            return f"{RESET} - {level_color}{record.levelname}{RESET} - {record.getMessage()}"


class PlainFormatter(logging.Formatter):
    """
    Formatter to format log messages without colors for file output.
    
    This formatter provides a plain text format for log messages that is suitable for 
    file logging, ensuring that the log files remain readable and free of color codes.
    """

    def format(self, record):
        """
        Formats a log record without color codes.

        Args:
            record (logging.LogRecord): The log record to format.

        Returns:
            str: The formatted log message without color codes.
        """
        return super().format(record)


def setup_logger():
    """
    Sets up the logger with colored output for the console and file logging.

    Creates a directory for log files if it does not exist, configures the logger with 
    file and console handlers, and applies appropriate formatters for each handler.

    Returns:
        logging.Logger: The configured logger instance.
    """
    # Create a directory for log files if it does not exist
    if not os.path.exists('logs'):
        os.makedirs('logs')

    # Create and configure the logger
    logger = logging.getLogger('DataSphere')
    logger.setLevel(logging.DEBUG)

    try:
        # File handler for logging to a file
        file_handler = logging.FileHandler('logs/data_sphere.log')
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
