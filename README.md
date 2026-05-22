# Lightweight CSV Data Profiler

<p align="left">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" height="48" alt="Python" title="Python" /> &nbsp;
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pandas/pandas-original.svg" height="48" alt="Pandas" title="Pandas" />
</p>

## Project Overview
This repository contains a command-line utility designed for rapid Exploratory Data Analysis (EDA) and automated data cleaning. It allows users to quickly ingest raw CSV datasets, generate structural insights, and output a sanitized version of the data for downstream machine learning or backend processing pipelines.

## Features
- **Automated Data Profiling:** Instantly generates file structure metadata, including data types, non-null counts, and unique value distributions per column.
- **Data Sanitization:** Automatically detects and removes duplicate records, saving a cleaned output file without altering the source data.
- **Robust Error Handling:** Built-in exception handling to gracefully manage missing files, empty datasets (`EmptyDataError`), and unexpected structural anomalies.
- **CLI Interface:** A simple, interactive command-line interface for seamless local testing and data inspection.

## Quick Start

1. Ensure you have Python installed along with the Pandas library:
   ```bash
   pip install pandas
   ```
2. Run the analyzer script:
   ```bash
   python "CSV File Analyzer.py"
   ```
3. When prompted, provide the absolute path to your target CSV file. The script will output the insights to your terminal and generate a cleaned_data_[filename].csv in the exact same directory as your source file.
