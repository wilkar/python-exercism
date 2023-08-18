"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    return list(args)


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :parm each_wagons_id: list - the list of wagons.
    :parm missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    id_one = each_wagons_id.index(1)
    print(id_one)

    first, second, *remaining_vagons = each_wagons_id
    first_value = each_wagons_id[id_one]
    remaining_vagons.remove(first_value)
    combined_wagons = first_value, *missing_wagons, *remaining_vagons, first, second
    combined_wagons_list = list(combined_wagons)

    return combined_wagons_list


def add_missing_stops(route, **stops):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    stops_list: list = []
    for stop in stops:
        stops_list.append(stops[stop])
    converted_stops = {"stops": stops_list}
    route_with_stops = {**route, **converted_stops}
    return route_with_stops


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    return {**route, **more_route_information}


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    return [list(wagon) for wagon in zip(*wagons_rows)]