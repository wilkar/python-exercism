def square(number):
    if number not in range(1, 65):
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number - 1)


def total():
    total_grains = 0
    for sq in range(1, 65):
        total_grains = total_grains + square(sq)
    return total_grains
