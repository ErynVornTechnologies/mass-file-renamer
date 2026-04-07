# Mass File Renamer

A simple, interactive Python script for safely and quickly batch-renaming files inside a folder while maintaining their original extensions. It will automatically pad the file numbering with zeros to ensure correct alphabetical sorting (e.g. `_01`, `_02`... instead of `_1`, `_2`).

## Features

- **Interactive Prompts**: No need to fiddle with command-line arguments.
- **Auto-Padding**: Smartly pads numbers with zeroes according to the amount of files.
- **Extension Safekeeping**: Recognizes and saves the original file extension automatically.
- **Path Cleanup**: Automatically strips out Windows "Copy as path" quotation marks.

## How to use

1. Open your terminal or command prompt.
2. Run the script:
   ```bash
   python rename_files.py
   ```
3. When prompted:
   - Provide the **full directory path** containing the files you wish to rename.
   - Enter your desired **base name** (e.g., `Holiday_Picture`).
4. Read the terminal output to confirm the renaming. All files will now follow the format `Holiday_Picture_01.jpg`, `Holiday_Picture_02.jpg`, etc.

## Requirements

- Python 3.x
- Built-in `os` library (no external installations required).