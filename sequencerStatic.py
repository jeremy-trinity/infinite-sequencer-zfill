import os
import re

def rename_files(directory="."):
    # 1. Get all files and identify existing IDs
    all_files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    all_files.sort()

    highest_id = 0
    new_files = []

    for f in all_files:
        if f.startswith("sequencer"):
            continue
        
        match = re.match(r'^(\d+)_', f)
        if match:
            # Track the highest ID, but DO NOT add these to a list to be renamed
            current_id = int(match.group(1))
            if current_id > highest_id:
                highest_id = current_id
        else:
            new_files.append(f)

    if not new_files:
        print("No new files to number.")
        return

    # 2. Determine padding ONLY for the new files
    # We start from highest_id + 1 and go up to highest_id + len(new_files)
    final_id_prediction = highest_id + len(new_files)
    padding = len(str(final_id_prediction))

    # 3. Rename ONLY the new files
    current_num = highest_id + 1
    for filename in new_files:
        clean_name = filename.replace(" ", "")
        # Apply padding to the new ID
        prefix = str(current_num).zfill(padding)
        new_name = f"{prefix}_{clean_name}"
        
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))
        print(f"Assigned Static ID: {filename} -> {new_name}")
        current_num += 1

if __name__ == "__main__":
    rename_files()
