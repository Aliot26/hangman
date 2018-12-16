import os


def print_hello():
    print('HELLO')
    print("RULES OF THE GAME")


def print_word(word):
    print()
    print("Guess the word:")
    print(".".join(word))
    print()


def print_wrong_letters(wrong_letters):
    print()
    print("List of wrong letters: ", wrong_letters)
    print()


def print_message(msg):
    print()
    print(msg)
    print()


def print_header(life, wrong_letters, hide_word):
    os.system("clear")
    print_message("Life : {}".format(life))
    print_wrong_letters(wrong_letters)
    print_word(hide_word)
