def flatten(iterable: list[any]):
    flatten_list: list = []

    for item in iterable:
        if not isinstance(item, list) and item is not None:
            flatten_list.append(item)
        elif item is not None:
            flatten_list.extend(flatten(item))

    return flatten_list
