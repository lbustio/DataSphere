"""
Plugin for visualizing a DataFrame as an interactive table.

Author: Lázaro Bustio Martínez
Date: 2024-08-01
Version: 1.1.0
Email: lbustio@gmail.com
"""

import pandas as pd
import plotly.graph_objects as go
from core.logging_config import logger
from core.visualization_plugin import VisualizationPlugin

class table_viewer(VisualizationPlugin):
    """
    Plugin for visualizing pandas DataFrames as interactive tables using Plotly.

    Methods:
        visualize(dataframe: pd.DataFrame, class_column: str = None, class_value: str = None): Visualizes the DataFrame as an interactive table.
    """
    
    def __init__(self):
        """
        Initializes the table_viewer plugin with default configuration settings.
        """
        super().__init__()
        self._description = "Plugin for visualizing pandas DataFrames as interactive tables."
        self._version = "1.1.0"
        self._author = "Lázaro Bustio Martínez"
        self._config = {
            "max_rows": 100,  # Maximum number of rows to display at once
            "row_selection": "Random"  # Method for selecting rows: Random, Top, Bottom, by_class
        }

    def visualize(self, dataframe: pd.DataFrame, class_column: str = None, class_value: str = None):
        """
        Visualizes the DataFrame as an interactive table using Plotly.

        Args:
            dataframe (pd.DataFrame): The DataFrame to visualize.
            class_column (str, optional): The column name for class-based selection. Required for by_class.
            class_value (str, optional): The value of the class to select. Required for by_class.

        Returns:
            None
        
        Raises:
            ValueError: If class_column or class_value are not provided when row_selection is 'by_class'.
            KeyError: If the specified class_column does not exist in the DataFrame.
        """
        try:
            num_rows = len(dataframe)
            max_rows = self._config.get("max_rows", 100)
            row_selection = self._config.get("row_selection", "Random")

            # Validate and apply row selection policy
            if num_rows <= max_rows:
                logger.info(f"DataFrame has {num_rows} rows, which is fewer than or equal to max_rows. Showing all rows.")
                selected_data = dataframe
            else:
                if row_selection == "Top":
                    selected_data = dataframe.head(max_rows)
                elif row_selection == "Bottom":
                    selected_data = dataframe.tail(max_rows)
                elif row_selection == "Random":
                    selected_data = dataframe.sample(min(max_rows, num_rows), random_state=42)
                elif row_selection == "by_class":
                    if class_column is None or class_value is None:
                        logger.error("class_column and class_value must be provided for row_selection='by_class'.")
                        raise ValueError("class_column and class_value must be specified for by_class selection.")
                    
                    class_column = class_column.lower()
                    class_value = class_value.lower()
                    
                    if class_column not in dataframe.columns:
                        logger.error(f"Class column '{class_column}' does not exist in the DataFrame.")
                        raise KeyError(f"Class column '{class_column}' does not exist in the DataFrame.")
                    
                    filtered_data = dataframe[dataframe[class_column].str.lower() == class_value]
                    selected_data = filtered_data.head(max_rows)
                else:
                    logger.error(f"Unknown row_selection method: '{row_selection}'. Defaulting to 'Top'.")
                    selected_data = dataframe.head(max_rows)
            
            # Create the interactive table using Plotly
            fig = go.Figure(data=[go.Table(
                header=dict(values=list(selected_data.columns),
                            fill_color='paleturquoise',
                            align='left'),
                cells=dict(values=[selected_data[col] for col in selected_data.columns],
                           fill_color='lavender',
                           align='left'))
            ])

            fig.update_layout(title="Interactive DataFrame Viewer")
            fig.show()

            logger.info("DataFrame visualized successfully.")

        except ValueError as ve:
            logger.error(f"ValueError: {str(ve)}")
            raise
        except KeyError as ke:
            logger.error(f"KeyError: {str(ke)}")
            raise
        except Exception as e:
            logger.error(f"An error occurred while visualizing the DataFrame: {str(e)}")
            raise
