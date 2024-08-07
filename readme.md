# DataSphere CLI

![DataEther Logo](res/datasphere.jpg)

DataSphere CLI is a command-line interface designed for managing and processing data through a modular plugin architecture. This tool enables users to efficiently load, visualize, analyze, and save data using a variety of extendable plugins.

DataSphere is specifically crafted to support researchers and developers by simplifying the data handling process. It abstracts away the complexities of data management and visualization, allowing users to concentrate on refining and testing their algorithms. By streamlining these tasks, DataSphere reduces the overhead associated with orchestrating data workflows, enabling researchers to focus more on their core computational work and experimental analysis.

## Table of Contents

- Features
- Installation
- Usage
  - Command Line Arguments
  - Commands
- Plugin System
  - BasePlugin
  - DataIOPlugin
  - VisualizationPlugin
  - AnalysisPlugin
- Logging Configuration
- Scientific Experimentation Focus
- Contributing
- License

## Features

- **Load Data:** Supports various file formats through data I/O plugins.
- **Visualize Data:** Provides visualization capabilities using dedicated plugins.
- **Analyze Data:** Allows data analysis with customizable analysis plugins.
- **Save Results:** Saves the results of data analysis to specified paths.
- **Plugin Architecture:** Extensible system for adding new functionalities via plugins.

## Installation

To get started with DataSphere CLI, clone the repository and install the necessary dependencies:

```bash
git clone https://github.com/your-username/datasphere-cli.git
cd datasphere-cli
pip install -r requirements.txt
```

## Usage

To use the DataSphere CLI, execute the script from the command line with the appropriate arguments.

### Command Line Arguments

The CLI accepts commands in the format `command=value`.  If multiple commands are required, each `command=value` pair should be separated by a space. Here’s a quick overview of available commands:

- `load_data=<path> [sheet_name=<name>]`: Load data from the specified file path. Optionally specify the sheet name for XLSX files.
- `visualize=<plugin> [max_row=<number>] [row_selection=<top|bottom|random|by_class>] [class_column=<column>] [class_value=<value>]`: Visualize data using the specified plugin.
- `analyze=<plugin>`: Analyze data using the specified plugin (**Under construction**).
- `save=<path>`: Save analysis results to the specified file path (**Under construction**).
- `help [command]`: Show help information for a specific command or general help (**Under construction**).

### Example

Some usage examples are:

```bash
# Command to read a CSV file from the 'data\raw' directory
python3 main.py load_data=data\raw\iris.csv

# Command to read a CSV file from the 'data\raw' directory and display the data in a table view
python3 main.py load_data=data\raw\iris.csv visualize=table_viewer

# Command to read the first sheet of an XLSX file from the 'data\raw' directory and visualize it using an interactive graph
python3 main.py load_data=data\raw\iris.xlsx visualize=interactive_graph_viewer sheet_name=1
```

## Plugin System

The DataSphere CLI utilizes a plugin-based architecture, enabling flexible and extensible data processing. The following image illustrates the proposed class hierarchy:

![Class hierarchy](res/class_diagram.png)

### BasePlugin

The `BasePlugin` class serves as the foundation for all plugins. It provides basic attributes such as description, version, author, and configuration.

### DataIOPlugin

The `DataIOPlugin` class is used for data input and output operations. It extends `BasePlugin` and is responsible for loading and saving data.

### VisualizationPlugin

The `VisualizationPlugin` class is used for data visualization tasks. It extends BasePlugin and provides methods to generate visual representations of the data.

### AnalysisPlugin

The `AnalysisPlugin` class is used for data analysis tasks. It extends `BasePlugin` and provides methods to perform various types of data analysis.

## Logging Configuration

The project uses a custom logging configuration to provide colored console output and file logging. The `logging_config.py` module sets up the logger with different formatters for console and file outputs.

## Scientific Experimentation Focus

DataSphere is designed with scientific experimentation in mind. It aims to streamline the workflow for researchers and developers by focusing on the core tasks of algorithm development and data analysis. The tool abstracts away the complexities of data management and visualization, allowing users to concentrate on the critical aspects of their experiments.

## Key Points of Focus

- **Simplified Data Handling**: DataSphere provides a seamless interface for loading, visualizing, and analyzing data, reducing the need for users to write boilerplate code for these tasks. This simplification accelerates the experimentation process by enabling researchers to quickly integrate and work with data.

- **Modular Plugin Architecture**: By using a modular plugin system, DataSphere allows users to extend its capabilities without altering the core functionality. Researchers can develop and integrate custom plugins tailored to their specific needs, ensuring that the system adapts to various experimental requirements.

- **Focus on Algorithm Development**: With DataSphere managing the data handling aspects, users can focus on refining their algorithms and methodologies. This focus helps to improve the quality and efficiency of experiments, as researchers can dedicate more time to experimentation and analysis.

- **Flexible Visualization and Analysis**: The built-in plugins for visualization and analysis offer a range of options to explore and interpret data. This flexibility supports a variety of scientific needs, from simple data exploration to complex statistical analysis.

By abstracting the data management and visualization tasks, DataSphere empowers researchers to conduct their work more effectively and efficiently, fostering innovation and accelerating the pace of scientific discovery.

## Contributing

DataSphere is a project currently under development, and as such, bugs and errors may occur. The author provides no warranties, and the software should be used at your own risk. Contributions are welcome! Please open an issue or submit a pull request with your proposed changes. Ensure that you adhere to the project's coding standards and include tests for any new features.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

For more information, contact Lázaro Bustio Martínez at <lbustio@gmail.com>.
