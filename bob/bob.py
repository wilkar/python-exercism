def response(hey_bob: str) -> str:
    hey_bob = clean_string(hey_bob)
    print(hey_bob)
    if hey_bob.endswith("?") and hey_bob.isupper() == True:
        return "Calm down, I know what I'm doing!"
    elif hey_bob.endswith("?"):
        return "Sure."
    elif hey_bob.isupper() == True:
        return "Whoa, chill out!"
    elif not hey_bob.isprintable() or len(hey_bob) == 0:
        return "Fine. Be that way!"
    else:
        return "Whatever."


def clean_string(text: str):
    return text.strip().replace("\t", "").replace("\n", "").replace("\r", "")
