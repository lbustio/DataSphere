import pandas as pd
import numpy as np
import os
import webbrowser
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
        self._date = "2024.08.03"
        self._author = "Lázaro Bustio Martínez"
    
    def visualize(self, dataframe: pd.DataFrame, data_path: str = None, class_column: str = None, class_value: str = None, output_file: str = "summary_report.html"):
        """
        Generates an HTML report summarizing the DataFrame including dimensions, column names, data types, and statistics.

        Args:
            dataframe (pd.DataFrame): The DataFrame to summarize.
            data_path (str): The path to the data file.
            class_column (str): Optional column name for filtering.
            class_value (str): Optional value for filtering.
            output_file (str): The path where the HTML report will be saved.

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

            # Ensure the output directory exists
            output_file_path = os.path.join('results', 'visualization', output_file)
            os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

            # Create an HTML report
            with open(output_file_path, "w") as file:
                # HTML Header with CSS styles
                file.write("""
                <html>
                <head>
                    <title>DataFrame Summary Report</title>
                    <style>
                        body {
                            font-family: Arial, sans-serif;
                            margin: 20px;
                            color: #333;
                        }
                        h1 {
                            color: #2c3e50;
                        }
                        h2 {
                            color: #3498db;
                        }
                        table {
                            width: 100%;
                            border-collapse: collapse;
                            margin: 20px 0;
                        }
                        table, th, td {
                            border: 1px solid #ddd;
                        }
                        th, td {
                            padding: 12px;
                            text-align: left;
                        }
                        th {
                            background-color: #f2f2f2;
                            color: #2c3e50;
                        }
                        tr:nth-child(even) {
                            background-color: #f9f9f9;
                        }
                        tr:hover {
                            background-color: #f1c40f;
                        }
                        .statistics {
                            border: 1px solid #ddd;
                            padding: 10px;
                            margin: 10px 0;
                            background-color: #f5f5f5;
                        }
                    </style>
                </head>
                <body>
                <h1>DataFrame Summary Report</h1>
                """)

                # Include the data file path
                if data_path:
                    file.write(f"<h2>Data File Path</h2><p>{data_path}</p>")

                # DataFrame dimensions
                num_rows, num_cols = dataframe.shape
                file.write(f"<h2>DataFrame Dimensions</h2>")
                file.write(f"<p>Rows: {num_rows}<br>Columns: {num_cols}</p>")

                # Column names and data types
                column_info = dataframe.dtypes.reset_index()
                column_info.columns = ['Column Name', 'Data Type']
                column_info["Data Type"] = column_info["Data Type"].astype(str)  # Convert to string

                file.write("<h2>Column Names and Data Types</h2>")
                file.write(column_info.to_html(index=False, border=0, classes='statistics'))

                # Basic statistics for numerical and non-numerical columns
                numeric_stats = dataframe.describe(include=[np.number]).style.background_gradient(cmap='coolwarm').to_html()
                non_numeric_stats = dataframe.describe(exclude=[np.number]).style.background_gradient(cmap='coolwarm').to_html()

                file.write("<h2>Basic Statistics (Numerical)</h2>")
                file.write(numeric_stats)

                file.write("<h2>Basic Statistics (Non-Numerical)</h2>")
                file.write(non_numeric_stats)

                # HTML Footer
                file.write("</body></html>")

            logger.info(f"DataFrame summary report generated successfully: {output_file_path}")

            # Open the HTML file in the default web browser
            webbrowser.open(f'file://{os.path.abspath(output_file_path)}')

        except Exception as e:
            logger.error(f"An error occurred while generating the summary report: {str(e)}")
            raise
