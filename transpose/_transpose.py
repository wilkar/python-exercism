def transpose(text: str) -> str:
    if not text:
        return ""

    data = text.split("\n")

    if not data or not any(data):
        return ""

    max_len = max(len(row) for row in data)
    x = range(max_len)
    y = range(len(data))

    transposed_string = iterate_letters(y, data, x)

    return transposed_string


def iterate_rows(y_range: range, data: list[str], col_index: int) -> str:
    line_parts: list = []
    last_char_provider_pos = -1

    for i, row_index in enumerate(y_range):
        if col_index < len(data[row_index]):
            line_parts.append(data[row_index][col_index])
            last_char_provider_pos = i
        else:
            line_parts.append(" ")

    return "".join(line_parts[: last_char_provider_pos + 1])


def iterate_letters(y_range: range, data: list[str], x_range: range) -> str:
    list_of_transposed_strings: list = []
    for col_index in x_range:
        list_of_transposed_strings.append(iterate_rows(y_range, data, col_index))
    return "\n".join(list_of_transposed_strings)
