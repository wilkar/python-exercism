numbers_to_twenty = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
}
tens_words = {
    2: "twenty",
    3: "thirty",
    4: "forty",
    5: "fifty",
    6: "sixty",
    7: "seventy",
    8: "eighty",
    9: "ninety",
}


def get_number_parts(number: int):
    billion = number // 10**9
    remaining_after_billion = number % 10**9

    million = remaining_after_billion // 10**6
    remaining_after_million = remaining_after_billion % 10**6

    thousand = remaining_after_million // 10**3
    unit = remaining_after_million % 10**3

    number_parts = {
        "billion": billion,
        "million": million,
        "thousand": thousand,
        "": unit,
    }

    return {key: value for key, value in number_parts.items() if value != 0}


def say_hundreds(number: int):
    first_digit = (number // 10**2) % 10
    second_digit = (number // 10**1) % 10
    third_digit = (number // 10**0) % 10

    number_to_say: str = ""

    if first_digit == 0 and second_digit == 0 and third_digit != 0:
        return f"{numbers_to_twenty.get(third_digit)}"

    if first_digit != 0:
        number_to_say = f"{number_to_say}{numbers_to_twenty.get(first_digit)} hundred "

    if second_digit == 1 and third_digit is not None:
        return (
            f"{number_to_say}{numbers_to_twenty.get(second_digit * 10 + third_digit)}"
        )
    if second_digit >= 2 and third_digit == 0:
        return f"{number_to_say}{tens_words.get(second_digit)}"

    if second_digit >= 2 and third_digit != 0:
        return f"{number_to_say}{tens_words.get(second_digit)}-{numbers_to_twenty.get(third_digit)}"

    return number_to_say


def say_func(number: int):
    if number < 0 or number > 999999999999:
        raise ValueError("input out of range")

    if number == 0:
        return "zero"

    parts = get_number_parts(number)
    complete_number_to_say: str = ""

    for part, value in parts.items():
        complete_number_to_say = (
            f"{complete_number_to_say}{say_hundreds(value)} {part} "
        )

    return complete_number_to_say.rstrip()
