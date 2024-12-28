def proverb_func(*input_data: str, qualifier: str | None = None) -> list:
    if len(input_data) == 0:
        return []
    if len(input_data) >= 2:
        result = get_main_sentences(*input_data)
    else:
        result = []
    if qualifier is None:
        result.append(f"And all for the want of a {input_data[0]}.")
    else:
        result.append(f"And all for the want of a {qualifier} {input_data[0]}.")

    return result


def get_main_sentences(*input_data: str) -> list:
    result: list = []
    for i in range(len(input_data) - 1):
        result.append(f"For want of a {input_data[i]} the {input_data[i+1]} was lost.")
    return result
