# https://en.wikipedia.org/wiki/Depth-first_search
# https://github.com/nryoung/algorithms/blob/master/algorithms/searching/depth_first_search.py

# This is a recursive implementation of the Depth-first search algorithm used to traverse trees and graphs.
# DFS starts at a selected node (root) and explores the branch as far as possible before backtracking.

# Time complexity is O(E + V) where:
# E = Number of edges
# V = Number of vertices (nodes)

# Parameters are:
# graph: A dictionary of nodes and edges
# start: The node to start the recursive search with
# path: A list of edges to search

def dfs(graph, start, path=[]):
    if start not in graph or graph[start] is None or graph[start] == []:
        return None
    path = path + [start]
    for edge in graph[start]:
        if edge not in path:
            path = dfs(graph, edge, path)
    return path

# Now, in order to test this I need to find, or better yet, make a graph to use for testing
# http://networkx.readthedocs.io/en/networkx-1.10/index.html can get me started.
