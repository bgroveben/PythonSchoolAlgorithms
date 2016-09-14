# Linear Search function used to find an item in a list.

def linear_search(my_item, my_list):
    found = False
    position = 0
    while position < len(my_list) and not found:
        if my_list[position] == my_item:
            found = True
        position = position + 1
    return found

if __name__ == "__main__":
    shopping_list = ["apples", "bananas", "cherries", "duraznos"]
    item = input("What item do you want to find?")
    is_it_found = linear_search(item, shopping_list)
    if is_it_found:
        print("Your item is on the list.")
    else:
        print("Your item is not on the list")
