# Selection sort is an in-place comparison sort that:
# 1) Finds the maximum in a list or array.
# 2) Swaps the maximum value with the value in the last position.
# 3) Repeats steps 1 and 2 for the remainder of the list or array.
# Selection sort can also be written to find the minimum value and swap it with the value in the first position.
# Even though selection sort only swaps elements when necessary, the best time complexity is O(n^2)

# I found this implementation at http://interactivepython.org/runestone/static/pythonds/SortSearch/TheSelectionSort.html

def selection_sort(my_list):
   for index in range(len(my_list)-1,0,-1):
       position_of_max_value = 0
       for pointer_location in range(1, index+1):
           if my_list[pointer_location] > my_list[position_of_max_value]:
               position_of_max_value = pointer_location
       my_list[index], my_list[position_of_max_value] = my_list[position_of_max_value], my_list[index]

some_list = [54,26,93,17,77,31,44,55,20]
selection_sort(some_list)
print(my_list)

test = [13,14,94,33,82,25,59,94,65,23,45,27,73,25,39,10]
selection_sort(test)
print(test)
