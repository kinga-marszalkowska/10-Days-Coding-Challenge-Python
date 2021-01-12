from string import punctuation, ascii_lowercase, ascii_uppercase, digits
from secrets import randbelow, choice
import random
import requests


def get_word(url):
    # adjectives for a noun "http://api.datamuse.com/words?rel_jjb=beach"
    print(requests.request("GET", url).json()[0]["word"])
    return requests.request("GET", url).json()[0]["word"]


def generate_password(special_chars, password_length):
    password = ""
    # get all possible characters and join them into a list a-z A-Z 0-9 are inputted from 1 to 3 times
    # (to increase their chances of being chosen)
    all_chars = list(ascii_lowercase) * (randbelow(3) + 1) + list(ascii_uppercase) * (randbelow(3) + 1) + list(digits) * (randbelow(3) + 1)
    if special_chars == "y":
        all_chars += list(punctuation) * (randbelow(2) + 1)
    # shuffle all chars
    random.shuffle(all_chars)

    for i in range(password_length):
        password += choice(all_chars)

    print(password)
    return password


def generate_mnemonics(password):
    #todo add words that start with a given letter
    mnemo = ""
    for i in range(len(password)):
        if str(i) in ascii_lowercase or str(i) in ascii_uppercase:
            mnemo += get_word("http://api.datamuse.com/words?sp={i}*".format(i=password[i])) + " "
    return mnemo


if __name__ == '__main__':
    password_length = 10
        # int(input("Password length: "))
    special_chars = "y"
        # input("Include special chars? [y/n]: ")

    print("Choose the one that you like the most: ")
    # print(generate_mnemonics(generate_password(special_chars, password_length)))
    generate_password(special_chars, password_length)
    generate_password(special_chars, password_length)

