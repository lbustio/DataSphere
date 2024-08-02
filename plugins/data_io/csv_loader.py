import pandas as pd
from core.logging_config import logger
from core.data_io_plugin import DataIOPlugin

class csv_loader(DataIOPlugin):
    """
    Plugin for loading CSV files.

    Methods:
        load(path): Loads a CSV file from the specified path and returns a DataFrame.
    """
    
    def __init__(self):
        super().__init__()
        self._description = "Plugin for loading CSV files into a pandas DataFrame."
        self._version = "1.0.0"
        self._author = "Lázaro Bustio Martínez"
        self._date = "2024.08.01"
        self._config = {
            "delimiter": ",",  # Default delimiter for CSV
            "header": True,    # Whether the CSV file has a header row
        }

    def load(self, path):
        """
        Load a CSV file from the specified path.

        Args:
            path (str): The path to the CSV file.

        Returns:
            pd.DataFrame: The loaded data as a DataFrame.
        
        Raises:
            FileNotFoundError: If the CSV file does not exist.
            pd.errors.EmptyDataError: If the CSV file is empty.
            pd.errors.ParserError: If there is a parsing error in the CSV file.
        """
        try:
            # Load the CSV file into a DataFrame
            data = pd.read_csv(path, delimiter=self._config["delimiter"], header=0 if self._config["header"] else None)
            logger.info(f"CSV file loaded successfully from '{path}'.")
            return data
        except FileNotFoundError as e:
            logger.error(f"CSV file not found: '{path}'. The error message is: {e}")
            raise e
        except pd.errors.EmptyDataError as e:
            logger.error(f"CSV file is empty: '{path}'. The error message is: {e}")
            raise e
        except pd.errors.ParserError as e:
            logger.error(f"Error parsing CSV file: '{path}'. The error message is: {e}")
            raise
        except Exception as e:
            logger.error(f"An unexpected error occurred while loading CSV file: {e}")
            raise e
