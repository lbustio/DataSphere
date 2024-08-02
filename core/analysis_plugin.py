"""
Base class for analysis plugins in the DataSphere system.

This module defines the AnalysisPlugin class, which serves as a base class for analysis plugins in the system. 
It inherits from the BasePlugin class and provides a foundation for all analysis-related plugins.

Author: Lázaro Bustio Martínez
Date: 2024-08-01
Version: 1.0
Email: lbustio@gmail.com
"""

from base_plugin import BasePlugin

class AnalysisPlugin(BasePlugin):
    """
    Base class for analysis plugins.
    
    Inherits from BasePlugin and serves as a foundation for all analysis-related plugins.
    """
    def __init__(self):
        super().__init__()
