# https://en.wikipedia.org/wiki/Merge_sort
# Merge sort courtesy of John von Neumann circa 1945.
# Merge sort is a divide and conquer algorithm that works by:
# 1) Dividing an unsorted list into n sublists, each containing 1 element.
# -- Why 1 element? A list of one element is considered sorted.
# 2) Repeatedly merging the sublists to produce new sorted sublists until only one sublist remains.
# -- This will be the sorted list.
# Implementations of merge sort can be top-down or bottom-up, each with or without using lists.

# http://interactivepython.org/runestone/static/pythonds/SortSearch/TheMergeSort.html
# Merge sort is a recursive algorithm that continually splits a list in half.
# If the list is empty or has one item, it is sorted by definition (the base case).
# If the list has more than one item, we split the list and recursively invoke a merge sort on both halves.
# Once the two halves are sorted, the fundamental operation, called a merge, is performed.
# Merging is the process of taking two smaller sorted lists and combining them into a single, sorted, new list.

def merge_sort(my_list):
    print("Splitting ",my_list)
    if len(my_list) > 1:
        midpoint = len(my_list)//2
        left_half = my_list[:midpoint]
        right_half = my_list[midpoint:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = 0
        j = 0
        k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                my_list[k] = left_half[i]
                i += 1
            else:
                my_list[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            my_list[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            my_list[k] = right_half[j]
            j += 1
            k += 1
    print("Merging ",my_list)

some_list = [54,26,93,17,77,31,44,55,20]
merge_sort(some_list)
print(some_list)

print()

test = [13,14,94,33,82,25,59,94,65,23,45,27,73,25,39,10]
merge_sort(test)
print(test)
