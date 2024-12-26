def decode(string: str):
    decoded_string = ""
    counter = ""

    for char in string:
        print(char)
        if char.isdigit():
            counter += char
            print(counter)
        else:
            if counter:
                decoded_string += char * int(counter)
                counter = ""
            else:
                decoded_string += char

    return decoded_string


def encode(string: str):
    if not string:
        return ""

    counter: int = 1
    encoded_string: list = []
    prev_char = string[0]

    for char in string[1:]:
        if char == prev_char:
            counter += 1
        else:
            if counter == 1:
                encoded_string.append(prev_char)
            else:
                encoded_string.append(str(counter) + prev_char)
            prev_char = char
            counter = 1

    if counter == 1:
        encoded_string.append(prev_char)
    else:
        encoded_string.append(str(counter) + prev_char)

    return "".join(encoded_string)
