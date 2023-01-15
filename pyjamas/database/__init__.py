from .csv_database import store_in_csv as store_in_csv
from .firebase_database import store_in_firebase as store_in_firebase
from ..miscellaneous import load_desired_env_variable


def store_in_database(
    username: str,
    plain_text_password: str,
    database_name: str,
    type_of_db: str = load_desired_env_variable("TYPE_OF_DB"),
):
    if type_of_db:
        if type_of_db.casefold() == "firebase":
            store_in_firebase(username, plain_text_password, database_name)
        else:
            store_in_csv(username, plain_text_password, database_name)
    else:
        store_in_csv(username, plain_text_password, database_name)
