# 05_text_file_analysis/main.py
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

def analyze_file(file):
    """Analyze a text file and print basic statistics"""
    lines = file.readlines()
    text = "".join(lines)
    chars = len(text)
    words = len(text.split())
    print(f"Lines: {len(lines)}, Words: {words}, Chars: {chars}")

def main():
    """Entry point for Text File Analysis project"""
    default_file = BASE_DIR / "input" / "story.txt"

    while True:
        print()
        user_path = input("Enter full .txt file path to analyze (or press Enter for default, 'q' to quit): ").strip()
        print()

        if user_path.lower() == "q":
            print("Exiting Text File Analysis project...")
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
                    analyze_file(file)
            except Exception as e:
                print(f"Failed to open file: {e}")
        else:
            print("Invalid file or file not found. Please provide a valid .txt file.")

if __name__ == "__main__":
    main()