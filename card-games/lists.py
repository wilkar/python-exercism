"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """

    return [number + num for num in range(3)]


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """

    return rounds_1 + rounds_2


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """

    if number in rounds:
        return True
    return False


def card_average(hand):
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """

    return sum(hand) / len(hand)


def approx_average_is_average(hand):
    """Return if an average is using (first + last index values ) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """

    true_average = sum(hand) / len(hand)
    approx_average_1 = (hand[0] + hand[-1]) / 2
    approx_average_2 = (
        hand[len(hand) // 2]
        if len(hand) % 2
        else (hand[len(hand) // 2] + hand[len(hand) // 2 - 1]) / 2
    )

    return true_average in (approx_average_1, approx_average_2)


def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """

    even_numbers: list = []
    odd_numbers: list = []

    for item in enumerate(hand):
        if item[0] % 2 == 0:
            even_numbers.append(hand[item[0]])
        else:
            odd_numbers.append(hand[item[0]])

    if sum(even_numbers) / len(even_numbers) == sum(odd_numbers) / len(odd_numbers):
        return True
    return False


average_even_is_average_odd([1, 2, 3, 4, 4])


def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """
    if 11 in hand:
        hand[-1] = hand[-1] * 2
    return hand
