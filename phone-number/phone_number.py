import string


class PhoneNumber:
    def __init__(self, number: str):
        self._pre_processing_validation(number)
        cleaned_number = self._clean_number(number)

        self.number = cleaned_number
        self.area_code = cleaned_number[0:3]

    def pretty(self):
        return f"({self.number[0:3]})-{self.number[3:6]}-{self.number[6:10]}"

    def _clean_number(self, number) -> str:
        digits: list = [char for char in number if char.isnumeric()]

        # # if a phone number has 11 digits, but starts with a number other than 1.
        if len(number) == 11 and number[0] != "1":
            raise ValueError("11 digits must start with 1")

        if len(digits) == 11:
            cleaned_number = "".join(digits[1:])
        else:
            cleaned_number = "".join(digits)

        self._post_processing_validation(cleaned_number)
        return cleaned_number

    def _pre_processing_validation(self, number):
        print(number)
        # # if a phone number has punctuation in place of some digits.
        if any(char in ["!", "?", "@", ":"] for char in number):
            raise ValueError("punctuations not permitted")

        # # if a phone number has letters in place of some digits.
        if any(char in string.ascii_letters for char in number):
            raise ValueError("letters not permitted")

        return number

    def _post_processing_validation(self, number):
        print(number)
        # # if a phone number has less than 10 digits.
        if len(number) < 10:
            raise ValueError("must not be fewer than 10 digits")

        # # if a phone number has more than 11 digits.
        if len(number) > 11:
            raise ValueError("must not be greater than 11 digits")
        # # if a phone number has an exchange code that starts with 0.
        if number[3] == "0":
            raise ValueError("exchange code cannot start with zero")

        # # if a phone number has an exchange code that starts with 1.
        if number[3] == "1":
            raise ValueError("exchange code cannot start with one")

        # # if a phone number has an area code that starts with 0.
        if number[0] == "0":
            raise ValueError("area code cannot start with zero")

        # # if a phone number has an area code that starts with 1.
        if number[0] == "1":
            raise ValueError("area code cannot start with one")
