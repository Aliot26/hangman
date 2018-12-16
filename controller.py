import sys
import file_handling
import random
import inputs
import display

filename = "capitals.txt"


def choice_word():
    capitals = file_handling.import_data(filename)
    choice = random.choice(capitals)
    word = ("".join(choice)).lower()
    return word


def convert_word_to_list_of_letters(word):
    letters_word = [char for char in str(word)]
    return letters_word


def hide_word_by_user(word):
    hide_word = "_" * len(word)
    return hide_word


def get_letter_from_user(wrong_letters, hide_word):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    while True:
        guess = inputs.get_input_string("Please enter a letter ").lower()
        if len(guess) != 1:
            display.print_message("There must be single letter")
        elif guess in wrong_letters:
            display.print_message(
                "You have already tried this letter. Choose again")
        elif guess in hide_word:
            display.print_message(
                "You have already guessed this letter. Choose again")
        elif guess not in alphabet:
            display.print_message("This is not a LETTER")
        else:
            return guess


def check_letter_in_word(word, guess):
    list_letter_index = []
    i = 0
    while i < len(word):
        if guess == word[i]:
            list_letter_index.append(i)
        i += 1
    return list_letter_index


def update_list_wrong_letters(list_letter_index, wrong_letters, guess):
    if list_letter_index == []:
        wrong_letters.append(guess)
    return wrong_letters


def show_guessed_letter(list_letter_index, guess, hide_word):
    word_as_list = convert_word_to_list_of_letters(hide_word)
    for el in list_letter_index:
        word_as_list[el] = guess
    hide_word = ''.join(word_as_list)
    return hide_word


def game_over_condition(life):
    if life == 0:
        display.print_message("Life : {}".format(life))
        display.print_message("Guessed  word : {}".format(word))
        display.print_message("GAME OVER")


def check_win_condition(word, hide_word):
    if word == hide_word:
        display.print_word(hide_word)
        display.print_message("YOU WIN!")
        return True
    return False


def check_guessed_word(word, hide_word):
    if check_win_condition(word, hide_word):
        return True
    else:
        display.print_message("You are wrong. This word : {}".format(word))
        display.print_message("GAME OVER")
        return False
