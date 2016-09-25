# https://en.wikibooks.org/wiki/Algorithm_Implementation/Sorting/Bucket_sort
# https://en.wikipedia.org/wiki/Bucket_sort

# Bucket sort, aka bin sort, works by distributing the elements of an array into a number of buckets.
# Each bucket is then sorted individually, either by using a different sorting algorithm,
# or by recursively applying the bucket sorting algorithm.
# Bucket sort works as follows:
# 1) Initialize an array of empty buckets.
# 2) Scatter: Go over the original array, putting each object in its respective bucket.
# 3) Sort each non-empty bucket.
# 4) Gather: Visit the buckets in order and put all of the elements back into the original array.
# Note that for bucket sort to be O(n) on average, the number of buckets n must be equal to the length of
# the array being sorted, AND the input array must be uniformly distributed across the range of possible
# bucket values.
# In the following program, insertion_sort is used to sort each bucket.
# http://www.geekviewpoint.com/python/sorting/bucketsort

from insertion_sort import insertion_sort

def bucket_sort(my_array):
    # get hash codes
    code = hashing(my_array)
    buckets = [list() for _ in range(code[1])] # the underscore is a throwaway variable
    # distribute data into buckets: 0(n)
    for i in my_array:
        x = re_hashing(i, code)
        buck = buckets[x]
        buck.append(i)

    for bucket in buckets:
        insertion_sort(bucket)

    ndx = 0
    # merge the buckets: 0(n)
    for b in range(len(buckets)):
        for v in buckets[b]:
            my_array[ndx] = v
            ndx+=1

import math

def hashing(my_array):
    m = my_array[0]
    for i in range(1, len(my_array)):
        if (m < my_array[i]):
            m = my_array[i]
    result = [m, int(math.sqrt(len(my_array)))]
    return result

def re_hashing(i, code):
    return int( i // code[0] * (code[1] - 1))


some_list = [8,5,3,1,9,6,0,7,4,2]
bucket_sort(some_list)
print(some_list)

test = [13,14,94,33,82,25,59,94,65,23,45,27,73,25,39,10]
bucket_sort(test)
print(test)
