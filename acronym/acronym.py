import re


def abbreviate(words: str):
    words = words.replace("_", "")
    words_list = re.split(r"[-\s]+", words.strip())
    letters: list = []
    print(words_list)
    for word in words_list:
        letters.append(word[0])
    return "".join(letters).upper()
