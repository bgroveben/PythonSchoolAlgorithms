# https://en.wikipedia.org/wiki/Breadth-first_search
# Breadth-first search is an algorithm for traversing or searching tree or graph data structures.
# It starts at the tree root (aka the search key, usually an arbitrary node on the graph) and explores
# the neighbor nodes first, before moving to the next level of nodes.
# https://github.com/nryoung/algorithms/blob/master/algorithms/searching/breadth_first_search.py
# Time complexity is calculated as O(E + V) where
# E = Number of edges
# V = Number of vertices (nodes)

def bfs(graph, start):
    if start not in graph or graph[start] is None or graph[start] == []:
        return None
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited

# Now, in order to test this I need to find, or better yet, make a graph to use for testing
# http://networkx.readthedocs.io/en/networkx-1.10/index.html can get me started. 
