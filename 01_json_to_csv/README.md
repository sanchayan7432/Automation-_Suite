# JSON to CSV Converter

## Description
Converts JSON files into CSV format.
Supports single JSON objects and lists of objects, and flattens nested data automatically.

**YouTube Video:**
[[Python File & Folder Automation – Project 1: JSON to CSV Converter](https://youtu.be/d3NOSTWauDo?si=GUKU1u5xfOoaDQB3/)]

## Modules Used
- `pathlib` – for working with file paths
- `json` – for parsing JSON files
- `pandas` – for creating and saving CSV files

## Dataset
- Source: Any JSON file (single object or list of objects)  
- Example Input

```json
{
  "id": 1,
  "name": "Sabir Hussain",
  "username": "sabirhussainbalal",
  "email": "sabirhussain@example.com",
  "phone": "+92-000-000-000",
  "address": {
    "street": "Irrigation Colony",
    "city": "Hyderabad",
    "zip": "71000"
  },
  "roles": ["Coder", "Loser"],
  "isActive": true,
  "born": "21-May"
}
```

## Features
- Handles single or multiple JSON records
- Flattens nested dictionaries using dot notation
- Converts list values into separate columns (one-hot style)
- Automatically creates output folder
- Safely overwrites existing CSV

## Project Structure
```
01_json_to_csv/
├── input/
│ ├── data.json
│ └── single.json
├── output/
│ └── data.csv
├── main.py
└── README.md

```


