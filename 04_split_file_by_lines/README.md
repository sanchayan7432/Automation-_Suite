# Split Text File by Lines

## Description
Splits a .txt file into multiple smaller text files based on a user-defined number of lines per file.

- Built to be simple, safe, and repeatable.
- Old output is automatically replaced on each run.

This project focuses on file reading, writing, and controlled data chunking

## Modules Used
- `pathlib`, `shutil`

## Dataset
- Source: Any .txt file
- Default file: input/story.txt
- Example Input

```
Once upon a quiet evening,
One of the youthful programmers was sitting in front of a light screen.
The code was simple,
But the questions were deep.

He did not rush for shortcuts,
Nor did he reproduce without knowing.
Every line had a purpose,
And every bug was a lesson.

At times, the program was unsuccessful,
At times, the reason was too much.
But step by step,
clarity began to form.

With patience and practice,
Doubt gradually changed to confidence.
And here and there a single project,
The way ahead was made evident.
```

## Features
- Supports any .txt file
- Splits content by number of lines
- Handles remaining lines automatically
- Deletes old output before creating new files
- Automatically creates output folder
- Clear console messages for each step
- Beginner-friendly and readable code


## Project Structure
```
04_split_file_by_lines/
├── input/
│   └── story.txt
├── output/
│   ├── file1.txt
│   ├── file2.txt
│   └── ...
├── main.py
└── README.md
```
