from ..miscellaneous import load_env_variable as load_env_variable
from .hasher import hasher

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


def pad_hash_with_developer_key(first_hash: str, key: str = None) -> str:
    """
    Function that pads the given text (eg: SHA256 Hash) with the ONE_TIME_PAD_KEY stored in env variable and returns it.
    Key must be same length as first hash
    """
    key = load_env_variable("ONE_TIME_PAD_KEY")

    if not key:
        return first_hash
    elif len(first_hash) < len(key):
        key = key[0 : len(first_hash)]
    elif len(first_hash) > len(key):
        key = hasher(key)
        return pad_hash_with_developer_key(first_hash, key)
    length = len(numeric_values)
    cipher_text = "".join(
        [
            numeric_values[
                (numeric_values.index(first_hash[i]) + numeric_values.index(key[i])) % length
            ]
            for i in range(len(first_hash))
        ]
    )
    return cipher_text
