import pandas as pd

def load_csv(filepath: str) -> pd.DataFrame:
    """Load a CSV file into a pandas DataFrame."""
    try:
        return pd.read_csv(filepath)
    except Exception as e:
        raise RuntimeError(f"Error loading CSV: {e}")
