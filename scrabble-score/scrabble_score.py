score_dict = {
    1: ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
    2: ["D", "G"],
    3: ["B", "C", "M", "P"],
    4: ["F", "H", "V", "W", "Y"],
    5: ["K"],
    8: ["J", "X"],
    10: ["Q", "Z"],
}


def score(word: str) -> int:
    score: int = 0
    for letter in word.upper():
        for key, value in score_dict.items():
            if letter in value:
                score += key

    return score
