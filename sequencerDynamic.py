import os
import re

def rename_files(directory="."):
    # 1. Get all files and separate them into "needs numbering" and "already numbered"
    all_files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    all_files.sort()

    numbered_files = [] # Stores (current_number, original_filename)
    new_files = []      # Stores filenames

    for f in all_files:
        if f.startswith("sequencer"):
            continue
        
        match = re.match(r'^(\d+)_', f)
        if match:
            numbered_files.append((int(match.group(1)), f))
        else:
            new_files.append(f)

    if not new_files and not numbered_files:
        print("Folder is empty.")
        return

    # 2. Calculate the NEW highest number and the required padding
    highest_existing = max([n[0] for n in numbered_files]) if numbered_files else 0
    final_total = highest_existing + len(new_files)
    padding = len(str(final_total))

    # 3. Step One: Update OLD files if padding changed (e.g., 8 -> 08)
    for num, filename in numbered_files:
        clean_name = re.sub(r'^\d+_', '', filename).replace(" ", "")
        new_prefix = str(num).zfill(padding)
        new_name = f"{new_prefix}_{clean_name}"
        
        if filename != new_name:
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))
            print(f"Updated Padding: {filename} -> {new_name}")

    # 4. Step Two: Number the NEW files starting from the next available number
    current_num = highest_existing + 1
    for filename in new_files:
        clean_name = filename.replace(" ", "")
        prefix = str(current_num).zfill(padding)
        new_name = f"{prefix}_{clean_name}"
        
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))
        print(f"New Sequence: {filename} -> {new_name}")
        current_num += 1

if __name__ == "__main__":
    rename_files()
