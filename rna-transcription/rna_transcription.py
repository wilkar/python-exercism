def to_rna(dna_strand) -> str:
    mapping: dict = {"G": "C", "C": "G", "T": "A", "A": "U"}

    dna_strand_list = list(dna_strand)
    rna_strand_list: list = []
    if not dna_strand:
        return ""

    for dna_element in dna_strand_list:
        rna_element = mapping.get(dna_element)
        rna_strand_list.append(rna_element)

    return "".join(rna_strand_list)
