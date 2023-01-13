import os
from base64 import b64decode, b64encode
from hashlib import sha256
from dotenv import load_dotenv

from .miscellaneous import check_if_exists_in_directory as check_if_exists_in_directory


def hasher(text: str) -> str:
    """
    Takes a UTF-8 encoded piece of text of any length, and returns the SHA-256 hash of the text as a string object, in uppercase.
    """
    return sha256(bytes(text, "utf-8")).hexdigest().upper()


def one_time_padder_for_hash(first_hash: str, key: str = None) -> str:
    """
    Function that pads the given text (eg: SHA256 Hash) with the ONE_TIME_PAD_KEY stored in env variable and returns it.
    Key must be same length as first hash
    """
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
        if len(first_hash) < len(key):
            key = key[0 : len(first_hash)]
        else:
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
    """
    Returns the base64 encoded string of the username,
    """
    return b64encode(bytes(username, "utf-8")).decode("utf")


def salted_hash_generator(username: str, password: str) -> str:
    """
    Returns a SHA-256 hash of the the combined string of the following:
    1. Plaintext password
    2. Base 64 string of the username
    """
    return hasher(password + salter(username))


def get_password(username: str, plain_text_password: str) -> str:
    """
    Master algorithm for generating the "final' hash for any combination of password and username.

    All changes to the base algorithm must be made here, and it will automatically be reflected in other places because everything else is calling this function to generate password hashes, instead of doing it on their own everywhere.
    """
    return one_time_padder_for_hash(
        salted_hash_generator(username, plain_text_password)
    )


def check_if_exists_in_common_passwords_list(
    plain_text_password_to_check: str,
    list_of_passwords: str = "./static/common-passwords.txt",
):
    """
    Checks if a password is included in a list of common passwords used online.

    By default, it is a list of 1000 common passwords from the 10 million password list, taken from https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10-million-password-list-top-1000.txt .
    """
    with open(
        os.path.dirname(__file__) + "/" + list_of_passwords,
        "r",
    ) as pw_file_object:
        common_passwords = set(pw_file_object.readlines())
    if (
        plain_text_password_to_check + "\n"
    ) in common_passwords or plain_text_password_to_check in common_passwords:
        return True
    else:
        return False


def check_password(
    username: str, plain_text_password_to_check: str, password_hash_in_db: str
) -> bool:
    """
    Given a password hash from the database, and a username and a plain text password to generate the password hash for, this function checks if they match after calculating the hash.
    """
    if password_hash_in_db == get_password(username, plain_text_password_to_check):
        return True
    else:
        return False
