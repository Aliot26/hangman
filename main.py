import display
import controller


def main():
    """
    Calls all interaction between user and program, handles program
    and user inputs. 
    """
    display.print_hello()
    display.print_message(controller.choice_word())


if __name__ == '__main__':
    main()
