"""
Base class for all plugins in the system.

This module defines the BasePlugin class, which serves as a base class for all plugins in the system. 
It provides common attributes and methods that all plugins can inherit and use.

Author: Lázaro Bustio Martínez
Date: 2024-08-01
Version: 1.0
Email: lbustio@gmail.com
"""

class BasePlugin:
    """
    Base class for all plugins.

    Attributes:
        description (str): Description of the plugin.
        version (str): Version of the plugin.
        author (str): Author of the plugin.
        date (str): Date of the plugin.
        config (dict): Configuration dictionary of the plugin.
    """
    
    def __init__(self):
        self._description = "No description provided."
        self._version = "0.0.0"
        self._author = "Unknown"
        self._date = "Unknown"
        self._config = {}

    @property
    def description(self):
        """
        Returns a description of the plugin.
        
        Returns:
            str: Description of the plugin.
        """
        return self._description

    @property
    def version(self):
        """
        Returns the version of the plugin.
        
        Returns:
            str: Version of the plugin.
        """
        return self._version

    @property
    def author(self):
        """
        Returns the author of the plugin.
        
        Returns:
            str: Author of the plugin.
        """
        return self._author
    
    @property
    def date(self):
        """
        Returns the date of the plugin.
        
        Returns:
            str: Date of the plugin.
        """
        return self._date

    @property
    def config(self):
        """
        Returns the configuration of the plugin.
        
        Returns:
            dict: Configuration dictionary of the plugin.
        """
        return self._config
