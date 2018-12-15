import file_handling
import random


filename = "capitals.txt"
miss_letter = []


def choice_word():
    capitals = file_handling.import_data(filename)
    choice = random.choice(capitals)
    word = ("".join(choice)).lower()
    return word


def convert_word_to_set_of_letters(word):
    letters_word = [char for char in str(word)]
    return set(letters_word)


def hide_word_by_user(word):
    hide_word = "-"*len(word)
    print(hide_word)


hide_word_by_user("word")
