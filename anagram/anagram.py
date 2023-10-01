from collections import Counter


def find_anagrams(word: str, candidates: list[str]) -> list[str]:
    anagrams: list[str] = []
    anagram_counter = Counter(word.lower())
    for candidate in candidates:
        candidate_counter = Counter(candidate.lower())
        print(candidate_counter)
        if anagram_counter == candidate_counter and candidate.lower() != word.lower():
            anagrams.append(candidate)
    return anagrams
