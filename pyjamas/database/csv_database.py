import csv
import os
from colorama import Fore

from ..miscellaneous import check_if_exists_in_directory as check_if_exists_in_directory
from ..passwords import (
    check_password as check_password,
    common_password_checker as common_password_checker,
    get_password as get_password,
)


def get_database(database_name: str, type_of_db: str = "csv") -> tuple:
    """
    returns a tuple of reader and writer object given a database name and type (defaults to csv if not provided)
    """

    reader = csv.reader(open(database_name, "r"), delimiter=",", lineterminator="\n")
    writer = csv.writer(open(database_name, "a"), delimiter=",", lineterminator="\n")
    return reader, writer


def write_to_database(row_to_write: tuple, database_name: str, type_of_db: str = "csv"):

    """
    writes header row if database is empty
    checks is entered password is in a list of common passwords and prevents if its present
    writes username with hashed password if already not in database
    """
    reader, writer = get_database(database_name)

    if os.stat(database_name).st_size == 0:
        writer.writerow(("username", "password", "salt_type", "hashing_algo"))

    username = row_to_write[0]
    plain_text_password = row_to_write[1]

    usernames = {row[0] for row in reader}

    if username not in usernames:
        if not common_password_checker.check_if_exists_in_common_passwords_list(
            plain_text_password
        ):
            row_to_write[1] = get_password(username, plain_text_password)
            writer.writerow(row_to_write)
            print(f"Securely stored password for {username}")
        else:
            print("Password is too common, use a strong password.")
    else:
        print(
            f"Username {username} already exists in database, will not be overwritten."
        )
        if authenticate(username, plain_text_password, database_name):
            print(f"{Fore.GREEN}Password for {username} is correct.{Fore.RESET}")
        else:
            print(f"{Fore.RED}Password for {username} is INCORRECT!.{Fore.RESET}")


def authenticate(username: str, plain_text_password: str, database_name: str) -> bool:
    """
    checks if username exists and database and hash of password is same as hashed password in database
    """
    reader, _ = get_database(database_name)

    hashed_pw = [row[1] for row in reader if row[0] == username][0]

    if not hashed_pw:
        return False

    return check_password(username, plain_text_password, hashed_pw)


def store_in_database(
    username: str, plain_text_password: str, database_name: str, type_of_db: str = "csv"
):
    """
    driver function that stores password in database
    """
    if not check_if_exists_in_directory(database_name):
        open(database_name, "w")

    row_to_write = [
        username,
        plain_text_password,
        "b64",
        "sha256",
    ]
    write_to_database(row_to_write, database_name, type_of_db)
