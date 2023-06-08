from random import choice, randint
from secrets import token_hex
from string import ascii_lowercase


def generate_random_number(length):
    return ''.join(["{}".format(randint(0, 9)) for _ in range(0, length)])


def generate_static_number(length):
    return '999999'


def generate_random_string(length):
    return ''.join(choice(ascii_lowercase) for _ in range(length))


def generate_random_api_key(length: int) -> str:
    return token_hex(length)
