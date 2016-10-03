# https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_string_search_algorithm
# https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore%E2%80%93Horspool_algorithm
# http://code.activestate.com/recipes/117223-boyer-moore-horspool-string-searching/

# Boyer-Moore_Horspool is an algorithm for finding substrings in strings.
# While Boyer-Moore applies two shift rules -- the bad character rule and the good suffix rule --
# BMH only uses a bad-suffix rule for matching.
# This makes BMH simpler to implement and, in some cases, faster than BM.

# If the word being searched for is present in the text, the array position of the first letter will be returned.
# If the word being searched for is not present, -1 will be returned.
# Print statements at the end will give more details.

def bmh_search(pattern, text):
    needle = len(pattern)
    haystack = len(text)

    if needle > haystack:
        return -1

    skip = []
    for k in range(256): # for an alphabet of 256 symbols, i.e., bytes
        skip.append(needle)
    for k in range(needle-1):
        # https://docs.python.org/3/library/functions.html#ord
        skip[ord(pattern[k])] = needle - k-1
    skip = tuple(skip)

    k = needle-1
    while k < haystack:
        j = needle-1
        i = k
        while j >= 0 and text[i] == pattern[j]:
            j -=1
            i -=1
        if j == -1:
            return i+1
        k += skip[ord(text[k])]
    return -1

if __name__ =='__main__':
    text = "this is the string to search in"
    pattern = "the"
    s = bmh_search(pattern, text)
    print('Text:', text)
    print('Pattern:', pattern)
    if s > -1:
        print('Pattern \"' + pattern + '\" found at position', s)
    else:
        print('Sorry, no match')
