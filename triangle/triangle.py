def is_triangle(sides: list) -> bool:
    if all(side == 0 for side in sides):
        return False
    for side in sides:
        if sum(sides) - side < side:
            return False
    return True


def equilateral(sides: list):
    if is_triangle(sides) is True:
        try:
            iterator = iter(sides)
        except StopIteration:
            print("Error fetching first element from the list. Is the list empty?")
        first = next(iterator)
        if all(first == x for x in iterator):
            return True
    return False


def isosceles(sides: list):
    if is_triangle(sides) is True:
        if len(set(sides)) < 3:
            return True
    return False


def scalene(sides: list):
    if is_triangle(sides) is True:
        if len(set(sides)) == 3:
            return True
    return False
