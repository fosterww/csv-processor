CSV Processor

A Python script to parse and summarize CSV data using Pandas. This project demonstrates data processing, error handling, and command-line interface (CLI) skills, built as part of my journey to become a Junior Python Developer. Features include Load CSV, Reads CSV file, and command-line interface (CLI) skills.
Features

    Load CSV: Reads a CSV file into a Pandas DataFrame with robust error handling.
    Summarize Data: Computes summaries like average, total, and counts by category (e.g., average age, total salary, department counts).
    Save Output: Saves summaries to a text file (summary.txt).
    CLI Support: Accepts a CSV file path via command-line arguments.
    Portfolio-Ready: Clean, modular code with PEP 8 compliance and detailed documentation.

Prerequisites

    Python 3.10 or higher
    Pandas (pip install pandas)

Installation

    Clone the repository:
    bash

git clone https://github.com/fosterww/csv-processor.git
cd csv-processor
Create and activate a virtual environment:
bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:
bash

    pip install pandas

Usage

    Prepare a CSV file (e.g., data.csv) with columns like name, age, salary, and department. Example:
    csv

name,age,salary,department
Alice,25,50000,HR
Bob,30,60000,IT
Charlie,35,55000,HR
Dave,28,62000,IT
Run the script:
bash

    python csv_processor.py data.csv
    View output:
        Summaries are printed to the console.
        A summary.txt file is created with the results.

Example Output

Console:
text
Data Summary:
Average Age: 29.5
Total Salary: 227000
Department Counts: {'HR': 2, 'IT': 2}
Summary saved to summary.txt

summary.txt:
text
Data Summary
============
Average Age: 29.5
Total Salary: 227000
Department Counts: {'HR': 2, 'IT': 2}
Project Structure

    csv_processor.py: Main script to load, process, and summarize CSV data.
    data.csv: Sample CSV file for testing.
    summary.txt: Output file with summarized data.
    README.md: This documentation.

How It Works

    Load Data: Uses Pandas pd.read_csv() to load the CSV file, with error handling for invalid files or formats.
    Summarize Data: Computes metrics like average age, total salary, and department counts using Pandas.
    Save Results: Writes summaries to summary.txt for persistence.
    CLI Integration: Uses argparse to accept the CSV file path via the command line.

Testing

    Valid CSV: Run with data.csv to verify summaries.
    Edge Cases: Tested with:
        Non-existent files (shows "File not found" error).
        Empty CSV files (shows "CSV is empty" error).
        Invalid CSV formats (shows "Invalid CSV format" error).
    Code Quality: Follows PEP 8, checked with flake8.

To test, install Flake8 (pip install flake8) and run:
bash
flake8 csv_processor.py
Future Improvements

    Add visualizations (e.g., Matplotlib charts for department counts).
    Support multiple CSV files or custom summary metrics.
    Integrate a web interface for interactive data exploration.

About

This project was built to practice Python data processing skills, including Pandas, error handling, and CLI development. It’s part of my portfolio to demonstrate backend and data manipulation capabilities for a Junior Python Developer role.
Contact

    GitHub: fosterww

Feel free to star this repository or provide feedback!
