import re


def check_pattern(string):
    pattern = r"\([-]?\d+(\.\d+)?,[-]?\d+(\.\d+)?\)(?:,\([-]?\d+(\.\d+)?,[-]?\d+(\.\d+)?\))*"
    match = re.fullmatch(pattern, string)
    return bool(match)


def string_to_tuples(string):
    tuple_list = []

    # Remove the parentheses and split the string by comma and parentheses
    elements = string.replace("(", "").replace(")", "").split(",")
    if len(elements) % 2 != 0:
        return None
    # Iterate over the elements and create tuples
    for i in range(0, len(elements), 2):
        x = float(elements[i])
        y = float(elements[i + 1])
        tuple_list.append((x, y))

    return tuple_list


def has_letters(string):
    return any(char.isalpha() for char in string)
