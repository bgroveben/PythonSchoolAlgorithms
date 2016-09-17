# Insertion sort uses the idea of a marker as a dividing line between the sorted and unsorted my_list in a list.
# The marker starts at the left side of the list and moves to the right as the my_list go from unsorted to sorted.
# https://en.wikipedia.org/wiki/Insertion_sort

def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        j = i
        while j > 0 and (my_list[j] < my_list[j-1]):
            my_list[j], my_list[j-1] = my_list[j-1], my_list[j]  # Swap list elements
            j -= 1
    return my_list

if __name__=="__main__":
    this_list = [5, 2, 7, 1, 9, 3, 6, 8, 4]
    sorted_list = insertion_sort(this_list)
    print(sorted_list)
