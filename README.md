# infinite-sequencer-zfill 🚀

A smart, state-aware Python utility designed to bring perfect order to file directories. This script renames files with incrementing numeric prefixes, handles dynamic padding automatically, and ensures consistent sorting across your entire folder.

## ✨ Key Features

* **Retroactive Padding:** If your folder grows from 9 to 10 files, the script automatically updates `1_` to `01_` so your files always sort correctly.
* **Sequence Memory:** Automatically detects the highest number in the folder and starts new files from the next available number.
* **Space Removal:** Automatically strips all spaces from filenames for cleaner, web-friendly naming conventions.
* **Self-Exclusion:** Smart enough to skip `sequencer.py` and `sequencerCHANGES.py` automatically.

## 🛠️ How it Works

The script calculates the necessary "zero-fill" (`zfill`) based on the **final total** of files:
* **1-9 files:** Prefixes like `1_`, `2_`...
* **10-99 files:** Automatically ensures all files use `01_`, `02_`...
* **100+ files:** Dynamically scales to `001_` and beyond.

## 🚀 Usage

1. Place `sequencer.py` in the directory you wish to organize.
2. Run the script via terminal:
    ```bash
    python sequencer.py
    ```

## 📝 Rules & Best Practices

* **The "CHANGES" Rule:** If modifying this script, create a copy named `sequencerCHANGES.py` to test new logic before updating the main file.
* **Git Integration:** Always commit your changes after running the sequencer to maintain a clear version history.

---
*Created by [jeremy-trinity](https://github.com/jeremy-trinity) - 2026*
