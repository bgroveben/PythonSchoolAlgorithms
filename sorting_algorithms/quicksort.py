# Quicksort is a divide and conquer algorithm.
# A large array is divided into smaller sub-arrays that are then recursively sorted.
# 1. Pick an element from the array that becomes the pivot.
# 2. Partition the array so that all elements with values less than the pivot come before the pivot,
#    while all elements with values greater than the pivot come after it.
# 3. Recursively apply the above steps to the sub-arrays of elements.
# Pivot selection and partitioning steps can be done in different ways and can greatly affect performance.

def partition(my_list, start, end):
    pivot = my_list[start]
    left = start+1
    right = end
    done = False
    while not done:
        while left <= right and my_list[left] <= pivot:
            left = left+1
        while right >= left and my_list[right] >= pivot:
            right = right-1
        if right < left:
            done = True
        else:
            # swap left and right
            my_list[left], my_list[right] = my_list[right], my_list[left]
    # swap start with my_list[right]
    my_list[start], my_list[right] = my_list[right], my_list[start]
    return right

def quicksort(my_list, start, end):
    if start < end:
        # partition the list
        split = partition(my_list, start, end)
        # recursively sort both halves
        quicksort(my_list, start, split-1)
        quicksort(my_list, split+1, end)
    return my_list

if __name__=="__main__":
    my_list = [7,2,5,1,29,6,4,19,11]
    sorted_list = quicksort(my_list, 0, len(my_list)-1)
    print(sorted_list)
