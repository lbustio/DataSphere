import pandas as pd
import numpy as np
from core.logging_config import logger
from core.visualization_plugin import VisualizationPlugin

class resume_viewer(VisualizationPlugin):
    """
    Plugin for summarizing pandas DataFrames with textual information about dimensions, column names, data types, and statistics.
    """

    def __init__(self):
        """
        Initializes the ResumeViewer plugin with default configuration settings.
        """
        super().__init__()
        self._description = "Plugin for summarizing pandas DataFrames with textual information."
        self._version = "1.0.0"
        self._author = "Lázaro Bustio Martínez"
    
    def visualize(self, dataframe: pd.DataFrame, class_column: str = None, class_value: str = None):
        """
        Displays a textual summary of the DataFrame including dimensions, column names, data types, and statistics.

        Args:
            dataframe (pd.DataFrame): The DataFrame to summarize.
            class_column (str): Optional column name for filtering.
            class_value (str): Optional value for filtering.

        Returns:
            None
        
        Raises:
            ValueError: If the input is not a pandas DataFrame.
        """
        if not isinstance(dataframe, pd.DataFrame):
            logger.error("Input is not a pandas DataFrame.")
            raise ValueError("Input must be a pandas DataFrame.")
        
        try:
            # Filter DataFrame if class_column and class_value are provided
            if class_column and class_value:
                if class_column not in dataframe.columns:
                    raise ValueError(f"Column '{class_column}' does not exist in the DataFrame.")
                dataframe = dataframe[dataframe[class_column] == class_value]
                if dataframe.empty:
                    logger.warning("Filtered DataFrame is empty. Nothing to summarize.")
                    return 

            # DataFrame dimensions
            num_rows, num_cols = dataframe.shape
            print(f"DataFrame Dimensions:")
            print(f"  - Rows: {num_rows}")
            print(f"  - Columns: {num_cols}\n")

            # Column names and data types
            column_info = dataframe.dtypes.reset_index()
            column_info.columns = ['Column Name', 'Data Type']
            column_info["Data Type"] = column_info["Data Type"].astype(str)  # Convert to string

            print("Column Names and Data Types:")
            for _, row in column_info.iterrows():
                print(f"  - {row['Column Name']}: {row['Data Type']}")
            print()

            # Basic statistics for numerical and non-numerical columns
            numeric_stats = dataframe.describe(include=[np.number])
            non_numeric_stats = dataframe.describe(exclude=[np.number])

            # Print basic statistics
            print("Basic Statistics (Numerical):")
            print(numeric_stats)
            print()

            print("Basic Statistics (Non-Numerical):")
            print(non_numeric_stats)
            print()

            logger.info("DataFrame summarized successfully.")

            # Textual summary
            self._print_textual_summary(dataframe) 

        except Exception as e:
            logger.error(f"An error occurred while summarizing the DataFrame: {str(e)}")
            raise

    def _print_textual_summary(self, dataframe: pd.DataFrame):
        """
        Prints a textual summary of the DataFrame including dimensions, column names, data types, and basic statistics.

        Args:
            dataframe (pd.DataFrame): The DataFrame to summarize.

        Returns:
            None
        """
        num_rows, num_cols = dataframe.shape

        # DataFrame dimensions
        print(f"DataFrame Dimensions:")
        print(f"  - Rows: {num_rows}")
        print(f"  - Columns: {num_cols}\n")

        # Column names and data types
        print("Column Names and Data Types:")
        for col, dtype in dataframe.dtypes.items():
            print(f"  - {col}: {dtype}")
        print()

        # Basic statistics
        print("Basic Statistics (Numerical):")
        print(dataframe.describe(include=[np.number]))

        print("\nBasic Statistics (Non-Numerical):")
        print(dataframe.describe(exclude=[np.number]))
