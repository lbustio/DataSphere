import pandas as pd
from scipy.io import arff
from core.logging_config import logger
from core.data_io_plugin import DataIOPlugin

class arff_loader(DataIOPlugin):
    """
    Plugin for loading ARFF files into a pandas DataFrame.

    Methods:
        load(path): Loads an ARFF file from the specified path and returns a DataFrame.
    """
    
    def __init__(self):
        super().__init__()
        self._description = "Plugin for loading ARFF files into a pandas DataFrame."
        self._version = "1.0.0"
        self._author = "Lázaro Bustio Martínez"
        self._date = "2024.08.01"
        self._config = {
            # ARFF files typically do not have specific configuration settings for this plugin
        }

    def load(self, path):
        """
        Load an ARFF file from the specified path.

        Args:
            path (str): The path to the ARFF file.

        Returns:
            pd.DataFrame: The loaded data as a DataFrame.
        
        Raises:
            FileNotFoundError: If the ARFF file does not exist.
            ValueError: If there is an issue with reading the ARFF file.
            Exception: For any other exceptions that occur.
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
            raise e
        except ValueError as e:
            logger.error(f"Error with ARFF file: '{path}'. The error message is: {e}")
            raise e
        except Exception as e:
            logger.error(f"An unexpected error occurred while loading ARFF file: {e}")
            raise e
