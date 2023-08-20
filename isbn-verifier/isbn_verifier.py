def is_valid(isbn: str):
    isbn_chars_list = [item for item in isbn.replace("-", "")]

    if not all(char in "0123456789X" for char in isbn_chars_list):
        return False

    if len(isbn_chars_list) != 10:
        return False

    if isbn_chars_list[-1] == "X":
        isbn_chars_list[-1] = "10"

    if any(item.isalpha() for item in isbn_chars_list):
        return False

    numbers = [int(item) for item in isbn_chars_list]

    multiplied_values: list = []
    for multiplier, number in zip(range(10, 0, -1), numbers):
        multiplied_values.append(multiplier * number)

    if sum(multiplied_values) % 11 == 0:
        return True
    return False
