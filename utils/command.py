import random
import string


def rand_str(lens):
    name = ''.join(random.sample(string.ascii_letters, 1)) + ''.join(
        random.sample(string.ascii_letters + string.digits, lens))
    return name
