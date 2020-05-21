# Resolve the problem!!
import string
from random import randint, choice, sample

SYMBOLS = list('!"#$%&\'()*+,-./:;?@[]^_`{|}~')

def generate_password():
    LETTERS = string.ascii_letters
    UPPER_LETERS = LETTERS[int(len(LETTERS)/2):]
    LOWER_LETTERS = LETTERS[:int(len(LETTERS)/2)]
    DIGITS = string.digits
    size = randint(8,16)
    password = []
    
    while len(password) <= size:
        password += sample(SYMBOLS, randint(1,4)) +sample(UPPER_LETERS, randint(1,4)) + sample(DIGITS, randint(1,4)) + sample(LOWER_LETTERS, randint(1,4))

    password = password[:size]

    return ''.join(sample(password, len(password)))


def validate(password):
    if len(password) >= 8 and len(password) <= 16:
        has_lowercase_letters = False
        has_numbers = False
        has_uppercase_letters = False
        has_symbols = False

        for char in password:
            if char in string.ascii_lowercase:
                has_lowercase_letters = True
                break

        for char in password:
            if char in string.ascii_uppercase:
                has_uppercase_letters = True
                break

        for char in password:
            if char in string.digits:
                has_numbers = True
                break

        for char in password:
            if char in SYMBOLS:
                has_symbols = True
                break

        if has_symbols and has_numbers and has_lowercase_letters and has_uppercase_letters:
            return True
    return False


def run():
    password = generate_password()
    if validate(password):
        print('Secure Password')
    else:
        print('Insecure Password')


if __name__ == '__main__':
    run()
