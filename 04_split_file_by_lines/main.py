# 04_split_file_by_lines/main.py
from pathlib import Path
import shutil

BASE_DIR = Path(__file__).resolve().parent

def split_file(file):
    """Split a text file into multiple smaller files"""
    # Clean old output folder
    output_dir = BASE_DIR / "output"
    if output_dir.exists():
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Ask for number of lines per file
    while True:
        x = input("Enter number of lines per file (or press 'q' to go back): ").strip()
        if x.lower() == "q":
            print("Going back to file selection...")
            return
        try:
            x = int(x)
            if x > 0:
                break
            raise ValueError()
        except ValueError:
            print("Please enter a valid number.")

    # Read all lines from file
    lines = file.readlines()
    total_lines = len(lines)
    file_count = 1
    start = 0

    try:
        while start < total_lines:
            file_path = output_dir / f"file{file_count}.txt"
            chunk = lines[start:start + x]
            with open(file_path, "w", encoding="utf-8") as out:
                out.writelines(chunk)

            print(f"Part {file_count} created successfully → {file_path}")
            file_count += 1
            start += x
    except Exception as e:
        print(f"Error: {e}")

    print("All files created successfully in 'output/' folder.")


def main():
    """Entry point for Split Text File by Lines project"""
    default_file = BASE_DIR / "input" / "story.txt"

    while True:
        print()
        user_path = input("Enter full .txt file path to split (or press Enter for default, 'q' to quit): ").strip()
        print()

        if user_path.lower() == "q":
            print("Exiting Split Text File by Lines project...")
            break

        if not user_path:
            path = default_file
            if path.is_file():
                print(f"No path provided — using default file: {default_file.name}")
            else:
                print("No path provided and default file is missing.")
                continue
        else:
            path = Path(user_path)

        if path.is_file() and path.suffix.lower() == ".txt":
            try:
                with path.open("r", encoding="utf-8") as file:
                    print(f"File loaded successfully: {path.name}")
                    split_file(file)
            except Exception as e:
                print(f"Failed to open file: {e}")
        else:
            print("Invalid file or file not found. Please provide a valid .txt file.")


if __name__ == "__main__":
    main()