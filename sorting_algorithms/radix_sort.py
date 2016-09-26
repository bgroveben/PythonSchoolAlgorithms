# https://en.wikipedia.org/wiki/Sorting_algorithm#Radix_sort
# http://www.geekviewpoint.com/python/sorting/radixsort
# Radix sort is an algorithm that sorts numbers by processing individual digits and is similar in concept to bucket sort.
# n numbers consisting of k digits each are sorted in O(n * k) time.
# Radix sort can process digits of each number either starting from most or least significant digit.
# The particular distinction for radix sort is that it creates a bucket for each cipher (digit);
# this means that each bucket in a radix sort must be a list that can expand to admit different keys.
# For decimal values, the number of buckets is 10 (for the 10 different numerals/ciphers).
# Then the keys are continuously sorted by significant digits, either MSD or LSD.

def radix_sort(my_list):
    RADIX = 10
    max_length = False
    tmp, placement = -1, 1

    while not max_length:
        max_length = True
        # declare and initialize buckets -- [[],[],[],[],[],[],[],[],[],[]]
        #                                -- [[] for i in range(RADIX)]
        buckets = [list() for _ in range(RADIX)]
        # split my_list between lists
        for i in my_list:
            tmp = i // placement
            buckets[tmp % RADIX].append(i)
            if max_length and tmp > 0:
                max_length = False
        # empty lists into my_list array
        a = 0
        for b in range(RADIX):
            buck = buckets[b]
            for i in buck:
                my_list [a] = i
                a+=1
        # move to next digit
        placement *= RADIX

this_list = [18,5,100,3,1,19,6,0,7,4,2]
radix_sort(this_list)
print(this_list)

some_list = [8,5,3,1,9,6,0,7,4,2]
radix_sort(some_list)
print(some_list)

test = [13,14,94,33,82,25,59,94,65,23,45,27,73,25,39,10]
radix_sort(test)
print(test)
