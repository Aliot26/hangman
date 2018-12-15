import display
import controller
import inputs


def main():
    """
    Calls all interaction between user and program, handles program
    and user inputs. 
    """
    display.print_hello()
    word = controller.choice_word()
    letter_of_word = controller.convert_word_to_set_of_letters(word)
    display.print_word(word)
    hide_word = controller.hide_word_by_user(word)
    print(letter_of_word)
    print(hide_word)
    display.print_word(hide_word)
    guess = controller.get_letter_from_user()
    print(guess)


if __name__ == '__main__':
    main()
