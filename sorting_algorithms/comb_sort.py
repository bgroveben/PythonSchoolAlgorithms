# https://en.wikibooks.org/wiki/Algorithm_Implementation/Sorting/Comb_sort

# Comb sort is an improvement to the bubble sort algorithm.
# The basic idea is to eliminate the small values near the end of the list that slow down the sorting.
# Like the shell sort, the comb sort increases the gap used in comparisons and exchanges (swaps).

def update_gap(gap):
    # The gap starts with a large value and shrinks by a factor of 1.3 on each iteration until it reaches 1
    gap = (gap * 10) / 13
    if gap == 9 or gap == 10:
        gap = 11
    return int(max(1, gap))

def comb_sort(my_list):
    gap = len(my_list)
    swapped = True
    if gap < 2:
        return
    while gap > 1 or swapped:
        gap = update_gap(gap)
        swapped = False
        for i in range(0, len(my_list) - gap, gap):
            if my_list[i] > my_list[i + gap]:
                my_list[i], my_list[i + gap] = my_list[i + gap], my_list[i]
                swapped = True

some_list = [54,26,93,17,77,31,44,55,20]
comb_sort(some_list)
print(some_list)

test = [13,14,94,33,82,25,59,94,65,23,45,27,73,25,39,10]
comb_sort(test)
print(test)
