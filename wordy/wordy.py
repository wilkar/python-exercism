def answer(question: str):
    operators = ["plus", "minus", "divided", "multiplied"]

    if not question.startswith("What is"):
        raise ValueError("unknown operation")

    question = (
        question.lower()
        .replace("?", "")
        .replace("what is", "")
        .strip()
        .replace(" by", "")
    )
    tokens = question.split()

    print(tokens)
    if len(tokens) == 0:
        raise ValueError("syntax error")

    # Case where the question only has one number.
    if len(tokens) == 1:
        if not _is_int(tokens[0]):
            raise ValueError("syntax error")
        return int(tokens[0])

    # Check for unknown operations
    for token in tokens:
        if token not in operators and not _is_int(token) and token != "by":
            raise ValueError("unknown operation")

    if (
        len(tokens) < 3
        or not _is_int(tokens[0])
        or tokens[1] not in operators
        or not _is_int(tokens[2])
    ):
        raise ValueError("syntax error")

    value = _calculator(int(tokens[0]), int(tokens[2]), tokens[1])
    del tokens[0:3]

    while tokens:
        # Check if the next token sequence is valid before processing.
        if len(tokens) < 2 or tokens[0] not in operators or not _is_int(tokens[1]):
            raise ValueError("syntax error")

        value = _calculator(value, int(tokens[1]), tokens[0])
        del tokens[0:2]

    return value


def _is_int(value: str):
    try:
        int(value)
        return True
    except ValueError:
        return False


def _calculator(digit1: int, digit2: int, operator: str):
    if operator == "plus":
        return digit1 + digit2
    elif operator == "minus":
        return digit1 - digit2
    elif operator == "divided":
        return digit1 // digit2
    else:
        return digit1 * digit2


# print(answer("Who is the President of the United States?"))
