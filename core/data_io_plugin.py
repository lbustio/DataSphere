"""
Module for defining the DataIOPlugin base class.

This module contains the DataIOPlugin class, which serves as a base class for 
data input and output (I/O) plugins. It inherits from the BasePlugin class and 
provides a common interface for plugins that handle data I/O operations.

Author: Lázaro Bustio Martínez
Date: 2024-08-01
Version: 1.0
Email: lbustio@gmail.com
"""

from .base_plugin import BasePlugin

class DataIOPlugin(BasePlugin):
    """
    Base class for data I/O plugins.

    This class serves as a base for plugins that handle input and output operations
    related to data. It inherits from BasePlugin and provides a common interface
    for data I/O plugins.

    Attributes:
        None
    """
    
    def __init__(self):
        """
        Initializes the DataIOPlugin.

        Calls the initializer of the parent class, BasePlugin.
        """
        super().__init__()
