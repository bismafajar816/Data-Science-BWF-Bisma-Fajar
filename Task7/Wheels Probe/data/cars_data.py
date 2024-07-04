import pandas as pd


def read_csv_data(file_path):
    try:
        df = pd.read_csv(file_path, encoding='latin1')
        return df.to_dict(orient='records')
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return []

# Example usage:
# cars_data = read_csv_data('cars.csv')
