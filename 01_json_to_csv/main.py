# 01_json_to_csv/main.py
from pathlib import Path
import json
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent

def convert(data):
    """Convert JSON data to CSV"""
    output_dir = BASE_DIR / "output"
    output_dir.mkdir(parents=True, exist_ok=True)

    records = data if isinstance(data, list) else [data]
    users = []

    print(f"Processing {len(records)} record(s)...")

    for record in records:
        user = {}

        for key, value in record.items():

            # If value is a dictionary
            if isinstance(value, dict):
                for sub_key, sub_value in value.items():
                    user[f"{key}.{sub_key}"] = sub_value

            # If value is a list
            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, dict):
                        for sub_key, sub_value in item.items():
                            user[f"{key}.{sub_key}"] = sub_value
                    else:
                        user[f"{key}.{item}"] = 1

            else:
                user[key] = value

        users.append(user)

    # Convert to DataFrame
    df = pd.DataFrame(users)

    csv_path = output_dir / "data.csv"
    df.to_csv(csv_path, index=False)
    print(f"CSV saved to: {csv_path}")

def main():
    """Entry point for JSON to CSV conversion"""
    while True:
        print()
        user_path = input("Enter full JSON file path (or press Enter to use default, 'q' to quit): ").strip()
        print()

        # Default file path
        default_json = BASE_DIR / "input" / "data.json"

        if user_path.lower() == "q":
            print("Exiting JSON to CSV converter...")
            break

        path = Path(user_path) if user_path else default_json

        if not path.is_file():
            print("File not found.")
            continue

        if path.suffix.lower() != ".json":
            print("Invalid file type. Only .json allowed.")
            continue

        try:
            with path.open("r", encoding="utf-8") as file:
                data = json.load(file)
                print("JSON file loaded successfully")
                convert(data)
        except json.JSONDecodeError:
            print("Failed to parse JSON.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()