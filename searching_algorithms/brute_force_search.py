# http://www.stoimen.com/blog/2012/03/27/computer-algorithms-brute-force-string-matching/
# https://programmingpraxis.com/2009/08/21/string-search-brute-force/

# (where m = len(text) and n = len(substring)
# The brute force search algorithm checks all positions in a block of text between 0 and n-m and determines
# whether an occurrence of the pattern begins there or not.
# After each attempt, the algorithm shifts the pattern by one position to the right.
# The brute force algorithm requires no preprocessing phase.
# The brute force algorithm does require a constant extra space in addition to the pattern and the text.
# During the search phase the text character comparisons can be done in any order.
# Time complexity is O(mn) and the expected number of character comparisons is 2n.

def brute_force(text, substring, start_from = 0, found_location = 0):

    if len(substring) == 0:
        return found_location

    if len(text) == 0:
        return -1

    for i in iter(text):  # https://docs.python.org/3/library/functions.html#iter
        start_from += 1
        for j in iter(substring):
            if i == j:
                found_location += start_from - 1
                # beacuse recursion is divine
                return brute_force(text[start_from:], substring[1:], 0, found_location)
            else:
                break
    return -1  # if substring is not in text


if __name__=="__main__":
    block = "This is a simple example"
    print("This is an example search on the string \"", block, "\".")
    print("nomatch :", brute_force(block, "nomatch"))
    print("ple :", brute_force(block, "ple "))
    print("example :", brute_force(block, "example"))
    print("simple :", brute_force(block, "simple"))
    print(" imple :", brute_force(block, " imple ")) # this returns 10, even though there is a space in front
