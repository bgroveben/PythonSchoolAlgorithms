# Bubble sort is an algorithm that repeatedly steps through the list to be sorted,
# compares each pair of adjacent items in the list and then swaps them if they are in the wrong order.
# The average case performance is O(n-squared), so this is not usually a preferred way of sorting stuff.

def bubble_sort(my_list):
    more_swaps = True
    while more_swaps:
        more_swaps = False
        for element in range(len(my_list) - 1):
            if my_list[element] > my_list[element + 1]:
                more_swaps = True
                temp = my_list[element]
                my_list[element] = my_list[element + 1]
                my_list[element + 1] = temp
    return my_list

if __name__=="__main__":
    this_list = [5, 2, 7, 1, 9, 3, 6, 8, 4]
    sorted_list = bubble_sort(this_list)
    print(sorted_list)

# A note about bubble sort and its refinements/relatives/offspring from Donald Knuth -
#
# "But none of these refinements leads to an algorithm better than straight insertion [that is, insertion sort];
#  and we already know that straight insertion isn't suitable for large N. [...] In short, the bubble sort seems
#  to have nothing to recommend it, except a catchy name and the fact that it leads to some interesting theoretical
#  problems."
#
# Knuth, Donald E. (1973). "Sorting by Exchanging". Art of Computer Programming. 3. Sorting and Searching (1st ed.).
# Addison-Wesley. pp. 110–111. ISBN 0-201-03803-X.
