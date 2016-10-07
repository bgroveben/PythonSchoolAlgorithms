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

# The following function returns Z, the Fundamental Preprocessing of S.
# Z[i] is the length of the substring beginning at i which is also a prefix of S.
# This pre-processing is done in O(n) time, where n is the length of S.
def fundamental_preprocess(S):
    if len(S) == 0:  # handles empty strings
        return []
    if len(S) == 1:  # for single character strings
        return [1]
    z = [0 for x in S]
    z[0] = len(S)
    z[1] = match_length(S, 0, 1)
    for i in range(2, 1+z[1]):
        z[i] = z[1]-i+1
    # define lower and upper limits of z-box
    l = 0
    r = 0
    for i in range(2+z[1], len(S)):
        if i <= r:  # i falls within existing z-box
            k = i-1
            b = z[k]
            a = r-i+1
            if b < a:  # b ends within existing z-box
                z[i] = b
            else:  # b ends at or after the end of the z-box, so we need to do an explicit match to the right of the z-box
                z[i] = a + match_length(S, a, r+1)
                l = i
                r = i+z[i]-1
        else:  # i does not reside within the existing z-box
            z[i] = match_length(S, 0, i)
            if z[i] > 0:
                l = i
                r = i+z[i]-1
    return z

# Generates R for S, which is an array indexed by the position of some character c in the English alphabet.
# At that index in R is an array of length |S|+1, specifying for each index i in S (plus the index after S)
# the next location of character c encountered when traversing S from right to left starting at i.
# This is used for a constant-time lookup for the bad character rule in the Boyer-Moore string search algorithm,
# although it has a much larger size than non-constant-time solutions.
def bad_character_table(S):
    pass
