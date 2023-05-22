import secrets
import string


def generate_alphanum_crypt_string():
    letters_and_digits = string.ascii_letters + string.digits
    crypt_rand_string = ''.join(secrets.choice(letters_and_digits) for i in range(7))
    return crypt_rand_string

