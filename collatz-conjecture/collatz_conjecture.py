def steps(number) -> int:
    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    iterations: int = 0
    while number != 1:
        if number % 2 == 0:
            number = int(number / 2)
        else:
            number = 3 * number + 1
        iterations = iterations + 1
    return iterations
