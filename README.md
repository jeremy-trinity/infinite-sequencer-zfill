# infinite-sequencer-zfill 🚀

A smart, dual-mode Python toolkit designed to bring perfect order to file directories. Whether you need visually perfect sorting or database-safe permanent IDs, this suite handles it automatically.

## ✨ Key Features

* **Dual Modes:** Choose between **Dynamic** (visual alignment) or **Static** (database safe).
* **Sequence Memory:** Both scripts automatically detect the highest existing number in the folder and start new files from the next available ID.
* **Space Removal:** Automatically strips all spaces from filenames for cleaner, web-friendly naming.
* **Self-Exclusion:** Automatically ignores `sequencerStatic.py`, `sequencerDynamic.py`, and any `CHANGES` versions.

## 🛠️ Choose Your Mode

### 1. Dynamic Mode (`sequencerDynamic.py`)
**Best for:** General organization and perfect sorting.
* **Retroactive Padding:** If your folder grows from 9 to 10 files, it automatically updates `1_` to `01_` so everything stays aligned.
* **Visual Symmetry:** Ensures all files have the same number of digits.

### 2. Static Mode (`sequencerStatic.py`)
**Best for:** Databases, Web Development, and API references.
* **Permanent IDs:** Once a number is assigned, it **never** changes. 
* **Safe Links:** Prevents broken references by ensuring `12_file.html` never becomes `012_file.html`.

## 🚀 Usage

1. Place the desired script in the directory you wish to organize.
2. Run the script via terminal:
    ```bash
    # For perfect sorting:
    python sequencerDynamic.py

    # For permanent IDs:
    python sequencerStatic.py
    ```

## 📝 Rules & Best Practices

* **The "CHANGES" Rule:** If modifying these scripts, create a copy named `sequencerStaticCHANGES.py` or `sequencerDynamicCHANGES.py` to test new logic before updating the main files.
* **Git Integration:** Always commit your changes after running the sequencer to maintain a clear version history.

---
*Created by [jeremy-trinity](https://github.com/jeremy-trinity) - 2026*
