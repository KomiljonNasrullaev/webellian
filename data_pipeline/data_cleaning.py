import pandas as pd
import logging
from dateutil import parser

logging.basicConfig(level=logging.WARNING, format="%(message)s")

def standardize_dates(series: pd.Series) -> pd.Series:
    """Convert mixed-format date strings to ISO (YYYY-MM-DD).
       Logs invalid entries, keeps output as string.
    """
    def parse_flexible(val):
        if pd.isna(val) or str(val).strip() == "":
            return None
        try:
            dt = parser.parse(str(val), dayfirst=False)
            return dt.strftime('%Y-%m-%d')
        except Exception:
            logging.warning(f"Invalid date skipped: {val}")
            return None

    # Ensure clean strings before parsing
    return series.astype(str).str.strip().apply(parse_flexible)

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean transaction dataframe according to requirements."""
    required_cols = ["transaction_id",
                     "user_id",
                     "transaction_date",
                     "amount",
                     "category"]

    for col in required_cols:
        if col not in df.columns:
            raise ValueError(f"Missing required column: {col}")

    df = df.copy()

    df['transaction_date'] = standardize_dates(df['transaction_date'])

    # Remove invalid dates
    df = df[df['transaction_date'].notna()]

    # Remove null or negative amounts
    df = df[df['amount'].notna() & (df['amount'] >= 0)]

    # Remove duplicates
    df = df.drop_duplicates(subset=['transaction_id'], keep='first')

    return df
