import string


def rotate(text: str, key: int):
    rotated_values: list = []
    for letter in text:
        if letter not in list(string.ascii_letters):
            rotated_values.append(letter)
        elif letter in list(string.ascii_uppercase):
            rotated_value = _get_rotated_letter(letter, key)
            rotated_values.append(rotated_value.upper())
        else:
            rotated_value = _get_rotated_letter(letter, key)
            rotated_values.append(rotated_value)

    return "".join(rotated_values)


def _get_rotated_letter(letter: str, key: int) -> int:
    alphabet = list(string.ascii_lowercase)
    index = alphabet.index(letter.lower()) + 1
    rotated_index = (index + key) % 26
    return alphabet[rotated_index - 1]
