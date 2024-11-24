protein_mapping = {
    "Methionine": ["AUG"],
    "Phenylalanine": ["UUU", "UUC"],
    "Leucine": ["UUA", "UUG"],
    "Serine": ["UCU", "UCC", "UCA", "UCG"],
    "Tyrosine": ["UAU", "UAC"],
    "Cysteine": ["UGU", "UGC"],
    "Tryptophan": ["UGG"],
    "STOP": ["UAA", "UAG", "UGA"],
}


def proteins(strand: str):
    codons = get_codons(strand)
    proteins: list = []
    for codon in codons:
        proteins.append(get_protein(codon))
    return proteins


def get_protein(codon: str) -> str:
    for protein, values in protein_mapping.items():
        if codon in values:
            return protein


def get_codons(strand: str) -> list[str]:
    codons = []
    for i in range(0, len(strand), 3):
        codon = strand[i : i + 3]
        if codon in protein_mapping["STOP"]:
            break
        codons.append(codon)
    return codons

