def is_anagram(word1: str, word2: str) -> bool:
    return word_to_dict(word1) == word_to_dict(word2)


def word_to_dict(word: str) -> dict:
    letters = {}
    for letter in word:
        letters[letter] = 1 if letter not in letters else letters[letter] + 1
    return letters
