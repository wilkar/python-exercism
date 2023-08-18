def distance(strand_a, strand_b):
    diff_counter = 0
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")

    for value_a, value_b in zip(strand_a, strand_b):
        if value_a != value_b:
            diff_counter += 1

    return diff_counter
