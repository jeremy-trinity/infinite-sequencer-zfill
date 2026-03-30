import os
import re

def rename_files(directory="."):
    # Get all files and sort them to ensure consistent order
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    files.sort()

    # Filter out files that already start with 3 or more digits followed by '_'
    files_to_rename = []
    for f in files:
        if not re.match(r'^\d{3,}_', f):
            files_to_rename.append(f)

    if not files_to_rename:
        print("No files need renaming.")
        return

    total_files = len(files_to_rename)
    
    # Determine padding based on the number of files
    # If 99 files, we need 3 digits (099) to allow for growth, etc.
    padding = len(str(total_files))
    if padding < 2:
        padding = 2

    for index, filename in enumerate(files_to_rename, start=1):
        # Remove spaces from the original name
        clean_name = filename.replace(" ", "")
        
        # Create the new prefix with dynamic padding
        prefix = str(index).zfill(padding)
        new_name = f"{prefix}_{clean_name}"
        
        old_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, new_name)
        
        os.rename(old_path, new_path)
        print(f"Renamed: {filename} -> {new_name}")

if __name__ == "__main__":
    rename_files()
