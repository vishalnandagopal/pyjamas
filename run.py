import pyjamas, os, dotenv

dotenv.load_dotenv("pyjamas.env")

if os.getenv("TO_INPUT"):
    username = input("Enter your username: ")
    plain_text_password = pyjamas.getpass("Enter your password: ")
    pyjamas.store_in_database(
        username, plain_text_password, "review-1-testing.csv", "csv"
    )
else:
    pyjamas.store_in_database("vishal", "mypw", "review-1-testing.csv", "csv")
