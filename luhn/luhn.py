class Luhn:
    def __init__(self, card_num: str):
        self.card_num = card_num

    def valid(self) -> bool:
        self.card_num = self.card_num.replace(" ", "")

        if not self.card_num.isdigit():
            return False

        if len(self.card_num) < 2:
            return False

        if not sum(self.parse_card_number()) % 10 == 0:
            return False

        return True

    def parse_card_number(self) -> list:
        reversed_digits = reversed(self.card_num)
        parsed_digits = []
        for i, digit in enumerate(reversed_digits):
            d = int(digit)
            if i % 2 == 1:
                d *= 2
                if d > 9:
                    d -= 9
            parsed_digits.append(d)
        return parsed_digits
