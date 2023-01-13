import os
from base64 import b64decode, b64encode
from hashlib import sha256

from dotenv import load_dotenv

from .miscellaneous import \
    check_if_exists_in_directory as check_if_exists_in_directory


def hasher(text: str) -> str:
    return sha256(bytes(text, "utf-8")).hexdigest().upper()


def one_time_padder_for_hash(first_hash: str, key: str = None) -> str:
    """
    Function that pads the given text (eg: SHA256 Hash) with the ONE_TIME_PAD_KEY stored in env variable and returns it.
    """

    # Key must be same length as first hash
    if not key:
        if check_if_exists_in_directory("pyjamas.env"):
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
        key = os.getenv("ONE_TIME_PAD_KEY")
    numeric_values = (
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "0",
    )
    if not key or (len(key) != len(first_hash)):
        return first_hash
    length = len(numeric_values)
    cipher_text = "".join(
        [
            numeric_values[
                (numeric_values.index(first_hash[i]) + numeric_values.index(key[i]))
                % length
            ]
            for i in range(len(first_hash))
        ]
    )
    return cipher_text


def salter(username: str) -> str:
    return b64encode(bytes(username, "utf-8")).decode("utf")


def salted_hash_generator(username: str, password: str) -> str:
    return hasher(password + salter(username))


def get_password(username: str, plain_text_password: str) -> str:
    print(username, plain_text_password)
    return one_time_padder_for_hash(
        salted_hash_generator(username, plain_text_password)
    )


def check_password(
    username: str, plain_text_password_to_check: str, password_hash_in_db: str
) -> bool:
    if password_hash_in_db == get_password(username, plain_text_password_to_check):
        return True
    else:
        return False
