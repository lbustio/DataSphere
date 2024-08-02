"""
Module: utils.data_generation

Author: Lázaro Bustio Martínez
Date: 2024-08-01
Version: 1.0
Email: lbustio@gmail.com

Description:
This module contains a function for generating dummy data and saving it to a CSV file. The `generate_dummy_data` function creates a DataFrame with random numerical data and stores it in the specified file path. This is useful for testing and development purposes when actual data is not available.

"""

import pandas as pd
import numpy as np
import os

def generate_dummy_data(file_path):
    """
    Generates a DataFrame with random numerical data and saves it to a CSV file.

    The function creates a DataFrame with a predefined number of rows and columns filled with random values. It then saves this DataFrame to the specified file path in CSV format. The file path should include the file name and extension.

    Args:
        file_path (str): The path where the CSV file will be saved. This should be a string representing the file's location in the filesystem.

    Returns:
        None

    Raises:
        ValueError: If `file_path` is not a valid string or is empty.

    Example:
        >>> generate_dummy_data('data/raw/sample.csv')
        Datos de prueba generados y guardados en data/raw/sample.csv
    """

    # Validate that file_path is a non-empty string
    if not isinstance(file_path, str) or not file_path.strip():
        raise ValueError("The file path must be a non-empty string.")
    
    # Define the number of rows and columns
    num_rows = 100
    num_cols = 5

    # Generate column names
    columns = [f"Column_{i+1}" for i in range(num_cols)]

    # Generate random data
    data = np.random.rand(num_rows, num_cols) * 100

    # Create a pandas DataFrame
    df = pd.DataFrame(data, columns=columns)

    # Save the DataFrame to a CSV file
    df.to_csv(file_path, index=False)
    print(f"Dummy data generated and saved to {file_path}")

if __name__ == '__main__':
    # Define the path for the dummy data file
    output_file = 'data/raw/sample.csv'
    
    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    # Generate the dummy data
    generate_dummy_data(output_file)
