"""
Plugin for loading ARFF files into pandas DataFrames.

Author: Lázaro Bustio Martínez
Date: 2024-08-01
Version: 1.0.0
Email: lbustio@gmail.com
"""

import pandas as pd
from scipy.io import arff
from core.logging_config import logger
from core.data_io_plugin import DataIOPlugin

class arff_loader(DataIOPlugin):
    """
    Plugin for loading ARFF files into a pandas DataFrame.

    Attributes:
        _description (str): A brief description of the plugin's functionality.
        _version (str): The version of the plugin.
        _author (str): The author of the plugin.
        _date (str): The date when the plugin was created or last modified.
        _config (dict): Configuration settings for the plugin, which is empty in this case.

    Methods:
        load(path: str) -> pd.DataFrame:
            Loads an ARFF file from the specified path and returns its content as a DataFrame.
    """
    
    def __init__(self):
        """
        Initializes the arff_loader plugin with default configuration settings.
        """
        super().__init__()
        self._description = "Plugin for loading ARFF files into a pandas DataFrame."
        self._version = "1.0.0"
        self._author = "Lázaro Bustio Martínez"
        self._date = "2024.08.01"
        self._config = {
            # ARFF files typically do not have specific configuration settings for this plugin
        }

    def load(self, path: str) -> pd.DataFrame:
        """
        Load an ARFF file from the specified path into a pandas DataFrame.

        Args:
            path (str): The path to the ARFF file.

        Returns:
            pd.DataFrame: The loaded data as a DataFrame.
        
        Raises:
            FileNotFoundError: If the ARFF file does not exist at the specified path.
            ValueError: If there is an issue with reading the ARFF file.
            Exception: For any other exceptions that occur during the file loading process.
        """
        try:
            # Load the ARFF file into a dictionary
            data, meta = arff.loadarff(path)
            # Convert the data to a pandas DataFrame
            df = pd.DataFrame(data)
            logger.info(f"ARFF file loaded successfully from '{path}'.")
            return df
        except FileNotFoundError as e:
            logger.error(f"ARFF file not found: '{path}'. The error message is: {e}")
            raise
        except ValueError as e:
            logger.error(f"Error with ARFF file: '{path}'. The error message is: {e}")
            raise
        except Exception as e:
            logger.error(f"An unexpected error occurred while loading ARFF file: {e}")
            raise
