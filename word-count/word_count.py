import re


def count_words(sentence: str) -> dict:
    cleaned = re.sub(r"[^A-Za-z0-9' ,_\t]", "", sentence)

    cleaned = cleaned.replace(",", " ").replace("_", " ").replace("\t", " ").lower()

    words_list = cleaned.split()
    stripped_words = [w.strip("':.!?\n\t,") for w in words_list]

    word_counts: dict = {}
    for word in stripped_words:
        if word:
            word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts
