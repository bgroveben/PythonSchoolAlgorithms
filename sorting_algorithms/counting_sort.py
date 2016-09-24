# http://www.geekviewpoint.com/python/sorting/countingsort
# Author: Isai Damier
# Title: Countingsort
# Project: GeekViewpoint
# Package: algorithms
#
# Statement:
# Given an unordered list of repeated integers, rearrange the integers in their natural order.
#
# Sample Input:  [4,3,2,1,4,3,2,4,3,4]
# Sample Output: [1,2,2,3,3,3,4,4,4,4]
#
# Sample Input:  [1, 4, 7, 2, 1, 3, 2, 1, 4, 2, 3, 2, 1]
# Sample Output: [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 7]

# Time Complexity of Solution:
# Best Case O(n+k); Average Case O(n+k); Worst Case O(n+k),
# where n is the size of the input array and k is the range of values from 0 to k.
#
# Approach:
# Counting sort, like radix sort and bucket sort, is an integer based algorithm.
# The values of the input array are assumed to be integers.
# Hence counting sort is among the fastest sorting algorithms available, in theory at least.
# The distinction for counting sort is that it creates a bucket for each value with a counter
# for each bucket, much like a histogram.
# Each time a value is encountered in the input collection, the corresponding counter is incremented.
# Because counting sort creates a bucket for each value, the maximum value in the input array
# must be known beforehand, which can be a formidable restriction.
#
# Counting sort is often confused with bucket sort.
# Bucket sort uses a hash function to distribute values.
# Counting sort creates a counter for each value.
#
# Implementation notes:
#
# 1) Since the values range from 0 to k, create k+1 buckets.
# 2) To fill the buckets, iterate through the input list -- each time a value
#    appears, increment the counter in its corresponding bucket.
# 3) Fill the input list with the compressed data in the buckets.
#    Each bucket's key represents a value in the array.
#    For each bucket, from the smallest key to the largest, add the index of the bucket to the
#    input array and decrease the counter in that bucket by one until the counter reaches zero.

def counting_sort(my_list, k):
    counter = [0] * (k+1)
    for i in my_list:
        counter[i] += 1
    index = 0
    for i in range(len(counter)):
        while 0 < counter[i]:
            my_list[index] = i
            index += 1
            counter[i] -= 1

some_list = [4,3,2,1,4,3,2,4,3,4]
counting_sort(some_list,4)
print(some_list)

test_list = [1, 4, 7, 2, 1, 3, 2, 1, 4, 2, 3, 2, 1]
counting_sort(test_list,7)
print(test_list)
