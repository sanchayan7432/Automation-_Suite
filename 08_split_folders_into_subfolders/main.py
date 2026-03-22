# 08_split_folders_into_subfolders/main.py
from pathlib import Path
import shutil

BASE_DIR = Path(__file__).resolve().parent

def split_folder(path, files_per_folder=9):
    """Split all files in a folder (including nested) into multiple subfolders in output/"""
    output_dir = BASE_DIR / "output"

    # Handle existing output folder
    if output_dir.exists():
        confirm = input("Output folder exists. Delete and continue? (y/n): ").strip().lower()
        if confirm != "y":
            print("Cancelled.")
            return
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Collect all files recursively
    all_files = [file for file in path.rglob("*") if file.is_file()]
    total_files = len(all_files)
    if total_files == 0:
        print("No files found to split.")
        return

    folder_count = 1
    start = 0

    try:
        while start < total_files:
            chunk = all_files[start:start+files_per_folder]
            if not chunk:
                break

            folder_path = output_dir / f"folder{folder_count}"
            folder_path.mkdir(parents=True, exist_ok=True)

            for file in chunk:
                dest_file = folder_path / file.name
                suffix = 1
                while dest_file.exists():
                    dest_file = folder_path / f"{file.stem}_{suffix}{file.suffix}"
                    suffix += 1
                shutil.move(str(file), dest_file)
                print(f"File: {file.name} → moved to {folder_path}")

            folder_count += 1
            start += files_per_folder

    except Exception as e:
        print(f"Error during splitting: {e}")

    print(f"{total_files} files split into {folder_count-1} subfolders successfully.")


def main():
    """Entry point for Split Folders into Subfolders project"""
    default_folder = BASE_DIR / "input"

    while True:
        print()
        user_path = input("Enter full folder path to split (or press Enter for default, 'q' to quit): ").strip()
        print()

        if user_path.lower() == "q":
            print("Exiting Split Folders into Subfolders project...")
            break

        if not user_path:
            path = default_folder
            if path.is_dir():
                print(f"No path provided — using default folder: {default_folder}")
            else:
                print("Default folder is missing.")
                continue
        else:
            path = Path(user_path)

        if path.is_dir():
            try:
                print(f"Folder exists: {path}")
                split_folder(path)
            except Exception as e:
                print(f"Error: {e}")
        else:
            print("Folder not found. Please enter a valid folder path.")


if __name__ == "__main__":
    main()