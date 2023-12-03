from typing import Generator, Any

SEATS = ["A", "B", "C", "D"]


def generate_seat_letters(number) -> Generator[str, Any, None]:
    for i in range(number):
        index = i % 4
        yield SEATS[index]


def generate_seats(number) -> Generator[str, Any, None]:
    seat_count = 0

    for row in range(1, number // 4 + 2):
        if row == 13:
            continue
        for seat in SEATS:
            if seat_count == number:
                return
            yield f"{row}{seat}"
            seat_count += 1


def assign_seats(passengers) -> dict:
    seats = generate_seats(len(passengers))
    return {passenger: next(seats) for passenger in passengers}


def generate_codes(seat_numbers, flight_id) -> Generator[str, Any, None]:
    for seat_number in seat_numbers:
        if len(seat_number) == 3:
            control_chars = "000"
        elif len(seat_number) == 4:
            control_chars = "00"
        yield f"{seat_number}{flight_id}{control_chars}"
