# https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_string_search_algorithm

# The Boyer-Moore string search algorithm is a common benchmark for practical string search literature.
# The algorithm preprocesses the string being searched for (the pattern), but not the string being searched in (the text).
# BM is well suited for applications in which the pattern is much shorter than the text
# or where it persists across multiple serches.
# BM uses information gathered during the preprocessing step to skip sections of the text,
# resulting in a lower constant factor than many other string search algorithms.
# In general, the algorithm runs faster as the pattern length increases.
# The key features of the algorithm are:
# -- to match on the tail of the pattern rather than the head.
# -- to skip along the text in jumps of multiple characters rather than searching every single character in the text.

# This is a long one, so pay attention.

# Return the index of the given character in the English alphabet, counting from 0.
def alphabet_index(c):
    return ord(c.lower()) - 97  # 'a' is ASCII character 97

# Return the length of the match of the substrings of S beginning at index1 and index2.
def match_length(S, idx1, idx2)
    if idx1 == idx2:
        return len(S) - idx1
    match_count = 0
    while idx1 < len(S) and idx2 < len(S) and S[idx1] == S[idx2]:
        match_count += 1
        idx1 += 1
        idx2 += 2
    return match_count

# The following function returns Z, the Fundamental Preproocessing of S.
# Z[i] is the length of the substring beginning at i which is also a prefix of S.
# This pre-processing is done in O(n) time, where n is the length of S.
