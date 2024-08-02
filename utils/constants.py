"""
Module: utils.terminal_colors

Author: Lázaro Bustio Martínez
Date: 2024-08-01
Version: 1.0
Email: lbustio@gmail.com

Description:
This module defines color codes for terminal output and associates them with different log levels. It allows for color-coded terminal messages to enhance readability and distinguish between different types of log messages.

"""

# Define color codes for terminal output
RESET = "\033[0m"       # Reset color to default
BLACK = "\033[30m"     # Black color code
RED = "\033[31m"       # Red color code
GREEN = "\033[32m"     # Green color code
YELLOW = "\033[33m"    # Yellow color code
BLUE = "\033[34m"      # Blue color code
MAGENTA = "\033[35m"   # Magenta color code
CYAN = "\033[36m"      # Cyan color code
WHITE = "\033[37m"     # White color code
LIGHT_BLUE = "\033[94m" # Light Blue color code

# Define log level colors
LOG_COLORS = {
    "DEBUG": BLUE,
    "INFO": GREEN,
    "WARNING": YELLOW,
    "ERROR": RED,
    "CRITICAL": MAGENTA,
}

