import pandas as pd
from core.logging_config import logger
from core.data_io_plugin import DataIOPlugin

class xlsx_loader(DataIOPlugin):
    """
    Plugin for loading XLSX files.

    Methods:
        load(path): Loads an XLSX file from the specified path and returns a DataFrame.
    """
    
    def __init__(self):
        super().__init__()
        self._description = "Plugin for loading XLSX files into a pandas DataFrame."
        self._version = "1.0.0"
        self._author = "Lázaro Bustio Martínez"
        self._date = "2024.08.01"
        self._config = {
            "sheet_name": 0,  # Default to loading the first sheet
            "header": True,   # Whether the XLSX file has a header row
        }

    def load(self, path):
        """
        Load an XLSX file from the specified path.

        Args:
            path (str): The path to the XLSX file.

        Returns:
            pd.DataFrame: The loaded data as a DataFrame.
        
        Raises:
            FileNotFoundError: If the XLSX file does not exist.
            ValueError: If the specified sheet does not exist.
            pd.errors.EmptyDataError: If the XLSX file is empty.
            Exception: For any other exceptions that occur.
        """
        try:
            # Load the XLSX file into a DataFrame
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
            raise e
        except ValueError as e:
            logger.error(f"Error with sheet selection in XLSX file: '{path}'. The error message is: {e}")
            raise e
        except pd.errors.EmptyDataError as e:
            logger.error(f"XLSX file is empty: '{path}'. The error message is: {e}")
            raise e
        except Exception as e:
            logger.error(f"An unexpected error occurred while loading XLSX file: {e}")
            raise e
