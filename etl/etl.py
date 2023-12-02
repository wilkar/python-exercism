LETTER_SCORES = {
    "a": 1,
    "b": 3,
    "c": 3,
    "d": 2,
    "e": 1,
    "f": 4,
    "g": 2,
    "h": 4,
    "i": 1,
    "j": 8,
    "k": 5,
    "l": 1,
    "m": 3,
    "n": 1,
    "o": 1,
    "p": 3,
    "q": 10,
    "r": 1,
    "s": 1,
    "t": 1,
    "u": 1,
    "v": 4,
    "w": 4,
    "x": 8,
    "y": 4,
    "z": 10,
}


def transform(legacy_data: dict) -> dict:
    return_dict: dict = {}
    for key, value in legacy_data.items():
        for letter in value:
            lower_letter = letter.lower()
            if lower_letter in LETTER_SCORES:
                return_dict[lower_letter] = LETTER_SCORES[lower_letter]
    return return_dict
