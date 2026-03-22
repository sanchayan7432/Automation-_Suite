# 03_merge_csv_files/main.py
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

def merge_csv(path):
    """Merge all CSV files inside a folder"""
    output_dir = BASE_DIR / "output"
    output_dir.mkdir(parents=True, exist_ok=True)

    try:
        data = None
        col = []

        for item in sorted(path.iterdir()):
            if item.suffix.lower() != ".csv":
                print(f"Skipping '{item.name}': Invalid file type (only .csv allowed)")
                continue

            csv = pd.read_csv(item)
            col_names = list(csv.columns)

            if not col:
                # Use the first valid CSV as base schema
                col = col_names
                data = csv
                print(f"Loaded '{item.name}' as base CSV with columns: {col_names}")
            else:
                # Only merge files with matching columns
                if set(col_names) == set(col):
                    csv = csv[col]
                    data = pd.concat([data, csv], axis=0)
                    print(f"Appended '{item.name}' ({len(csv)} rows)")
                else:
                    print(f"Skipped '{item.name}': columns don't match base CSV ({col_names})")

        if data is not None:
            data = data.reset_index(drop=True)
            file_path = output_dir / "data.csv"
            data.to_csv(file_path, index=False)
            print(f"\nMerged CSV saved to: {file_path} ({len(data)} total rows)")
        else:
            print("No valid CSV files found to merge.")

    except Exception as e:
        print(f"Error during merge: {e}")


def main():
    """Entry point for Merge CSV Files project"""
    default_folder = BASE_DIR / "input"

    while True:
        print()
        user_path = input("Enter full folder path to merge CSVs (or press Enter for default, 'q' to quit): ").strip()
        print()

        if user_path.lower() == 'q':
            print("Exiting Merge CSV Files project...")
            break

        if not user_path:
            path = default_folder
            if path.is_dir():
                print(f"No path provided — using default folder: {path}")
            else:
                print("Default folder is missing.")
                continue
        else:
            path = Path(user_path)

        if not path.is_dir():
            print("Folder not found. Please enter a valid folder path.")
            continue

        try:
            print(f"Folder exists: {path}")
            merge_csv(path)
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()