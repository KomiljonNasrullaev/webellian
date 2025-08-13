import click
from .utils import load_csv
from .core import mean, median, mode, variance, std_dev, correlation_matrix
from .visualization import histogram, boxplot, scatter_plot

@click.group()
def cli():
    pass

@cli.command()
@click.argument("csv_file")
def summary(csv_file):
    """Show summary statistics for a CSV file."""
    df = load_csv(csv_file)
    click.echo("Summary Statistics:")
    for col in df.select_dtypes(include=["number"]).columns:
        click.echo(f"\nColumn: {col}")
        click.echo(f"  Mean: {mean(df, col)}")
        click.echo(f"  Median: {median(df, col)}")
        click.echo(f"  Mode: {mode(df, col)}")
        click.echo(f"  Variance: {variance(df, col)}")
        click.echo(f"  Std Dev: {std_dev(df, col)}")
        click.echo(f"  Correlation Matrix: {correlation_matrix(df)}")

@cli.command()
@click.argument("csv_file")
@click.argument("column")
def hist(csv_file, column):
    """Show histogram of a column."""
    df = load_csv(csv_file)
    histogram(df, column)

@cli.command()
@click.argument("csv_file")
@click.argument("column")
def box(csv_file, column):
    """Show boxplot of a column."""
    df = load_csv(csv_file)
    boxplot(df, column)

@cli.command()
@click.argument("csv_file")
@click.argument("x")
@click.argument("y")
def scatter(csv_file, x, y):
    """Show scatter plot between two columns."""
    df = load_csv(csv_file)
    scatter_plot(df, x, y)

if __name__ == "__main__":
    cli()
