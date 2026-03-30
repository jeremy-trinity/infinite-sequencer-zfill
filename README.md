# infinite-sequencer-zfill 🚀

A smart, scalable Python utility designed to bring order to chaotic file directories. This script renames files with incrementing numeric prefixes, handles dynamic padding automatically, and cleans up filenames for better compatibility.

## ✨ Key Features

* **Dynamic Padding:** Automatically scales from `01_` to `001_` (and beyond) based on the total number of files.
* **Intelligent Skipping:** Recognizes files that already have a 3-digit prefix (e.g., `001_file.html`) and skips them to avoid double-processing.
* **Space Removal:** Automatically strips all spaces from filenames for cleaner, web-friendly naming conventions.
* **Idempotent:** Safe to run multiple times in the same folder as you add new files.

## 🛠️ How it Works

The script calculates the necessary "zero-fill" (`zfill`) based on your file count:
* **1-99 files:** Prefixes like `01_`, `02_`...
* **100-999 files:** Automatically shifts to `001_`, `002_`...
* **1000+ files:** Scales to `0001_` and so on.

## 🚀 Usage

1.  Place `renamer.py` in the directory you wish to organize.
2.  Run the script via terminal:
    ```bash
    python renamer.py
    ```

## 📝 Rules & Best Practices

* **The "CHANGES" Rule:** If modifying this script, create a copy named `renamerCHANGES.py` to test new logic before updating the main file.
* **Git Integration:** Always commit your changes after running the sequencer to maintain a clear version history.

---
*Created by [jeremy-trinity](https://github.com/jeremy-trinity) - 2026*
