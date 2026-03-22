# XML to JSON Converter

## Description
Converts XML files into JSON format.
Supports both single-record and multi-record XML structures.

## Modules Used
- `pathlib` – for working with file paths
- `xml.etree.ElementTree` – for parsing XML files
- `json` – for creating JSON output

## Dataset
- Example Input

```xml
<?xml version="1.0" encoding="UTF-8"?>
<users>
    <user>
        <id>1</id>
        <name>Alice Johnson</name>
        <username>alicej</username>
        <email>alice.johnson@example.com</email>
        <phone>+1-202-555-0147</phone>
        <isActive>true</isActive>
        <createdAt>2024-05-12T10:15:30Z</createdAt>
    </user>

    <user>
        <id>2</id>
        <name>Bob Smith</name>
        <username>bobsmith</username>
        <email>bob.smith@example.com</email>
        <phone>+1-202-555-0199</phone>
        <isActive>false</isActive>
        <createdAt>2024-06-01T14:22:10Z</createdAt>
    </user>

</users>

```

## Features
- Load XML files from user input or default path
- Convert flat XML data to JSON
- Handles missing paths and invalid XML safely
- Automatically creates output/ folder
- Saves output as data.json


## Project Structure
```
02_xml_to_json/
├── input/
│ ├── data.xml
│ └── single.xml
├── output/
│ └── data.json
├── main.py
└── README.md
```

*Note:*

**Nested XML elements are intentionally ignored in this version to keep the logic beginner-friendly.**
