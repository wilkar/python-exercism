def slices(series: str, length: int):
    if length == 0:
        raise ValueError("slice length cannot be zero")
    if length < 0:
        raise ValueError("slice length cannot be negative")
    if len(series) == 0:
        raise ValueError("series cannot be empty")
    if length > len(series):
        raise ValueError("slice length cannot be greater than series length")

    slices: list = []
    for i in range(0, len(series)):
        slice = series[i : i + length]
        if len(slice) == length:
            slices.append(slice)

    return slices
