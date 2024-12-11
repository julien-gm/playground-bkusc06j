def is_anagram(word1: str, word2: str) -> bool:
    return sorted(word1.lower()) == sorted(word2.lower())
