# Webellian Data Pipeline

## Overview
This Python application processes a CSV file containing user transactions and stores the cleaned data in a SQLite database.
It includes a CLI for loading data and generating summaries.
Python package called stats_helper that provides core statistical analysis functions on structured datasets (CSV files)

## Features
- Reads CSV files
- Cleans and validates data
- Stores results in SQLite
- CLI commands for data loading and summaries
- Logging for cleaning steps and errors

## Installation
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

Initialize database:
python init_db.py

Load CSV:
python -m data_pipeline.cli load transactions.csv

View summary:
python -m data_pipeline.cli summary

## Task 2: stats_helper Package
Show summary:
python -m stats_helper.cli summary transactions.csv

Show histogram:
python -m stats_helper.cli hist transactions.csv amount

Tests
pytest
# webellian
# webellian
