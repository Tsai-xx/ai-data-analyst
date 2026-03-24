import pandas as pd

def analyze_data(file_path):
    df = pd.read_csv(file_path)

    summary = {
        "shape": df.shape,
        "columns": df.columns.tolist(),
        "missing": df.isnull().sum().to_dict(),
        "stats": df.describe().to_string()
    }

    return summary