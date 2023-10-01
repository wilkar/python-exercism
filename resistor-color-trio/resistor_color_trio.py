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


def label(colors: list[str]) -> str:
    if len(colors) <= 2:
        raise ValueError("At least two colors are needed")

    value = (
        int(_get_base_value(colors[0:2])) * _get_exp(colors[2])
        if len(colors) > 2
        else int(_get_base_value(colors))
    )

    if value >= 10**9:
        return f"{value // 10**9} gigaohms"
    elif value >= 10**6:
        return f"{value // 10**6} megaohms"
    elif value >= 10**3:
        return f"{value // 10**3} kiloohms"
    else:
        return f"{value} ohms"


def _get_exp(color: str) -> int:
    return 10 ** resistors[color]


def _get_base_value(base_colors: list[str]) -> str:
    return "".join([str(resistors[item]) for item in base_colors])
