def find(search_list: list[int], value: int):
    start = 0
    end = len(search_list) - 1

    while start <= end:
        mid_index = (start + end) // 2
        mid_item = search_list[mid_index]

        if mid_item == value:
            return mid_index

        if mid_item < value:
            start = mid_index + 1
        else:
            end = mid_index - 1

    raise ValueError("value not in array")
