import string


def is_pangram(sentence):
    alphabet = string.ascii_lowercase
    sentence = sentence.lower()
    return all(letter in sentence for letter in alphabet)
