def import_data(filename):
    """
    Import data from a file to a list. 
    :param str filename: optional, name of the file to be imported
    :returns: list representing data
    :rtype: list
    """
    result = []
    try:
        with open(filename, 'r') as datafile:
            for line in datafile.readlines():
                result.append(line.strip().split(','))
    except FileNotFoundError:
        message = "FileNotFoundError"
        display.print_command_result(message)
    except Exception:
        message = "Unknown error"
        display.print_command_result(message)
    else:
        return result
