# https://en.wikipedia.org/wiki/Rabin%E2%80%93Karp_algorithm
# The Rabin-Karp algorithm is a string search algorithm that uses hashing to find any one set of pattern strings in a text.
# A practical application of Rabin-Karp is in detecting plagiarism:
# Given source material, RK can rapidly search through a paper for instances of sentences from the source material,
# while ignoring details such as case and punctuation.

# Speaking of plagiarism, I found this python implementation at:
# https://github.com/nryoung/algorithms/blob/master/algorithms/searching/rabinkarp_search.py

# This implementation will search for a substring in a given string by comparing hash values of the strings.
# If a match is found the program will return the array position of the first letter of the match.
# If there is no match, the result will be an empty array.


from hashlib import md5

def RKSearch(text, sub):
    """
    text is the string (or block of text) to be searched
    sub is the substring to be searched for
    """
    haystack = len(text)
    needle = len(sub)
    hsub_digest = md5(sub.encode('utf-8')).digest()
    offsets = []
    if needle > haystack:
        return offsets

    for i in range(haystack - needle + 1):
        if md5(text[i:i + needle].encode('utf-8')).digest() == hsub_digest:
            if text[i:i + needle] == sub:
                offsets.append(i)

    return offsets


if __name__=="__main__":
    block = "This is a simple example"
    print("This is an example search on the string \"", block, "\".")
    print("ple :", RKSearch(block, "ple "))
    print("example :", RKSearch(block, "example"))
    print("simple :", RKSearch(block, "simple"))
    print(" imple :", RKSearch(block, " imple "))
