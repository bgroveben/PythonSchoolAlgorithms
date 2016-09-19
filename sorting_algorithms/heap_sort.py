# I found this implementation at http://www.geekviewpoint.com/python/sorting/heapsort
#                            and https://code.activestate.com/recipes/577086-heap-sort/
# The idea of heapsort is to turn an array into a binary heap structure.
# A binary heap structure allows efficient retrieval and removal of the maximal element.
# The largest/highest element is repeatedly removed from the heap, building the sorted list from back to front.
# Heapsort requires random access, so it can only be used on an array or array-like data structure.

# Heapsort happens in two stages.
# In the first stage, the array is transformed into a heap data structure in the form of a binary tree where:
# 1) Each node is greater than each of its children.
# 2) The tree is perfectly balanced.
# 3) All leaves are in the leftmost position available.
# In the second stage the heap is reduced to a sorted array:
# While the heap is not empty:
# - move the top element into an array
# - fix the heap

def heap_sort(A): # A is an array or list (that will be converted to an array)

    # Convert the array or list to a heap
    def heapify(A):
        start = (len(A) - 2) // 2
        while start >= 0:
            sift_down(A, start, len(A) - 1)
            start -= 1

    # Make sure that we are dealing with a heap structure:
    # - check that an element is greater than its children.
    # - if not, the values of the element and the child are swapped.
    # - The function continues until the element is at a position where it is greater than its children
    def sift_down(A, start, end):
        root = start
        while root * 2 + 1 <= end:
            child = root * 2 + 1
            if child + 1 <= end and A[child] < A[child + 1]:
                child += 1
            if child <= end and A[root] < A[child]:
                A[root], A[child] = A[child], A[root]
                root = child
            else:
                return  ## force exit -- usually a trip back through the while loop in def heapify(A) 

    # Now flatten the heap into a sorted array
    heapify(A)
    end = len(A) - 1
    while end > 0:
        A[end], A[0] = A[0], A[end]
        sift_down(A, 0, end-1)
        end -= 1

if __name__=='__main__':
    test = [13,14,94,33,82,25,59,94,65,23,45,27,73,25,39,10]
    heap_sort(test)
    print(test)
