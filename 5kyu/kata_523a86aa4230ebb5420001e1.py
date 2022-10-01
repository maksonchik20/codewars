#Where my anagrams at?

def anagrams(word, words):
    return [el for el in words if set(el) == set(word) and len(el) == len(word)]