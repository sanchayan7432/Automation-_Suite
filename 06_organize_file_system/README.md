# File System Organizer

## Description
Organizes files from a folder into a clean output/ directory based on file type.

For example:
- Images go to `img/`
- Documents go to `doc/`
- Audio files go to `audio/`
- Code files go to `code/`
- Unknown files go to `others/`

This project focuses on file classification, folder creation, and safe file movement.

It helps turn messy folders into a structured directory automatically.

**Note:** ***Dummy files exist in the `test/` folder.  
Copy them to the `input/` folder or provide a custom path, then run `main.py`***

## Modules Used
- `pathlib`, `shutil`

## Features
- Reads all files from a folder (default `input/` or user-specified path)
- Automatically creates categorized folders based on file extensions
- Handles images, documents, audio, video, code, archives, fonts, and more
- Moves unknown file types to an `others/` folder
- Asks for confirmation before deleting old output/ folder


## Project Structure
```
06_organize_file_system/
├── input/
│   └── ...           # Add files to organize here
├── output/
│   └── ...           # Organized folders created here
├── test/             # Contains dummy files for testing
├── main.py
└── README.md
```
