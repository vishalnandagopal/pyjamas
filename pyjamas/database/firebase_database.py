from ..miscellaneous import check_if_exists_in_directory
from ..passwords import check_password as check_password
from ..passwords import common_password_checker as common_password_checker
from ..passwords import get_password as get_password


def get_database(database_name: str) -> tuple:
    pass


def handle_header_and_creation(database_name: str) -> bool:
    pass

    header = ("username", "password", "salt_type", "hashing_algo")


def write_to_database(row_to_write: tuple, database_name: str):
    username = row_to_write[0]
    plain_text_password = row_to_write[1]


def store_in_database(username: str, plain_text_password: str, database_name: str):
    pass
    row_to_write = [
        username,
        plain_text_password,
        "b64",
        "sha256",
    ]
    write_to_database(row_to_write, database_name)
