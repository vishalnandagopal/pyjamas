from os.path import dirname as dirname
from random import choice as randchoice
from random import shuffle as randshuffle


def get_word_list(
    relative_filename_of_wordlist: str = "./../static/wordlist.txt",
) -> list[str]:

    filename_word_list = dirname(__file__) + relative_filename_of_wordlist
    with open(filename_word_list, "r") as f:
        return f.readlines()


def passphrase_generator(no_of_words: int = 3) -> str:
    word_list = get_word_list()
    passphrase = ""
    for i in range(no_of_words):
        passphrase += "-" + randchoice(word_list).strip()
    return passphrase.strip("-")


def password_generator(
    no_of_chars: int = 20,
    include_uppercase: bool = True,
    include_numbers: bool = True,
    include_special_characters: bool = True,
) -> str:
    import string

    password: str = ""
    chars: list
    if include_uppercase:
        chars = list(string.ascii_letters)
    else:
        chars = list(string.ascii_lowercase)

    if include_numbers:
        chars += list("1234567890")
    if include_special_characters:
        chars += list("~`! @#$%^&*()_-+={[}]|\\:;\<,>.?/")
    randshuffle(chars)
    for i in range(no_of_chars):
        password += randchoice(chars)
    return password
