from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float, Date
from .config import DB_PATH

engine = create_engine(f"sqlite:///{DB_PATH}", echo=False)
metadata = MetaData()

transactions_table = Table(
    "transactions", metadata,
    Column("transaction_id", String, primary_key=True),
    Column("user_id", Integer, nullable=False),
    Column("transaction_date", Date, nullable=False),
    Column("amount", Float, nullable=False),
    Column("category", String, nullable=False),
)

def init_db():
    metadata.create_all(engine)

def get_connection():
    return engine.connect()
