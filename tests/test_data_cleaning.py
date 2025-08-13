import pandas as pd
from data_pipeline.data_cleaning import clean_data

def test_clean_data_removes_negatives():
    df = pd.DataFrame({
        "transaction_id": ["1", "2"],
        "user_id": [1, 2],
        "transaction_date": ["2024-01-01", "2024-01-02"],
        "amount": [10.0, -5.0],
        "category": ["A", "B"]
    })
    cleaned = clean_data(df)
    print(cleaned)
    assert cleaned["amount"].min() >= 0
