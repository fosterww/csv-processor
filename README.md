# CSV Processor

A Python script to parse and summarize CSV data using Pandas. This project demonstrates data processing, error handling, and command-line interface (CLI) development.

## ✨ Features

- **Load CSV**: Reads a CSV file into a Pandas DataFrame with robust error handling.
- **Summarize Data**: Computes:
  - Average age
  - Total salary
  - Department-wise employee count
- **Save Output**: Exports summaries to `summary.txt`.
- **CLI**: Accepts CSV file path via command-line arguments.
- **Portfolio-Ready**: Clean, modular, PEP 8-compliant code.

## 📦 Prerequisites

- Python 3.10 or higher
- Pandas

Install with:

```bash
pip install pandas
```

## 📥 Installation

Clone the repository and set up your environment:

```bash
git clone https://github.com/fosterww/csv-processor.git
cd csv-processor
```

Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Install dependencies:

```bash
pip install pandas
```

## 🚀 Usage

Prepare a CSV file named `data.csv`:

```csv
name,age,salary,department
Alice,25,50000,HR
Bob,30,60000,IT
Charlie,35,55000,HR
Dave,28,62000,IT
```

Run the script:

```bash
python csv_processor.py data.csv
```

### 📤 Output

Console:
```
Data Summary:
Average Age: 29.5
Total Salary: 227000
Department Counts: {'HR': 2, 'IT': 2}
Summary saved to summary.txt
```

File `summary.txt`:
```
Data Summary
============
Average Age: 29.5
Total Salary: 227000
Department Counts: {'HR': 2, 'IT': 2}
```

## 🧪 Testing

- ✅ Valid CSV: Run with a well-formed CSV to verify output.
- ⚠️ Edge Cases:
  - File not found error
  - Empty CSV error
  - Invalid format error

### Code Quality

Check with `flake8`:

```bash
pip install flake8
flake8 csv_processor.py
```

## 🔮 Future Improvements

- Add visualizations (e.g., bar charts with Matplotlib)
- Support multiple CSV files and custom metrics
- Add web interface for interactive exploration

## 👨‍💻 About

This project was created to practice backend and data manipulation skills using Python and Pandas. It’s part of my portfolio to showcase capabilities for junior-level development roles.

## 📬 Contact

- **GitHub**: [fosterww](https://github.com/fosterww)