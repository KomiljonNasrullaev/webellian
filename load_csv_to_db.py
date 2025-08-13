import sys
from data_pipeline.cli import cli

if __name__ == "__main__":
    # usage: python load_csv_to_db.py path/to/file.csv
    if len(sys.argv) < 2:
        print("Usage: python load_csv_to_db.py <csv_file>")
    else:
        # invoke click programmatically
        cli.main(["load", sys.argv[1]])
