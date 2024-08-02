"""
Plugin for loading CSV files into pandas DataFrames.

Author: Lázaro Bustio Martínez
Date: 2024-08-01
Version: 1.0.0
Email: lbustio@gmail.com
"""

import pandas as pd
from core.logging_config import logger
from core.data_io_plugin import DataIOPlugin

class csv_loader(DataIOPlugin):
    """
    Plugin for loading CSV files into a pandas DataFrame.

    Attributes:
        _description (str): A brief description of the plugin's functionality.
        _version (str): The version of the plugin.
        _author (str): The author of the plugin.
        _date (str): The date when the plugin was created or last modified.
        _config (dict): Configuration settings for the plugin, including delimiter and header options.

    Methods:
        load(path: str) -> pd.DataFrame:
            Loads a CSV file from the specified path and returns its content as a DataFrame.
    """
    
    def __init__(self):
        """
        Initializes the csv_loader plugin with default configuration settings.
        """
        super().__init__()
        self._description = "Plugin for loading CSV files into a pandas DataFrame."
        self._version = "1.0.0"
        self._author = "Lázaro Bustio Martínez"
        self._date = "2024.08.01"
        self._config = {
            "delimiter": ",",  # Default delimiter for CSV
            "header": True,    # Whether the CSV file has a header row
        }

    def load(self, path: str) -> pd.DataFrame:
        """
        Load a CSV file from the specified path into a pandas DataFrame.

        Args:
            path (str): The path to the CSV file.

        Returns:
            pd.DataFrame: The loaded data as a DataFrame.
        
        Raises:
            FileNotFoundError: If the CSV file does not exist at the specified path.
            pd.errors.EmptyDataError: If the CSV file is empty and cannot be read.
            pd.errors.ParserError: If there is an error in parsing the CSV file.
            Exception: For any other exceptions that occur during the file loading process.
        """
        try:
            # Load the CSV file into a DataFrame with specified configuration
            data = pd.read_csv(
                path,
                delimiter=self._config["delimiter"],
                header=0 if self._config["header"] else None
            )
            logger.info(f"CSV file loaded successfully from '{path}'.")
            return data
        except FileNotFoundError as e:
            logger.error(f"CSV file not found: '{path}'. The error message is: {e}")
            raise
        except pd.errors.EmptyDataError as e:
            logger.error(f"CSV file is empty: '{path}'. The error message is: {e}")
            raise
        except pd.errors.ParserError as e:
            logger.error(f"Error parsing CSV file: '{path}'. The error message is: {e}")
            raise
        except Exception as e:
            logger.error(f"An unexpected error occurred while loading the CSV file: {e}")
            raise
