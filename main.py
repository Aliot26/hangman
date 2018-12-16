import os
import time
import display
import controller
import inputs


def main():
    """
    Calls all interaction between user and program, handles program
    and user inputs. 
    """
    wrong_letters = []
    life = 5
    display.print_hello()
    word = controller.choice_word()
    letter_of_word = controller.convert_word_to_list_of_letters(word)
    display.print_word(word)
    hide_word = controller.hide_word_by_user(word)
    time.sleep(5)
    while life > 0:
        os.system("clear")
        display.print_message("Life : {}".format(life))
        display.print_wrong_letters(wrong_letters)
        display.print_word(hide_word)
        request = inputs.get_input_number(
            "Please enter 1 if you want to guess the word \n or enter 2 if you want to guess a letter ")
        print(request)
        guess = controller.get_letter_from_user(wrong_letters)
        list_letter_index = controller.check_letter_in_word(
            word, guess)
        print(list_letter_index)
        if list_letter_index == []:
            life -= 1
            wrong_letters = controller.update_list_wrong_letters(
                list_letter_index, wrong_letters, guess)
        hide_word = controller.show_guessed_letter(
            list_letter_index, guess, word, hide_word)
        controller.check_win_condition(life, word, hide_word)


if __name__ == '__main__':
    main()
