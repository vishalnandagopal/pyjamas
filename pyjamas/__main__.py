from getpass import getpass
from .database import store_in_database as store_in_database

""" Take username and password input from user and store them in database."""
entered_username = input("Enter your username: ")
plain_text_password = getpass("Enter password: ")
store_in_database(
    entered_username,
    plain_text_password,
    "review-1-testing.csv",
)
