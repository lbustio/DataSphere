# DataSphere CLI

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

The CLI accepts commands in the format `command=value`. Here’s a quick overview of available commands:

- `load_data=<path> [sheet_name=<name>]`: Load data from the specified file path. Optionally specify the sheet name for XLSX files.
- `visualize=<plugin> [max_row=<number>] [row_selection=<top|bottom|random|by_class>] [class_column=<column>] [class_value=<value>]`: Visualize data using the specified plugin.
- `analyze=<plugin>`: Analyze data using the specified plugin.
- `save=<path>`: Save analysis results to the specified file path.
- `help [command]`: Show help information for a specific command or general help.

### Example

Some usage examples are:

```bash
python datasphere_cli.py load_data=data.xlsx sheet_name=Sheet1
python datasphere_cli.py visualize=histogram max_row=50 row_selection=top class_column=Category
python datasphere_cli.py analyze=summary_statistics
python datasphere_cli.py save=results.txt
```

## Plugin System

The DataSphere CLI uses a plugin-based architecture to allow for flexible and extensible data processing.

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

Contributions are welcome! Please open an issue or submit a pull request with your proposed changes. Ensure to follow the project's coding standards and include tests for new features.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

For more information, contact Lázaro Bustio Martínez at <lbustio@gmail.com>.
