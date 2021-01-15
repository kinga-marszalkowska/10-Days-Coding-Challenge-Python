from os import listdir
from os.path import isfile, join
from tkinter import filedialog
from tkinter import *
from pprint import pprint
import keyword


def get_all_files():
    # pick file folder
    root = Tk()
    root.withdraw()
    path_to_challenge_folder = filedialog.askdirectory()

    code_files = []
    # get paths to all code files
    for f in listdir(path_to_challenge_folder):
        if isfile(join(path_to_challenge_folder, f)):
            # append all files that start with day and and with .py (only challenge code files)
            if f.startswith("Day") and f.endswith(".py"):
                code_files.append(f)

    return code_files


def code_lines_count(filename):
    try:
        file = open(filename, "r")
        counter = 0
        content = file.read()
        lines = content.split("\n")

        for i in lines:
            # don't count blank lines
            if i is not "":
                # don't count comments or multiline strings
                if not i.startswith("'") and not i.startswith('#'):
                    counter += 1
        return counter
    except FileNotFoundError:
        print("file does not exist")


def unique_words_count(filename):
    # collects also variable names so i.e. all_words is one word
    all_words = dict()
    try:
        file = open(filename, "r")
        content = file.read()
        # get all the lines in a file
        lines = content.split("\n")

        for line in lines:
            # get all the words in a line
            words_in_line = line.split()
            for word in words_in_line:
                try:
                    all_words[word] += 1
                except KeyError:
                    all_words[word] = 1

        return len(all_words.keys())
    except FileNotFoundError:
        print("file does not exist")


def used_keywords_count(filename):
    try:
        file = open(filename, "r")
        content = file.read()
        # get all the lines in a file
        lines = content.split("\n")

        counter = 0
        for line in lines:
            # get all the words in a line
            words_in_line = line.split()
            for word in words_in_line:
                if word in keyword.kwlist:
                    counter += 1
        return counter
    except FileNotFoundError:
        print("file does not exist")


def all_python_modules():
    try:
        # create a list of all available modules
        all_modules = []
        file = open("all_modules.txt", "r")
        content = file.read()
        # get all the lines in a file
        lines = content.split("\n")

        for line in lines:
            for word in line.split():
                all_modules.append(word)
        return all_modules
    except FileNotFoundError:
        print("file does not exist")


def imported_modules(filename):
    try:
        all_modules = all_python_modules()
        # if all modules function didn't work, end
        if all_modules is None or len(all_modules) == 0:
            return
        used_modules = []

        # get all the used modules
        file = open(filename, "r")
        content = file.read()
        # get all the lines in a file
        lines = content.split("\n")

        for line in lines:
            if line.startswith("import") or line.startswith("from"):
                for word in line.split():
                    if word != "import" and word != "from" and word not in used_modules and word in all_modules:
                        used_modules.append(word)

        return used_modules
    except FileNotFoundError:
        print("file does not exist")


all = get_all_files()
total_lines = 0
all_modules = set()
for file in all:
    total_lines += code_lines_count(file)
    print(file, code_lines_count(file))
    print("unique words: ", unique_words_count(file))
    print("keywords count:  ", used_keywords_count(file))
    modules = imported_modules(file)
    for module in modules:
        all_modules.add(module)
    print("modules:  ", modules)

print(total_lines)
print(all_modules)

