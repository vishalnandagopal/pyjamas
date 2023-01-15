import os


def check_if_exists_in_common_passwords_list(
    plain_text_password_to_check: str,
    list_of_passwords: str = "./../static/common-passwords.txt",
):
    """
    Checks if a password is included in a list of common passwords used online.

    By default, it is a list of 1000 common passwords from the 10 million password list, taken from https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10-million-password-list-top-1000.txt .
    """
    try:
        with open(
            os.path.dirname(__file__) + "/" + list_of_passwords,
            "r",
        ) as pw_file_object:
            common_passwords = set(pw_file_object.readlines())
    except (FileNotFoundError, NotADirectoryError):
        common_passwords = {
            "password",
            "123456",
            "password",
            "12345678",
            "1234",
            "pussy",
            "12345",
            "dragon",
            "qwerty",
            "696969",
            "letmein",
            "abc123",
            "pass",
        }
    if (
        plain_text_password_to_check + "\n"
    ) in common_passwords or plain_text_password_to_check in common_passwords:
        return True
    else:
        return False
