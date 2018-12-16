import display


def get_input_string(label):
    return input(label)


def get_input_number(label):
    numbers = [1, 2]
    while True:
        try:
            number = int(input(label))
            if number not in numbers:
                raise ValueError
        except ValueError:
            display.print_message(
                "Wrong number")
        else:
            return number
