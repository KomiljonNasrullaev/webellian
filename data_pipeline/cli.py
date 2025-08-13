import click
from .logging_config import setup_logging
from .database import init_db, engine
from .data_ingestion import load_csv
from .data_cleaning import clean_data
from .summaries import get_summary

setup_logging()

@click.group()
def cli():
    """CLI for data pipeline"""
    pass

@cli.command()
@click.argument("csv_file")
def load(csv_file):
    """Load CSV file into the database after cleaning."""
    init_db()
    df = load_csv(csv_file)
    df_clean = clean_data(df)
    # Write to DB using pandas to_sql via SQLAlchemy engine
    with engine.begin() as conn:
        df_clean.to_sql("transactions", conn, if_exists="append", index=False)
    click.echo("Data loaded successfully.")

@cli.command()
def summary():
    """Print summary statistics."""
    s = get_summary()
    click.echo(f"Total transactions: {s['total_transactions']}")
    click.echo(s["category_stats"].to_string(index=False))
    start = s['date_range'][0]
    end = s['date_range'][1]
    click.echo(f"Date range: {start} → {end}")

if __name__ == "__main__":
    cli()
