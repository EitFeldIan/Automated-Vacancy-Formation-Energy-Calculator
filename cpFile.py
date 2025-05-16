import os
import shutil

def cpFile(filename, dest_path):
    """
    Purpose:
        Copy a file from the Automated-Vacancy-Formation-Energy-Calculator directory
        (the directory where this script resides) to a specified destination path.

    Inputs:
        filename (str): Name of the file inside the AVFEC directory to copy.
        dest_path (str): Full destination path (including filename) where the file will be copied.

    Outputs:
        None. Copies the file to the destination. Raises exceptions if errors occur.
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    src_path = os.path.join(script_dir, filename)
    
    if not os.path.isfile(src_path):
        raise FileNotFoundError(f"Source file not found: {src_path}")
    
    try:
        shutil.copy2(src_path, dest_path)
        print(f"Copied '{src_path}' to '{dest_path}'")
    except Exception as e:
        raise Exception(f"Error copying file: {e}")
