# http://interactivepython.org/runestone/static/pythonds/SortSearch/TheShellSort.html

# The shell sort improves on the insertion sort by breaking the original list into sublists.
# Each of these sublists is then sorted using insertion sort.
# The unique way that these sublists are chosen is the key to the shell sort.
# Shell sort uses a 'gap', which can be thought of as an increment i.
# Instead of breaking the list into sublists of contiguous items, the sublist is composed of items that are i items apart.
# For example, if there are 9 items in a list, and the gap is 3, then 3 sublists are sorted using insertion sort.

def shell_sort(my_list):
    sublist_count = len(my_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(my_list, start_position, sublist_count)
        print("After increments of size", sublist_count, "The list is", my_list)
        sublist_count = sublist_count // 2

def gap_insertion_sort(my_list, start, gap):
    for i in range(start+gap, len(my_list), gap):
        current_value = my_list[i]
        position = i
        while position >= gap and my_list[position - gap] > current_value:
            my_list[position] = my_list[position - gap]
            position = position - gap
        my_list[position] = current_value

some_list = [54,26,93,17,77,31,44,55,20]
shell_sort(some_list)
print(some_list)

test = [13,14,94,33,82,25,59,94,65,23,45,27,73,25,39,10]
shell_sort(test)
print(test)
