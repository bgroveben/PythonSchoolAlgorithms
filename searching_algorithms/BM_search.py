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
def match_length(S, idx1, idx2):
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

# The next function generates R for S -- an array indexed by the position of some character c in the English alphabet.
# At that index in R is an array of length |S|+1, specifying for each index i in S (plus the index after S)
# the next location of character c encountered when traversing S from right to left starting at i.
# This is used for a constant-time lookup for the bad character rule in the Boyer-Moore string search algorithm,
# although it has a much larger size than non-constant-time solutions.
def bad_character_table(S):
    if len(S) == 0:
        return [[] for a in range(26)]

    R = [[-1] for a in range(26)]
    alpha = [-1 for a in range(26)]
    for i, c in enumerate(S):
        alpha[alphabet_index(c)] = i
        for j, a in enumerate(alpha):
            R[j].append(a)
    return R

# This next function generates L for S -- an array used in the implementation of the strong suffix rule.
# L[i] = k, the largest position in S such that S[i:] (the suffix of S beginning at i) matches a suffix of
# S[:k] (a substring in S ending at k).
# Used in Boyer-Moore, L gives an amount to shift P relative to T such that no instances of P in T are skipped
# and a suffix of P[:L[i]] matches the substring of T matched by a suffix of P in the previous match attempt.
# Specifically, if the mismatch took place at position i-1 in P, the shift magnitude is given by the equation
# len(P) - L[i].
# In the case that L[i] = -1, the full shift table is used.
# Since only proper suffixes matter, L[0] = -1.
def good_suffix_table(S):
    L = [-1 for c in S]
    N = fundamental_preprocess(S[::-1])  # S[::-1] reverses S
    N.reverse()
    for j in range(0, len(S)-1):
        i = len(S) - N[j]
        if i != len(S):
            L[i] = j
    return L

# This next function generates F for S, an array used in a special case of the good suffix rule in the BM algorithm.
# F[i] is the length of th elongest suffix of S[i:] that is also a prefix of S.
# In the cases where it is used, the shift magnitude of the pattern P relative to the text T is
# len(P) - F[i] for a mismatch occurring at i-1.
def full_shift_table(S):
    F = [0 for c in S]
    Z = fundamental_preprocess(S)
    longest = 0
    for i, zv in enumerate(reversed(Z)):
        longest = max(zv, longest) if zv == i+1 else longest
        F[-i-1] = longest
    return F

# Now, on to the main course -- the implementation of the Boyer-Moore string search algorithm.
# The following function finds all occurrences of P in T, and incorporates numerous ways of preprocessing
# the pattern to determine the optimal amount to shift the string and skip comparisons.
# In practice it runs in O(n) (and sometimes even sublinear) time, where n is the length of T.
# This implementation performs a case-insensitive search on ASCII alphabetic characters, not including spaces.
def string_search(P, T):
    if len(P) == 0 or len(T) == 0 or len(T) < len(P):
        return []

    matches = []

    # Preprocessing
    R = bad_character_table(P)
    L = good_suffix_table(P)
    F = full_shift_table(P)

    k = len(P) - 1      # Represents alignment of end of P relative to T
    previous_k = -1     # Represents alignment in previous phase (Galil's rule)
    while k < len(T):
        i = len(P) - 1  # Character to compare in P
        h = k           # Character to compare in T
        while i >= 0 and h > previous_k and P[i] == T[h]:   # Matches starting from end of P
            i -= 1
            h -= 1
        if i == -1 or h == previous_k:  # Match has been found (Galil's rule)
            matches.append(k - len(P) + 1)
            k += len(P)-F[1] if len(P) > 1 else 1
        else:   # No match, shift by max of bad character and good suffix rules
            char_shift = i - R[alphabet_index(T[h])][i]
            if i+1 == len(P):   # Mismatch happened on first attempt
                suffix_shift = 1
            elif L[i+1] == -1:   # Matched suffix does not appear anywhere in P
                suffix_shift = len(P) - F[i+1]
            else:               # Matched suffix appears in P
                suffix_shift = len(P) - L[i+1]
            shift = max(char_shift, suffix_shift)
            previous_k = k if shift >= i+1 else previous_k  # Galil's rule
            k += shift
    return matches


#if __name__ =='__main__':
#    text = "this is the string to search in"
#    pattern = "the"
#    test = string_search(pattern, text)
#    print('Text:', text)
#    print('Pattern:', pattern)
#    print(test)

if __name__ == "__main__":
    block = "This is a simple example"
    print("This is an example search on the string \"", block, "\".")
    print("ple  :", string_search(block, "ple "))
    print("example :", string_search(block, "example"))
    print("simple :", string_search(block, "simple"))
    print(" imple :", string_search(block, " imple"))
    print("is :", string_search(block, "is"))
