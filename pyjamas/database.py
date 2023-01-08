import csv

from .miscellaneous import check_if_exists_in_directory
from .passwords import check_password, get_password


def get_database(database_name: str, type_of_db: str = "csv") -> tuple:
    if type_of_db == "csv":
        if check_if_exists_in_directory(database_name):
            with open(database_name, "r") as csv_file_obj:
                csv_read = csv.reader(csv_file_obj, delimiter=",", lineterminator="\n")
                return tuple(csv_read)


def write_to_database(row_to_write: tuple, database_name: str, type_of_db: str = "csv"):
    header = ("username", "password", "salt_type", "hashing_algo")
    username = row_to_write[0]
    plain_text_password = row_to_write[1]
    if type_of_db == "csv":
        if check_if_exists_in_directory(database_name):
            with open(database_name, "a+") as csv_file_obj:
                csv_write = csv.writer(csv_file_obj, delimiter=",", lineterminator="\n")
                usernames = tuple(
                    row[0] for row in get_database(database_name, type_of_db)[1:]
                )
                if not usernames:
                    csv_write.writerow(header)
                if username not in usernames:
                    csv_write.writerow(row_to_write)
                    print(f"Securely stored password for {username}")
                else:
                    print(
                        f"Username {username} already exists in database, will not be overwritten."
                    )
                    index = usernames.index(username)
                    password_hash_in_db = (get_database(database_name, type_of_db)[1:])[
                        index
                    ][1]
                    if check_password(
                        username, plain_text_password, password_hash_in_db
                    ):
                        print(f"\nCorrect password for user {username}")
                    else:
                        print(f"\nWrong password for user {username}")
                    return
        else:
            with open(database_name, "w") as csv_file_obj:
                csv_write = csv.writer(
                    csv_file_obj, delimiter=",", lineterminator="\n"
                )
                csv_write.writerow(header)
            write_to_database(row_to_write, database_name, type_of_db)


def store_in_database(
    username: str, plain_text_password: str, database_name: str, type_of_db: str = "csv"
):
    row_to_write = (
        username,
        plain_text_password,
        "b64",
        "sha256",
    )
    write_to_database(row_to_write, database_name, type_of_db)
