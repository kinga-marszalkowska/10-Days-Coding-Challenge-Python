import re
from selenium import webdriver


def palindrome(phrase):
    # clean the input (remove spaces and non-letters)
    cleaned_input = phrase.lower().replace(' ', '')
    cleaned_input = re.sub('[,.]', '', cleaned_input)
    reverse = cleaned_input[:: -1]
    # if input and it's reverse return true i.e. the phrase is a palindrome
    return cleaned_input == reverse


def anagram(word):
    # initialize webdriver
    driver = webdriver.Chrome()
    # navigate to a page, add the inputted word at the end of the Url
    driver.get("https://poocoo.pl/scrabble-slowa-z-liter/"+word)
    # confirm we are on the right page using page's title
    assert "Słowa z liter" in driver.title
    # get all the tags from scrabble-result class (inspect page to find out)
    tags = driver.find_elements_by_class_name("scrabble-result")
    # print all the words
    print(tags[0].text)

    assert "No results found." not in driver.page_source
    driver.close()


def start():
    anagram(input("Give a word to find anagrams: "))

    if palindrome(input("Give a phrase to check if it's a palindrome: ")):
        print("It is a palindrome")
    else:
        print("No, it's not a palindrome")


start()

