import pandas as pd
import numpy as np
import os

def generate_dummy_data(file_path):
    # Define la cantidad de filas y columnas
    num_rows = 100
    num_cols = 5

    # Genera nombres de columnas
    columns = [f"Column_{i+1}" for i in range(num_cols)]

    # Genera datos aleatorios
    data = np.random.rand(num_rows, num_cols) * 100

    # Crea un DataFrame de pandas
    df = pd.DataFrame(data, columns=columns)

    # Guarda el DataFrame en un archivo CSV
    df.to_csv(file_path, index=False)
    print(f"Datos de prueba generados y guardados en {file_path}")

if __name__ == '__main__':
    # Define la ruta del archivo de datos de prueba
    output_file = 'data/raw/sample.csv'
    
    # Asegura que el directorio de salida exista
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    # Genera los datos de prueba
    generate_dummy_data(output_file)