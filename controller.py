import file_handling
import random


filename = "capitals.txt"


def choice_word():
    capitals = file_handling.import_data(filename)
    word = random.choice(capitals)
    return word
