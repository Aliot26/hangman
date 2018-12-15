import file_handling
import random
import inputs
import display

filename = "capitals.txt"
wrong_letters = []


def choice_word():
    capitals = file_handling.import_data(filename)
    choice = random.choice(capitals)
    word = ("".join(choice)).lower()
    return word


def convert_word_to_set_of_letters(word):
    letters_word = [char for char in str(word)]
    return set(letters_word)


def hide_word_by_user(word):
    hide_word = "-" * len(word)
    return hide_word


def get_letter_from_user():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    while True:
        guess = inputs.get_input_string("Please enter a letter ").lower()
        if len(guess) != 1:
            display.print_message("There must be single letter")
        elif guess in wrong_letters:
            display.print_message(
                "You have already guessed this letter. Choose again")
        elif guess not in alphabet:
            display.print_message("This is not a LETTER")
        else:
            return guess


def check_letter_in_word():
    pass
