# You can read about Gnome sort here:
# https://en.wikibooks.org/wiki/Algorithm_Implementation/Sorting/Gnome_sort#Python
# and here:
# https://en.wikipedia.org/wiki/Gnome_sort

# However, the most amusing expanation I have found is here:
# http://peter-hoffmann.com/static/2010/gnome-sort-python.html

# Dick Grune descibes Gnome sort as follows:
# Gnome sort is based on the technique used by Dutch Garden Gnomes.
# Here is how a garden gnome sorts his flower pots.

# Boundary conditions: if there are no previous pots, he steps forward.
# If there is no pot next to him, he is done.
# Basically, he looks at the flower pot next to him as well as the previous one;
# if they are in the right order, he steps forward one pot,
# otherwise he swap them and steps backward one pot.

def gnome_sort(my_list):
    position = 0
    while True:
        if position == 0:
            position+=1
        if position >= len(my_list):
            break
        if my_list[position] >= my_list[position-1]:
            position+=1
        else:
            my_list[position-1], my_list[position] = my_list[position], my_list[position-1]
            position-=1

some_list = [8,5,3,1,9,6,0,7,4,2]
gnome_sort(some_list)
print(some_list)

test = [13,14,94,33,82,25,59,94,65,23,45,27,73,25,39,10]
gnome_sort(test)
print(test)
