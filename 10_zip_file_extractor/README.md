# Zip File Extractor

## Description
Extracts a ZIP file into the output/ folder. A custom ZIP file path can be provided, or the default ZIP file will be used. Old output is safely deleted before extracting.

For example:
- `data.zip` → Extracted into `output/`

```
output/
├── extracted_folder/   # Contents of ZIP appear here
```

**Note:** ***A sample ZIP file exists in the `test/` folder.  
Copy it to the `input/` folder or provide a custom path, then run `main.py`.***

## Modules Used
- `pathlib` – safe and modern path handling
- `zipfile` – for reading and extracting ZIP archives
- `shutil` – for safe folder removal

## Features
- Extracts valid ZIP files
- Handles default input
- Prevents accidental overwrite
- Simple and readable structure


## Project Structure
```
10_zip_file_extractor/
├── input/
│   └── data.zip      # Default zip file
├── output/           
│   └── ...           # Extracted files appear here
├── test/             # Sample
├── main.py
└── README.md
```