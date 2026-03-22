# Merge CSV Files

## Description
Merges multiple CSV files from a folder into a single CSV file

Designed to handle files that contain the same columns, even if the column order is different,
This project focuses on working with tabular data and ensuring structural consistency before combining datasets.

## Modules Used
- `pathlib` – for handling file paths
- `pandas` – for reading, concatenating, and writing CSV files

## Dataset
- Source: Any folder containing CSV files
- Example Input

```
order_id,customer,product,quantity,price
1,Alice,Laptop,1,1200
2,Bob,Mouse,2,25
```

## Features
- Reads all .csv files from a folder (default input/ folder or user-specified)
- Skips invalid file types
- Compares columns by name (ignores order)
- Reorders columns to match the first CSV
- Combines all rows into a single CSV
- Resets row index after merging
- Automatically creates output/ folder
- Prints messages for each file processed

## How It Works
1. Scan folder for .csv files
2. Load the first valid CSV as base structure
3. Compare columns of remaining files
4. Reorder columns if necessary
5. Append rows
6. Save merged result to output folder


## Project Structure
```
03_merge_csv_files/
├── input/
│   ├── sales_part1.csv
│   ├── sales_part2.csv
│   └── sales_part3.csv
├── output/
│   └── data.csv
├── main.py
└── README.md
```