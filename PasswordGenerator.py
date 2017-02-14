import random
import string


def password_generator(length, chars=string.ascii_letters + string.digits):
    result = ""
    if length < 8:
        print("Password length can not be less than 8")
    else:
        result = "".join(random.choice(chars) for _ in range(length))
    return result

print(password_generator(10))