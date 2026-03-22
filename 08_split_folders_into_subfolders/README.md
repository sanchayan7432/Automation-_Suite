# Split Folders into Subfolders

## Description
Splits all files from a folder, including nested ones, into multiple subfolders in output/. Each subfolder has a fixed number of files, duplicates are renamed automatically, and the output folder is cleared before running.

For example:
- Input folder contains 34 files → Output:

```
output/
├── folder1/  # 9 files
├── folder2/  # 9 files
├── folder3/  # 9 files
├── folder4/  # 7 files
```


**Note:** ***Dummy files exist in the `test/` folder.  
Copy them to the `input/` folder or provide a custom path, then run `main.py`.***

## Modules Used
- `pathlib` – for safe and modern file/folder path handling
- `shutil` – for moving files and folders to the output folder

## Features
- Works with nested folders — collects all files recursively.
- Creates new folders automatically in the output folder.
- Handles duplicate file names without overwriting.
- Safely deletes old output folder if it exists.
- Beginner-friendly and readable code.


## Project Structure
```
08_split_folders_into_subfolders/
├── input/
│   └── ...           # default folder
├── output/           
│   └── ...           # Folders will be created here after running
├── test/             # Dummy data for testing
├── main.py
└── README.md

```
