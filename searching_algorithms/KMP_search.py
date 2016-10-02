# https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm
# https://github.com/nryoung/algorithms/blob/master/algorithms/searching/kmp_search.py

# Implementation of KMP search on a string using a prefix function to reduce search time.
# Searches for occurrences of a 'word' within a main 'string'.
# When a mismatch occurs, the word itself has enough information to determine where the next match could begin.
# This observation allows the re-examination of previously matched characters to be bypassed.

# The kmp_search(string, word) function should return the position of the first letter in 'word' if it is
# contained in 'string' (example output -> [4]); if 'word' is not in 'string', an empty list [] is returned.

# string: The string to be searched
# word: The sub-string to be searched for.

# q acts like the 'matcher' -- while iterating through 'string', if a letter matches the first letter of 'word',
# q goes up to 1. If the next letter is also the next letter in 'word' q goes up to 2, and so on until 'word' is matched.
# If the next letter is not in 'word', there is no match, q goes back to zero, and the index continues
# to iterate through 'string'.

# offsets starts as an empty list and (eventually) contains the array position of the return value.

# prefix creates a list whose length equals the number of letters in 'word' that must be matched.
def kmp_search(string, word):
    word_length = len(word)
    string_length = len(string)
    offsets = []

    if word_length > string_length:
        return offsets

    prefix = [0] * len(word)
    q = 0
    # https://docs.python.org/3.5/library/functions.html#enumerate
    for index, letter in enumerate(string):
        while q > 0 and word[q] != letter:
            q = prefix[q - 1]
        if word[q] == letter:
            q += 1
        if q == word_length:
            offsets.append(index - word_length + 1)
            q = prefix[q - 1]
    return offsets

# BTW, capitalization is not accounted for -- uppercase and lowercase letters must match exactly.
sentence = "The quick brown fox jumped over the lazy dog."
found = kmp_search(sentence, "quick")
print(found)
not_found = kmp_search(sentence, "none")
print(not_found)
