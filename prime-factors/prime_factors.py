from typing import List


def factors(value: int) -> List[int]:
    prime_factors: list = []
    i: int = 2
    while value > 1:
        if value % i == 0:
            prime_factors.append(i)
            value = value / i
        else:
            i += 1
    return prime_factors
