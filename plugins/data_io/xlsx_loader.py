"""
Plugin for loading XLSX files into pandas DataFrames.

Author: Lázaro Bustio Martínez
Date: 2024-08-01
Version: 1.0.0
Email: lbustio@gmail.com
"""

import pandas as pd
from core.logging_config import logger
from core.data_io_plugin import DataIOPlugin

class xlsx_loader(DataIOPlugin):
    """
    Plugin for loading XLSX files into a pandas DataFrame.

    Attributes:
        _description (str): A brief description of the plugin's functionality.
        _version (str): The version of the plugin.
        _author (str): The author of the plugin.
        _date (str): The date when the plugin was created or last modified.
        _config (dict): Configuration settings for the plugin, including default sheet and header options.

    Methods:
        load(path: str) -> pd.DataFrame: 
            Loads an XLSX file from the specified path and returns its content as a DataFrame.
    """
    
    def __init__(self):
        """
        Initializes the xlsx_loader plugin with default configuration settings.
        """
        super().__init__()
        self._description = "Plugin for loading XLSX files into a pandas DataFrame."
        self._version = "1.0.0"
        self._author = "Lázaro Bustio Martínez"
        self._date = "2024.08.01"
        self._config = {
            "sheet_name": 0,  # Default to loading the first sheet
            "header": True,   # Whether the XLSX file has a header row
        }

    def load(self, path: str) -> pd.DataFrame:
        """
        Load an XLSX file from the specified path into a pandas DataFrame.

        Args:
            path (str): The path to the XLSX file.

        Returns:
            pd.DataFrame: The loaded data as a DataFrame.
        
        Raises:
            FileNotFoundError: If the XLSX file does not exist at the specified path.
            ValueError: If the specified sheet name is invalid or the sheet does not exist.
            pd.errors.EmptyDataError: If the XLSX file is empty and cannot be read.
            Exception: For any other exceptions that occur during the file loading process.
        """
        try:
            # Load the XLSX file into a DataFrame with specified configuration
            data = pd.read_excel(
                path, 
                sheet_name=self._config["sheet_name"], 
                header=0 if self._config["header"] else None,
                index_col=None  # Do not use any column as the index
            )
            logger.info(f"XLSX file loaded successfully from '{path}'.")
            return data
        except FileNotFoundError as e:
            logger.error(f"XLSX file not found: '{path}'. The error message is: {e}")
            raise
        except ValueError as e:
            logger.error(f"Error with sheet selection in XLSX file: '{path}'. The error message is: {e}")
            raise
        except pd.errors.EmptyDataError as e:
            logger.error(f"XLSX file is empty: '{path}'. The error message is: {e}")
            raise
        except Exception as e:
            logger.error(f"An unexpected error occurred while loading the XLSX file: {e}")
            raise
