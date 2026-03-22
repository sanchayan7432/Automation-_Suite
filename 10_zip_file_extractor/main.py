# 10_zip_file_extractor/main.py
from pathlib import Path
import shutil
import zipfile

BASE_DIR = Path(__file__).resolve().parent

def extract_zip(path):
    """Extract a ZIP file into the output folder"""
    output_dir = BASE_DIR / "output"

    # Clear output folder if exists
    if output_dir.exists():
        confirm = input("Output folder exists. Delete and continue? (y/n): ").strip().lower()
        if confirm != "y":
            print("Cancelled.")
            return
        shutil.rmtree(output_dir)

    output_dir.mkdir(parents=True, exist_ok=True)

    try:
        extract_folder = output_dir / path.stem
        with zipfile.ZipFile(path, 'r') as zip_ref:
            zip_ref.extractall(extract_folder)
            print(f"Extracted '{path.name}' → '{extract_folder}' successfully.")
    except Exception as e:
        print(f"Error while extracting: {e}")


def main():
    """Entry point for Zip File Extractor project"""
    default_file = BASE_DIR / "input" / "data.zip"

    while True:
        print()
        user_path = input("Enter full path of zip file to extract (Enter for default, 'q' to quit): ").strip()
        print()

        if user_path.lower() == "q":
            print("Exiting Zip File Extractor project...")
            break

        if not user_path:
            path = default_file
            if path.is_file():
                print(f"No path provided — using default ZIP file: {path}")
            else:
                print("Default ZIP file is missing.")
                continue
        else:
            path = Path(user_path)

        if path.is_file() and path.suffix.lower() == ".zip":
            try:
                print(f"ZIP file exists: {path}")
                extract_zip(path)
            except Exception as e:
                print(f"Error: {e}")
        else:
            print("404 - Please enter a valid zip file path.")


if __name__ == "__main__":
    main()