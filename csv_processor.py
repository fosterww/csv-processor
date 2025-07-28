import pandas as pd
import argparse
import sys
from pathlib import Path

def load_data(file_path: str) -> pd.DataFrame:
    """Load a CSV file into a Pandas DataFrame."""
    try:
        if not Path(file_path).is_file():
            raise FileNotFoundError(f'Error: File "{file_path}" not found.')
        
        df = pd.read_csv(file_path)
        if df.empty:
            raise ValueError("Error: CSV file is empty.")
        
        return df
    except pd.errors.ParserError:
        print("Error: Invalid CSV format.")
        sys.exit(1)
    except Exception as e:
        print(f"Error loading file: {str(e)}")
        sys.exit(1)

def summarize_data(df: pd.DataFrame) -> dict:
    """Compute summaries from the DataFrame."""
    summary = {}
    
    try:
        if 'age' in df.columns:
            summary['average_age'] = df['age'].mean()
        if 'salary' in df.columns:
            summary['total_salary'] = df['salary'].sum()
        if 'department' in df.columns:
            summary['department_counts'] = df['department'].value_counts().to_dict()
            
        return summary
    except Exception as e:
        print(f"Error summarizing data: {str(e)}")
        return {}
    
def save_summary(summary: dict, output_file: str) -> None:
    """Save summary to a text file."""
    try:
        with open(output_file, 'w') as f:
            f.write('Data summary\n')
            f.write('============\n')
            for key, value in summary.items():
                f.write(f"{key.replace('_', ' ').title()}: {value}\n")
        print(f"Summary saved to {output_file}")
    except Exception as e:
        print(f"Error saving summary: {str(e)}")
        
def main():
    """Main function to process CSV and generate summary."""
    parser = argparse.ArgumentParser(description="Process a CSV file and summarize its data.")
    parser.add_argument("file_path", help="Path to the input CSV file")
    args = parser.parse_args()
    
    df = load_data(args.file_path)
    summary = summarize_data(df)
    
    if summary:
        print("Data summary:\n")
        for key, value in summary.items():
            print(f"{key.replace('_', ' ').title()}: {value}")
    output_file = "summary.txt"
    save_summary(summary, output_file)
    
if __name__ == "__main__":
    main()