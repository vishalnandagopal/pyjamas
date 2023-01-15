from base64 import b64decode, b64encode
from hashlib import sha256

from .ciphers import *
from .common_password_checker import check_if_exists_in_common_passwords_list


def handle_cipher(
    username: str,
    plain_text_password: str = None,
    cipher: str = "pad_hash_with_developer_key",
) -> str:
    cipher = cipher.casefold()
    if cipher == "pad_hash_with_developer_key":
        return pad_hash_with_developer_key(
            salted_hash_generator(username, plain_text_password)
        )
    
    return pad_hash_with_developer_key(
            salted_hash_generator(username, plain_text_password)
        )


def hasher(text: str) -> str:
    """
    Takes a UTF-8 encoded piece of text of any length, and returns the SHA-256 hash of the text as a string object, in uppercase.
    """
    return sha256(bytes(text, "utf-8")).hexdigest().upper()


def salter(username: str) -> str:
    """
    Returns the base64 encoded string of the username,
    """
    return b64encode(bytes(username, "utf-8")).decode("utf")


def salted_hash_generator(username: str, plain_text_password: str) -> str:
    """
    Returns a SHA-256 hash of the the combined string of the following:
    1. Plaintext password
    2. Base 64 string of the username
    """
    return hasher(plain_text_password + salter(username))


def get_password(username: str, plain_text_password: str) -> str:
    """
    Master algorithm for generating the "final' hash for any combination of password and username.

    All changes to the base algorithm must be made here, and it will automatically be reflected in other places because everything else is calling this function to generate password hashes, instead of doing it on their own everywhere.
    """
    return handle_cipher(username, plain_text_password)


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
