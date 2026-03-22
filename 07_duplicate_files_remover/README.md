# Duplicate Files Remover

## Description
Scans a folder for duplicate files based on their content and moves any duplicates into a separate output/ folder. The first copy of each file stays in its original location. This project uses file hashing to safely detect duplicates and helps keep folders clean and organized.

For example:
- Source: Any folder containing files.
- Example files:
```
input/
├── file1.txt
├── file2.txt
├── photo.jpg
├── document.pdf
```

## Modules Used
- `pathlib` – for safe and modern file/folder path handling
- `hashlib` – for generating file hashes to detect duplicate content
- `shutil` – for moving duplicate files to the output folder

## Features
- Detects duplicates by file content (hash comparison)
- Keeps the first occurrence in the original folder
- Moves duplicate files to `output/`
- Handles existing output folder safely
- Works with any file type


## Project Structure
```
07_duplicate_files_remover/
├── input/
│   └── ...           # default folder
├── output/           
│   └── ...           # Duplicates moved here
├── main.py
└── README.md
```



