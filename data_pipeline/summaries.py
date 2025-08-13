import pandas as pd
from sqlalchemy import text
from .database import engine

def get_summary():
    with engine.connect() as conn:
        total_transactions = conn.execute(text("SELECT COUNT(*) FROM transactions")).scalar()
        category_stats = pd.read_sql("SELECT category, SUM(amount) as total, AVG(amount) as average FROM transactions GROUP BY category", conn)
        date_range = conn.execute(text("SELECT MIN(transaction_date), MAX(transaction_date) FROM transactions")).fetchone()

    return {
        "total_transactions": total_transactions,
        "category_stats": category_stats,
        "date_range": date_range
    }
