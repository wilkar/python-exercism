import string


def rows(letter: str) -> list:
    alphabet = string.ascii_uppercase
    index = alphabet.index(letter)
    result: list = []

    for i in range(index + 1):
        result.append(row(alphabet[i], index, i))

    result += result[:-1][::-1]

    return result


def row(letter: str, max_index: int, index: int) -> str:
    if letter == "A":
        return " " * max_index + "A" + " " * max_index

    spaces_between = " " * (2 * index - 1)
    spaces_outer = " " * (max_index - index)

    return f"{spaces_outer}{letter}{spaces_between}{letter}{spaces_outer}"
