# Binary search function used to find an item in an ordered list.
# Binary search divides the list in half on each iteration.
# If the item is the midpoint, you have found it.
# If the item is higher than the midpoint, the low_end of the list moves to one item above the midpoint.
# If the item is lower than the midpoint, the high_end of the list moves to one less than the midpoint.

def binary_search(my_item, my_list):
    found = False
    low_end = 0
    high_end = len(my_list) - 1
    while low_end <= high_end and not found:
        midpoint = (low_end + high_end) // 2
        if my_list[midpoint] == my_item:
            found = True
        elif my_list[midpoint] < my_item:
            low_end = midpoint + 1
        else:
            high_end = midpoint - 1
    return found

if __name__=="__main__":
    number_list = [1,4,6,8,12,15,18,19,24,27,31,42,43,58]
    item = int(input("What number are you looking for?"))
    is_it_found = binary_search(item, number_list)
    if is_it_found:
        print("Your number is in the list.")
    else:
        print("Your number is not in the list.")
