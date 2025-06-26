import pandas as pd

# etl.py
"""
A simple ETL (Extract, Transform, Load) pipeline example for data engineering.
This script reads data from a CSV file, transforms it, and writes the result to a new CSV file.
"""


def extract(file_path):
    """Extract data from a CSV file."""
    df = pd.read_csv(file_path)
    return df

def transform(df):
    """Transform the data (example: clean and add a new column)."""
    # Drop rows with missing values
    df = df.dropna()
    # Add a new column: total = quantity * price
    if 'quantity' in df.columns and 'price' in df.columns:
        df['total'] = df['quantity'] * df['price']
    return df

def load(df, output_path):
    """Load the transformed data to a new CSV file."""
    df.to_csv(output_path, index=False)

if __name__ == "__main__":
    # Example usage
    input_file = 'input_data.csv'    # Replace with your input file path
    output_file = 'output_data.csv'  # Replace with your output file path

    # ETL process
    data = extract(input_file)
    data_transformed = transform(data)
    load(data_transformed, output_file)
    print(f"ETL process completed. Output saved to {output_file}")