import networkx as nx
from itertools import permutations

def cycle_length(g, cycle):
    # Checking that the number of vertices in the graph equals the number of vertices in the cycle.
    assert len(cycle) == g.number_of_nodes()
    length = 0
    for i in range(len(cycle)-1):
      edge = g[cycle[i]][cycle[i+1]]['weight']

      if edge == -1:
        return -1 
      length += edge
    return length

# def shortest_length(g):
#     # n is the number of vertices.
#     n = g.number_of_nodes()
#     index = 0
#     # Iterate through all permutations of n vertices
#     #for p in permutations(range(n)):
#     for p in permutations(range(n)):
#       if index == 0:
#         min_len = cycle_length(g, p)
#         index += 1
#       else:
#         length = cycle_length(g, p)
#         if length < min_len:
#           min_len = length
#     return min_len

def shortest_length(g):
    n = g.number_of_nodes()
     # The distance to the closest vertex. Initialized with infinity.
    min_len = float("inf")
    for p in permutations(range(n)):
      current_length = cycle_length(g, p)

      if current_length == -1:
        continue
      min_len = min(min_len, current_length)
    return min_len
    
# def shortest_path(g):
#     n = g.number_of_nodes()
#     index = 0
#     for p in permutations(range(n)):
#       if index == 0:
#         min_len = cycle_length(g, p)
#         min_p = p
#         index += 1
#       else:
#         length = cycle_length(g, p)
#         if length < min_len:
#           min_len = cycle_length(g, p)
#           min_p = p
#     return min_p

def shortest_path(g):
    n = g.number_of_nodes()
     # The distance to the closest vertex. Initialized with infinity.
    min_len = float("inf")
    for p in permutations(range(n)):
      current_length = cycle_length(g, p)
      if current_length == -1:
        continue

      if current_length < min_len:
        min_len = current_length
        min_path = p
    return min_path


g = nx.Graph()
# Now we will add 6 edges between 4 vertices
g.add_edge(0, 1, weight = 5)
g.add_edge(0, 2, weight = 7)
g.add_edge(0, 3, weight = 3)
g.add_edge(0, 4, weight = 5)

g.add_edge(1, 2, weight = -1)
g.add_edge(1, 3, weight = -1)
g.add_edge(1, 4, weight = 9)

g.add_edge(2, 3, weight = 2)
g.add_edge(2, 4, weight = -1)

g.add_edge(3, 4, weight = 1)


print(shortest_length(g))
print(shortest_path(g))