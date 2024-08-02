"""
Plugin for interactive and visually attractive data visualization using Plotly.

Author: Lázaro Bustio Martínez
Date: 2024-08-01
Version: 1.0.0
Email: lbustio@gmail.com
"""

import pandas as pd
import plotly.express as px
import ipywidgets as widgets
from IPython.display import display
from core.visualization_plugin import VisualizationPlugin

class interactive_graph_viewer(VisualizationPlugin):
    """
    Plugin for creating interactive and visually appealing data visualizations using Plotly.

    Attributes:
        _chart_types (list): List of supported chart types for visualization.

    Methods:
        visualize(dataframe: pd.DataFrame, class_column: str = None, class_value: str = None): 
            Displays interactive plots for the DataFrame.
    """
    
    def __init__(self):
        """
        Initializes the interactive_graph_viewer plugin with default settings and chart types.
        """
        super().__init__()
        self._description = "Plugin for interactive and visually attractive data visualization using Plotly."
        self._version = "1.0.0"
        self._author = "Lázaro Bustio Martínez"
        self._date = "2024.08.01"
        self._chart_types = ["scatter", "line", "bar", "histogram", "box", "heatmap"]

    def visualize(self, dataframe: pd.DataFrame, class_column: str = None, class_value: str = None):
        """
        Creates and displays interactive plots from the DataFrame using Plotly.
        
        Args:
            dataframe (pd.DataFrame): The DataFrame to visualize.
            class_column (str, optional): The column used for filtering the DataFrame by class.
            class_value (str, optional): The value of the class to filter by.

        Returns:
            None
        """
        # Filter dataframe if class_column and class_value are provided
        if class_column and class_value:
            if class_column not in dataframe.columns:
                logger.error(f"Column '{class_column}' does not exist in the DataFrame.")
                raise ValueError(f"Column '{class_column}' not found in DataFrame.")
            dataframe = dataframe[dataframe[class_column].astype(str).str.lower() == class_value.lower()]

        # Create widgets for user interaction
        chart_type = widgets.Dropdown(
            options=self._chart_types,
            value='scatter',
            description='Chart Type:',
        )
        x_axis = widgets.Dropdown(
            options=dataframe.columns.tolist(),
            value=dataframe.columns[0],  # Default to the first column
            description='X-axis:',
        )
        y_axis = widgets.Dropdown(
            options=dataframe.columns.tolist(),
            value=dataframe.columns[1] if len(dataframe.columns) > 1 else dataframe.columns[0],  # Default to the second column or first if only one column
            description='Y-axis:',
        )
        color_column = widgets.Dropdown(
            options=[None] + dataframe.columns.tolist(),  # Add 'None' option for no color distinction
            value=None,
            description='Color By:',
        )
        
        # Display widgets
        display(chart_type, x_axis, y_axis, color_column)
        
        # Function to update the plot based on widget values
        def update_plot(change):
            try:
                fig = None
                if chart_type.value == "scatter":
                    fig = px.scatter(dataframe, x=x_axis.value, y=y_axis.value, color=color_column.value)
                elif chart_type.value == "line":
                    fig = px.line(dataframe, x=x_axis.value, y=y_axis.value, color=color_column.value)
                elif chart_type.value == "bar":
                    fig = px.bar(dataframe, x=x_axis.value, y=y_axis.value, color=color_column.value)
                elif chart_type.value == "histogram":
                    fig = px.histogram(dataframe, x=x_axis.value, color=color_column.value)
                elif chart_type.value == "box":
                    fig = px.box(dataframe, x=x_axis.value, y=y_axis.value, color=color_column.value)
                elif chart_type.value == "heatmap":
                    fig = px.imshow(dataframe.corr())
                else:
                    logger.error(f"Unsupported chart type: '{chart_type.value}'. Defaulting to 'scatter'.")
                    fig = px.scatter(dataframe, x=x_axis.value, y=y_axis.value, color=color_column.value)
                
                fig.update_layout(title=f"{chart_type.value.capitalize()} Plot")
                fig.show()
            
            except Exception as e:
                logger.error(f"An error occurred while updating the plot: {str(e)}")
                raise

        # Attach the update function to widget changes
        chart_type.observe(update_plot, names='value')
        x_axis.observe(update_plot, names='value')
        y_axis.observe(update_plot, names='value')
        color_column.observe(update_plot, names='value')

        # Display initial plot
        update_plot(None)
