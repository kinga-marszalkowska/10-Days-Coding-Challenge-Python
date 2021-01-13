from string import punctuation, ascii_lowercase, ascii_uppercase, digits
from secrets import randbelow, choice
import random
import requests

words = ["exclamation_mark", "quote", "hash", "dollar", "percent", "and", "sign", "brackets", "brackets",
         "asterisk", "add", "comma", "subtract", "do", "slash", "colon", "semi-colon", "less", "equality", "greater",
         "question_mark", "at", "brackets", "slash", "brackets", "caret", "underscore", "tick", "brackets",
         "line", "brackets", "tilda"
         ]
# translate punctuation signs into words
punctuation_words = dict()
for i in range(len(list(punctuation))):
    punctuation_words[list(punctuation)[i]] = words[i]


class Response:
    word: str
    code: int

    def __init__(self, word, code):
        self.word = word
        self.code = code

    def is_correct(self):
        if self.code == 200:
            return True
        else:
            return False


def get_word(url):
    try:
        request = requests.request("GET", url).json()
        number = randbelow(int(len(request)/2))
        # return a word, and a success code 200 - OK
        response = Response(request[number]["word"], 200)
    except ValueError:
        # return a generic word, just in case nothing matches and 404 error code
        response = Response("and", 404)
    return response


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
    mnemo = ""
    for i in range(len(password)):
        # if it is a letter, get a word that starts with it
        if password[i] in ascii_lowercase or password[i] in ascii_uppercase:
            mnemo += get_word("http://api.datamuse.com/words?sp={i}*".format(i=password[i])).word + " "

        elif password[i] in list(punctuation):
            # for sign, get a word that spells similarly to the punctuation sign
            word_spell = get_word("http://api.datamuse.com/words?rel_sp={i}".format(i=punctuation_words[password[i]]))
            # if there is such a word, append it to the answer
            if word_spell.is_correct():
                mnemo += word_spell.word + " "
            # if there is no such word, try with rhymes
            else:
                # get a word that rhymes with this punctuation sign
                word_rhyme = get_word("http://api.datamuse.com/words?rel_rhy={i}".format(i=punctuation_words[password[i]]))
                if word_rhyme.is_correct():
                    mnemo += word_rhyme.word + " "
                # if there are no rhymes return generic word
                else:
                    mnemo += word_rhyme.word + " "
        elif password[i] in digits:
            mnemo += str(password[i]) + " "
    return mnemo


if __name__ == '__main__':
    password_length = int(input("Password length: "))
    special_chars = input("Include special chars? [y/n]: ")

    print("Choose the one that you like the most: ")
    print(generate_mnemonics(generate_password(special_chars, password_length)))
    print(generate_mnemonics(generate_password(special_chars, password_length)))
    print(generate_mnemonics(generate_password(special_chars, password_length)))

