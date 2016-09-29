# https://en.wikibooks.org/wiki/Algorithm_Implementation/Sorting/Patience_sort#Python
# https://en.wikipedia.org/wiki/Patience_sorting
# Like the card game, the game begins with a shuffled deck with the cards being dealt into a sequence of piles.
# 1) The first card dealt forms a new pile consisting of a single card.
# 2) Each subsequent card is placed on the leftmost pile whose top card has a value greater than or equal to
#    the new card's value, or to the right of all of the existing piles, thus forming a new pile.
# 3) When there are no more cards remaining to deal, the game ends.
# This game is turned into a two-stage sorting algorithm, as follows:
# 1) Given an array of n elements from some totally ordered domain, consider this array as a collection of cards
#    and simulate the patience sorting game.
# 2) When the game is over, recover the sorted sequence by repeatedly picking off the minimum visible card;
#    in other words, perform a k-way merge of the piles p, each of which is internally sorted.
# Let's do this.

# https://docs.python.org/3.5/library/bisect.html
# https://docs.python.org/3.5/library/heapq.html
import bisect, heapq

def patience_sort(my_list):
    piles = []
    for x in my_list:
        new_pile = [x]
        i = bisect.bisect_left(piles, new_pile)
        if i != len(piles):
            piles[i].insert(0, x)
        else:
            piles.append(new_pile)
    print("The longest increasing subsequence has a length =", len(piles))

    # a priority queue (https://en.wikipedia.org/wiki/Priority_queue) allows us to retrieve the least pile efficiently
    for i in range(len(my_list)):
        small_pile = piles[0]
        my_list[i] = small_pile.pop(0)
        if small_pile:
            heapq.heapreplace(piles, small_pile)
        else:
            heapq.heappop(piles)
    assert not piles

this_list = [8,5,3,1,9,6,0,7,4,2]
patience_sort(this_list)
print(this_list)

test = [13,14,94,33,82,25,59,94,65,23,45,27,73,25,39,10]
patience_sort(test)
print(test)

some_list = [4, 65, 2, 4, -31, 0, 99, 1, 83, 782, 1]
patience_sort(some_list)
print(some_list)
