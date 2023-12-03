resistors = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9,
}

tolerance = {
    "grey": 0.05,
    "violet": 0.1,
    "blue": 0.25,
    "green": 0.5,
    "brown": 1,
    "red": 2,
    "gold": 5,
    "silver": 10,
}


def label(colors: list[str]) -> list:
    if len(colors) <= 2:
        print(colors[0])
        return [str(resistors[colors[0]]), "ohms"]
    if len(colors) == 4:
        value = (
            int(_get_base_value(colors[0:2])) * _get_exp(colors[2])
            if len(colors) > 2
            else int(_get_base_value(colors))
        )
    elif len(colors) == 5:
        value = (
            int(_get_base_value(colors[0:3])) * _get_exp(colors[3])
            if len(colors) > 2
            else int(_get_base_value(colors))
        )

    if value >= 10**9:
        value_and_unit = [value / 10**9, "gigaohms"]
    elif value >= 10**6:
        value_and_unit = [value / 10**6, "megaohms"]
    elif value >= 10**3:
        value_and_unit = [value / 10**3, "kiloohms"]
    else:
        value_and_unit = [value, "ohms"]
    value_and_unit[0] = str(_format_value(value_and_unit[0]))
    return value_and_unit


def _get_exp(color: str) -> int:
    return 10 ** resistors[color]


def _get_base_value(base_colors: list[str]) -> str:
    return "".join([str(resistors[item]) for item in base_colors])


def resistor_label(colors: list[str]) -> str:
    value = label(colors)
    if value[0] == "0":
        return " ".join(value)
    if len(colors) == 4:
        return f'{" ".join(str(v) for v in value)} ±{tolerance[colors[3]]}%'
    return f'{" ".join(str(v) for v in value)} ±{tolerance[colors[4]]}%'


def _format_value(value) -> int | float:
    if isinstance(value, float) and value.is_integer():
        return int(value)
    return value


print(resistor_label(["green", "brown", "orange", "grey"]))
