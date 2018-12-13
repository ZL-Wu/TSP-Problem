
# Full Permutation of an array
# type nums: List[int]
# type start: int
def permutations(start, nums):
      res = []
      sub = [start]
      dfs(res,nums,sub)
      return res


# Assistance dfs function for permutations(nums)
def dfs(res, Nums, subList):
    if len(subList) == len(Nums):
        #print res,subList
        res.append(subList[:])
    for m in Nums:
        if m in subList:
            continue
        subList.append(m)
        dfs(res,Nums,subList)
        subList.remove(m)


# Return the total weight of a path
# type graph: List[List[int]]
# type path: List[int]
# return type: int
def path_length(graph, path):
    # Checking that the number of vertices in the graph equals the number of vertices in the cycle.
    assert len(path) == len(graph)
    length = 0
    # Get the total length of the path
    for i in range(len(path)-1):
      a = int(path[i])
      b = int(path[i+1])
      edge = int(graph[a][b])

    # If one of edge is -1, the path doesn't exist. Marked as -1
      if edge == -1:
        return -1 

      length += edge
    return length


# Return the shortest path length
# type graph: List[List[int]]
# return type: int
def shortest_length(start, graph):
    n = len(graph)
    # The distance to the closest vertex. Initialized with infinity.
    min_len = float("inf")
    # Travels all possible path through permutations() 
    for p in permutations(start, range(n)):
      current_length = path_length(graph, p)

      if current_length == -1:
        continue
      min_len = min(min_len, current_length)
    return min_len


# Return the shortest path
# type graph: List[List[int]]
# return type: List[int]    
def shortest_path(start, graph):
    n = len(graph)
     # The distance to the closest vertex. Initialized with infinity.
    min_len = float("inf")
    min_path = []
    for p in permutations(start, range(n)):
      current_length = path_length(graph, p)
      if current_length == -1:
        continue

      if current_length < min_len:
        min_len = current_length
        min_path = p
    return min_path



#Implement
graph =  [[-1, 5,  7,  3, 5],
          [5, -1, -1, -1, 9],
          [7, -1, -1, 2, -1],
          [3, -1, 2, -1,  1],
          [5, 9, -1,  1, -1]]

# nums = [0, 1, 2, 3]
# print(permutations(1, nums))
# print(permutations(4, [0, 1, 2, 3, 4]))

# start = int(input("Please input the start point: "))
start = 4
print("The shortest path length of the graph is '%d'" %(shortest_length(start, graph)))
print("The shortest path of the graph is %s" %(shortest_path(start, graph)))

