def get_input_string(label):
    return input(label)


def get_input_number(label):
    while True:
        try:
            number = int(input(label))
            if number != 1 or number != 2:
                raise ValueError
        except ValueError:
            display.print_message(
                "Please enter 1 if you want to guess the word \n or enter 2 if you want to guess a letter ")
        return input(label)
