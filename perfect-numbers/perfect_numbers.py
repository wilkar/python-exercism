def classify(number):
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")

    divisors = get_divisors(number)
    
    if sum(divisors) == number:
        return "perfect"
    elif sum(divisors) > number:
        return "abundant"
    else:
        return "deficient"


def get_divisors(number) -> list[int]:
    divisors: list = []
    for n in range(1, number):
        if number % n == 0:
            divisors.append(n)
    return divisors
