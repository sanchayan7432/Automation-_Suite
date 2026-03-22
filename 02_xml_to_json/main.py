# 02_xml_to_json/main.py
from pathlib import Path
import xml.etree.ElementTree as ET
import json

BASE_DIR = Path(__file__).resolve().parent

def convert(tree):
    """Convert parsed XML tree into JSON file"""
    output_dir = BASE_DIR / "output"
    output_dir.mkdir(parents=True, exist_ok=True)

    root = tree.getroot()
    data = []

    # Decide records
    if all(len(child) == 0 for child in root):
        records = [root]  # single record XML
    else:
        records = root     # multiple records XML

    for record in records:
        d = {}
        for i in record:
            if len(i) == 0 and i.text:
                d[i.tag] = i.text.strip()
        data.append(d)

    file_path = output_dir / "data.json"
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print(f"JSON saved to {file_path} ({len(data)} records)")

def main():
    """Entry point for XML to JSON conversion"""
    while True:
        print()
        user_path = input("Enter full XML file path (or press Enter to use default, 'q' to quit): ").strip()
        print()

        default_xml = BASE_DIR / "input" / "data.xml"

        if user_path.lower() == 'q':
            print("Exiting XML to JSON converter...")
            break

        if not user_path:
            path = default_xml
            if path.is_file():
                print("No path provided — using default XML file")
            else:
                print("No file path provided, and the default XML file is missing.")
                continue
        else:
            path = Path(user_path)

        if not path.is_file():
            print("File not found.")
            continue

        if path.suffix.lower() != ".xml":
            print("Invalid file type. Only .xml files are allowed.")
            continue

        try:
            tree = ET.parse(path)
            print("XML file loaded successfully")
            try:
                convert(tree)
            except Exception as e:
                print(f"Error during conversion: {e}")
        except ET.ParseError:
            print("Failed to parse XML.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()