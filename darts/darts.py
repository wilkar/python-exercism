from math import sqrt

def score(x: int, y: int):
    distance = sqrt(x**2 + y**2)

    if distance <= 1:
        return 10
    elif 1 < distance <= 5:
        return 5
    elif 5 < distance <= 10:
        return 1
    else:
        return 0