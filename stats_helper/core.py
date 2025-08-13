import pandas as pd

def mean(df: pd.DataFrame, column: str) -> float:
    return df[column].mean()

def median(df: pd.DataFrame, column: str) -> float:
    return df[column].median()

def mode(df: pd.DataFrame, column: str):
    return df[column].mode().tolist()

def variance(df: pd.DataFrame, column: str) -> float:
    return df[column].var()

def std_dev(df: pd.DataFrame, column: str) -> float:
    return df[column].std()

def correlation_matrix(df: pd.DataFrame) -> pd.DataFrame:
    return df.corr(numeric_only=True)
