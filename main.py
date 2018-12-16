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
    letter_of_word = controller.convert_word_to_set_of_letters(word)
    display.print_word(word)
    hide_word = controller.hide_word_by_user(word)
    print(letter_of_word)
    while life > 0:
        display.print_word(hide_word)
        display.print_wrong_letters(wrong_letters)
        guess = controller.get_letter_from_user(wrong_letters)
        print(guess)
        list_letter_index = controller.check_letter_in_word(
            word, hide_word, guess)
        if list_letter_index == []:
            life -= 1
        wrong_letters = controller.update_list_wrong_letters(
            list_letter_index, wrong_letters, guess)
        print(list_letter_index)
        print(wrong_letters)


if __name__ == '__main__':
    main()
