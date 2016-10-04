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
