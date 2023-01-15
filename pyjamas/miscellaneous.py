import os
"""  Checks if the given file or folder exists in the directory and change the directory accordingly"""

def check_if_exists_in_directory(file_or_folder_name: str, directory: str = "") -> bool:
    current_working_dir = os.getcwd()
    try:
        if directory:
            os.chdir(directory)
        return file_or_folder_name in os.listdir()
    except FileNotFoundError:
        return False
    finally:
        os.chdir(current_working_dir)
