import pandas as pd

def load_csv(filepath: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(filepath)
        return df
    except Exception as e:
        raise RuntimeError(f"Error reading CSV: {e}")
