# Comment in Python
# Generator Password
import random
import string


def pas():
    first_letter = random.choice(string.ascii_letters) + random.choice(
        string.ascii_letters) + random.choice(
        string.ascii_letters) + random.choice(string.ascii_letters)
    num = random.randint(1000, 9999)
    password = first_letter + str(num)
    print(password)


pas()
