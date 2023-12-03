def sum_of_multiples(limit: int, multiples: list) -> int:
    multiples_list: set = set()
    for item in multiples:
        if item == 0:
            continue
        i = 1
        while True:
            multiple = item * i
            if multiple >= limit:
                break

            multiples_list.add(multiple)
            i += 1

    return sum(multiples_list)


print(sum_of_multiples(1, [0]))
