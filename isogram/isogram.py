from collections import Counter


def is_isogram(string):
    string = "".join(char for char in string.lower() if char.isalpha())
    var = Counter(string)
    if any((k, v) for k, v in var.items() if v > 1):
        return False
    return True
