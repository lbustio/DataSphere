import pandas as pd
import plotly.express as px
import ipywidgets as widgets
from IPython.display import display
from core.visualization_plugin import VisualizationPlugin

class interactive_graph_viewer(VisualizationPlugin):
    """
    Plugin for interactive and visually attractive data visualization using Plotly.
    
    Methods:pip
        visualize(dataframe): Displays interactive plots for the DataFrame.
    """
    
    def __init__(self):
        super().__init__()
        self._description = "Plugin for interactive and visually attractive data visualization using Plotly."
        self._version = "1.0.0"
        self._author = "Lázaro Bustio Martínez"
        self._date = "2024.08.01"
        self._chart_types = ["scatter", "line", "bar", "histogram", "box", "heatmap"]

    def visualize(self, dataframe: pd.DataFrame, class_column=None, class_value=None):
        """
        Create interactive plots from the DataFrame.
        
        Args:
            dataframe (pd.DataFrame): The DataFrame to visualize.
            class_column (str): The column used for filtering by class.
            class_value (str): The value of the class to filter by.
            
        Returns:
            None
        """
        # Filter dataframe if class_column and class_value are provided
        if class_column and class_value:
            dataframe = dataframe[dataframe[class_column].astype(str).str.lower() == class_value.lower()]

        # Create widgets
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
        
        # Create and display plot
        def update_plot(change):
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
            
            fig.update_layout(title=f"{chart_type.value.capitalize()} Plot")
            fig.show()
        
        # Attach update function to widgets
        chart_type.observe(update_plot, names='value')
        x_axis.observe(update_plot, names='value')
        y_axis.observe(update_plot, names='value')
        color_column.observe(update_plot, names='value')

        # Initial plot
        update_plot(None)