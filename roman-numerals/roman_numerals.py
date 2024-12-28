mapping = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}

special_cases = {
    "DCCCC": "CM",
    "CCCC": "CD",
    "LXXXX": "XC",
    "XXXX": "XL",
    "VIIII": "IX",
    "IIII": "IV",
}


def prepare_dict(number: int) -> dict:
    number_parts: dict = {}
    remaining_value = number

    for item, value in sorted(mapping.items(), key=lambda x: x[1], reverse=True):
        multiplier = remaining_value // value
        remaining_number = remaining_value % value
        number_part = {"multiplier": multiplier, "remaining_part": remaining_number}

        number_parts[item] = number_part
        remaining_value = remaining_number
    return number_parts


def roman(number: int) -> str:
    roman_dict = prepare_dict(number)
    roman_number: list = []
    for item, value in roman_dict.items():
        if value["multiplier"] == 0:
            continue
        roman_number.append(item * value["multiplier"])
    naive_roman_number = "".join(roman_number)

    for old, new in special_cases.items():
        naive_roman_number = naive_roman_number.replace(old, new)

    return naive_roman_number
