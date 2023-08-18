def colors_list():
    colors = [
        "black",
        "brown",
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "violet",
        "grey",
        "white",
    ]
    return colors


def value(colors: list):
    resistor_values: list = []
    for color in colors[:2]:
        resistor_values.append(str(colors_list().index(color)))
    return int("".join(resistor_values))
