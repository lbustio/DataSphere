import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
from core.visualization_plugin import VisualizationPlugin
import threading

class interactive_graph_viewer(VisualizationPlugin):
    """
    Plugin for creating interactive and visually appealing data visualizations using Plotly and Dash.

    Attributes:
        _chart_types (list): List of supported chart types for visualization.

    Methods:
        visualize(dataframe: pd.DataFrame, class_column: str = None, class_value: str = None): 
            Displays interactive plots for the DataFrame.
    
    Example Usage:
        viewer = InteractiveGraphViewer()
        viewer.visualize(df, class_column='category', class_value='A')
    """
    
    def __init__(self):
        """
        Initializes the InteractiveGraphViewer plugin with default settings and chart types.
        """
        super().__init__()
        self._description = "Plugin for interactive and visually attractive data visualization using Plotly and Dash."
        self._version = "1.0.0"
        self._author = "Lázaro Bustio Martínez"
        self._date = "2024.08.01"
        self._chart_types = ["scatter", "line", "bar", "histogram", "box", "heatmap"]

    def visualize(self, dataframe: pd.DataFrame, class_column: str = None, class_value: str = None, use_reloader: bool = False):
        """
        Creates and displays interactive plots from the DataFrame using Plotly and Dash.
        
        Args:
            dataframe (pd.DataFrame): The DataFrame to visualize.
            class_column (str, optional): The column used for filtering the DataFrame by class.
            class_value (str, optional): The value of the class to filter by.
            use_reloader (bool, optional): Whether to use reloader for development. Default is False for production.

        Returns:
            None
        """
        if dataframe.empty:
            raise ValueError("DataFrame is empty.")

        if class_column and class_value:
            if class_column not in dataframe.columns:
                raise ValueError(f"Column '{class_column}' not found in DataFrame.")
            dataframe = dataframe[dataframe[class_column].astype(str).str.lower() == class_value.lower()]

        app = Dash(__name__)

        app.layout = html.Div([
            html.H1("Interactive Data Visualization"),
            dcc.Dropdown(
                id='chart-type',
                options=[{'label': chart_type.capitalize(), 'value': chart_type} for chart_type in self._chart_types],
                value='scatter',
                clearable=False,
                style={'width': '50%'}
            ),
            dcc.Dropdown(
                id='x-axis',
                options=[{'label': col, 'value': col} for col in dataframe.columns],
                value=dataframe.columns[0],
                clearable=False,
                style={'width': '50%'}
            ),
            dcc.Dropdown(
                id='y-axis',
                options=[{'label': col, 'value': col} for col in dataframe.columns],
                value=dataframe.columns[1] if len(dataframe.columns) > 1 else dataframe.columns[0],
                clearable=False,
                style={'width': '50%'}
            ),
            dcc.Dropdown(
                id='color-column',
                options=[{'label': 'None', 'value': 'None'}] + [{'label': col, 'value': col} for col in dataframe.columns],
                value='None',
                clearable=True,
                style={'width': '50%'}
            ),
            dcc.Graph(id='graph')
        ])

        @app.callback(
            Output('graph', 'figure'),
            [Input('chart-type', 'value'),
             Input('x-axis', 'value'),
             Input('y-axis', 'value'),
             Input('color-column', 'value')]
        )
        def update_graph(chart_type, x_axis, y_axis, color_column):
            try:
                color_column = None if color_column == 'None' else color_column
                
                # Validate that selected columns contain numeric data if needed
                if chart_type in ["scatter", "line", "bar", "histogram", "box"] and not pd.api.types.is_numeric_dtype(dataframe[x_axis]):
                    raise ValueError(f"Column '{x_axis}' must contain numeric data for chart type '{chart_type}'.")
                if chart_type in ["scatter", "line", "bar", "box"] and not pd.api.types.is_numeric_dtype(dataframe[y_axis]):
                    raise ValueError(f"Column '{y_axis}' must contain numeric data for chart type '{chart_type}'.")

                if chart_type == "scatter":
                    fig = px.scatter(dataframe, x=x_axis, y=y_axis, color=color_column)
                elif chart_type == "line":
                    fig = px.line(dataframe, x=x_axis, y=y_axis, color=color_column)
                elif chart_type == "bar":
                    fig = px.bar(dataframe, x=x_axis, y=y_axis, color=color_column)
                elif chart_type == "histogram":
                    fig = px.histogram(dataframe, x=x_axis, color=color_column)
                elif chart_type == "box":
                    fig = px.box(dataframe, x=x_axis, y=y_axis, color=color_column)
                elif chart_type == "heatmap":
                    # Validate if the DataFrame is suitable for heatmap (e.g., numeric values)
                    if not dataframe.select_dtypes(include=['number']).shape[1]:
                        raise ValueError("DataFrame does not contain numeric columns for heatmap.")
                    fig = px.imshow(dataframe.corr())
                else:
                    fig = px.scatter(dataframe, x=x_axis, y=y_axis, color=color_column)

                fig.update_layout(title=f"{chart_type.capitalize()} Plot")
                return fig
            except Exception as e:
                return px.scatter(title=f"Error: {str(e)}")

        # Run Dash app in a separate thread
        def run_server():
            app.run_server(debug=True, use_reloader=use_reloader)
            self._server_stop_event.set()  # Signal that the server has stopped

        thread = threading.Thread(target=run_server)
        thread.start()

        # Continue execution of the script
        print("Dash app is running in a separate thread.")

    def stop_server(self):
        """
        Stops the running Dash server by setting the stop event.
        """
        self._server_stop_event.set()
        print("Dash server has been stopped.")