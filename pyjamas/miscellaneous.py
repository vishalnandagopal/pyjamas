import os
from dotenv import load_dotenv


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


def load_desired_env_variable(env_variable: str, env_file_name: str = "../pyjamas.env"):
    if check_if_exists_in_directory(env_file_name):
        load_dotenv(env_file_name)
    elif check_if_exists_in_directory("pyjamas.env"):
        # print("loading env variables from current directory")
        load_dotenv("pyjamas.env")
    elif check_if_exists_in_directory("pyjamas.env", "pyjamas"):
        current_working_dir = os.getcwd()
        try:
            os.chdir("pyjamas")
            # print("loading env variables from pyjamas directory")
            load_dotenv("pyjamas.env")
        except (NotADirectoryError, FileNotFoundError):
            pass
        finally:
            os.chdir(current_working_dir)
    else:
        # print("loading env variables from environment")
        load_dotenv()
    return os.getenv(env_variable)