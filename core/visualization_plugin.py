"""
Base class for visualization plugins.

Author: Lázaro Bustio Martínez
Date: 2024-08-01
Version: 1.0.0
Email: lbustio@gmail.com
"""

from .base_plugin import BasePlugin

class VisualizationPlugin(BasePlugin):
    """
    Base class for visualization plugins.

    This class serves as a base class for all visualization-related plugins, 
    inheriting common functionality from the BasePlugin class. It is intended 
    to be extended by specific visualization plugins to implement custom 
    visualization logic.

    Attributes:
        _description (str): A brief description of the plugin's functionality.
        _version (str): The version of the plugin.
        _author (str): The author of the plugin.
        _date (str): The date when the plugin was created or last modified.

    Methods:
        __init__(): Initializes the VisualizationPlugin with base plugin settings.
    """
    
    def __init__(self):
        """
        Initializes the VisualizationPlugin class.

        Calls the constructor of the BasePlugin class to inherit its properties 
        and methods. This method is intended to set up any additional attributes 
        or configurations specific to visualization plugins.
        """
        super().__init__()
        # Additional initialization code for VisualizationPlugin can be added here
