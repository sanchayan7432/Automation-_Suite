# 06_organize_file_system/main.py
from pathlib import Path
import shutil

BASE_DIR = Path(__file__).resolve().parent

def organize_files(path):
    """Organize files from a folder into categorized subfolders"""
    output_dir = BASE_DIR / "output"
    
    # Delete existing output folder if present
    if output_dir.exists():
        confirm = input("Output folder exists. Delete and continue? (y/n): ").strip().lower()
        if confirm != "y":
            print("Cancelled organization.")
            return
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # File type categories
    categories = {
        "img" : [".jpg", ".jpeg", ".png", ".webp", ".gif", ".bmp", ".tiff", ".svg", ".ico", ".heif", ".heic", ".raw", ".exr", ".dds", ".avif"],
        "doc": [".pdf", ".txt", ".doc", ".docx", ".odt", ".rtf", ".md", ".epub", ".mobi", ".tex"],
        "audio" : [".mp3", ".wav", ".m4a", ".flac", ".aac", ".ogg", ".wma", ".alac"],
        "code" : [".py", ".js", ".java", ".html", ".css", ".cpp", ".c", ".rb", ".go", ".ts", ".php", ".swift", ".sh", ".rs", ".pl"],
        "data" : [".csv", ".json", ".sql", ".xml", ".sqlite", ".xlsx", ".ods", ".log", ".yaml"],
        "archives" : [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz", ".tar.gz", ".tar.bz2", ".tar.xz"],
        "executables" : [".exe", ".msi", ".bat", ".sh", ".app", ".dmg", ".jar", ".run"],
        "video" : [".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv", ".webm", ".mpg", ".mpeg", ".3gp", ".ogv", ".hevc", ".h264", ".vob"],
        "fonts" : [".ttf", ".otf", ".woff", ".woff2", ".eot"],
        "raw" : [".nef", ".cr2", ".arw", ".dng", ".orf", ".raf", ".pef", ".sr2"],
        "vmdk" : [".vmdk", ".vhd", ".vdi"],
        "database" : [".db", ".sqlite", ".mdb", ".accdb"],
        "config": [".ini", ".cfg", ".yml", ".env"]
    }

    records = 0

    try:
        for item in sorted(path.iterdir()):
            if item.is_file():
                records += 1
                ext = "".join(item.suffixes).lower() if len(item.suffixes) > 1 else item.suffix.lower()
                dest = "others"

                for cat, ext_list in categories.items():
                    if ext in ext_list:
                        dest = cat
                        break

                dest_folder = output_dir / dest
                dest_folder.mkdir(parents=True, exist_ok=True)

                try:
                    shutil.move(str(item), str(dest_folder / item.name))
                    print(f"Moved {item.name} → {dest}/")
                except Exception as e:
                    print(f"Error moving {item.name}: {e}")

    except Exception as e:
        print(f"Error during organizing: {e}")

    if records == 0:
        print("No files found to organize.")
    else:
        print(f"{records} files organized successfully.")


def main():
    """Entry point for File System Organizer project"""
    default_folder = BASE_DIR / "input"

    while True:
        print()
        user_path = input("Enter full folder path to organize (or press Enter for default, 'q' to quit): ").strip()
        print()

        if user_path.lower() == "q":
            print("Exiting File System Organizer project...")
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
                organize_files(path)
            except Exception as e:
                print(f"Error: {e}")
        else:
            print("Folder not found. Please enter a valid folder path.")


if __name__ == "__main__":
    main()