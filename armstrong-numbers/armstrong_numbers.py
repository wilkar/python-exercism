def is_armstrong_number(number: int):
    numbers = [int(num) for num in str(number)]
    return number == sum([num ** len(numbers) for num in numbers])
