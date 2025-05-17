import os
import shutil

def cpFile(filenames, dest_path):
    """
    Purpose:
        Copy one or more files from the 'vaspFiles' directory inside the Automated-Vacancy-Formation-Energy-Calculator
        to a specified destination path.

    Inputs:
        filenames (str or list of str): Name(s) of the file(s) inside the 'vaspFiles' directory to copy.
        dest_path (str): Destination directory (not full file paths). All files will be copied into this folder.

    Outputs:
        None. Copies the file(s) to the destination. Raises exceptions if errors occur.
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    vasp_dir = os.path.join(script_dir, 'vaspFiles')

    if isinstance(filenames, str):
        filenames = [filenames]

    for filename in filenames:
        src_path = os.path.join(vasp_dir, filename)
        dst_path = os.path.join(dest_path, filename)

        if not os.path.isfile(src_path):
            raise FileNotFoundError(f"Source file not found: {src_path}")
        
        try:
            shutil.copy2(src_path, dst_path)
        except Exception as e:
            raise Exception(f"Error copying {filename}: {e}")

