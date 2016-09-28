# Cocktail shaker sort is a variant of the bubble sort that sorts in both directions on each pass through a list.
# Cocktail sort will have the best run time if the list is mostly ordered before applying the algorithm.

def cocktail_sort(my_list):
    for k in range(len(my_list)-1, 0, -1):
        swapped = False
        for i in range(k, 0, -1):
            if my_list[i] < my_list[i-1]:
                my_list[i], my_list[i-1] = my_list[i-1], my_list[i]
                swapped = True

        for i in range(k):
            if my_list[i] > my_list[i+1]:
                my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
                swapped = True

        if not swapped:
            return my_list

some_list = [8,5,3,1,9,6,0,7,4,2]
cocktail_sort(some_list)
print(some_list)

test = [13,14,94,33,82,25,59,94,65,23,45,27,73,25,39,10]
cocktail_sort(test)
print(test)
