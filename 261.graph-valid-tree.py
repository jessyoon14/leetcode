"""
Iterative DFS (using adjacency map and stack)
time: O(N + E) -> every edge & vertex crossed once
space: O(N + E)
"""
# class Solution:
#     def validTree(self, n: int, edges: List[List[int]]) -> bool:
#         if len(edges) != n - 1: # if meets this condition, now we only have to check if fully connected!
#             return False

#         adj_list = [[] for _ in range(n)]
#         for a, b in edges:
#             adj_list[a].append(b)
#             adj_list[b].append(a)

#         parent = {0: -1}
#         stack = [0]

#         while stack:
#             node = stack.pop()
#             for neighbor in adj_list[node]:
#                 if neighbor == parent[node]:
#                     continue
#                 if neighbor in parent:
#                     return False # cycle

#                 parent[neighbor] = node
#                 stack.append(neighbor)

#         return len(parent) == n

"""
Improved iterative DFS (use the fact that there must be exactly n-1 edges)
time: O(n) (each node visited once)
space: O(n) (adjacency list) -> # edges are now bounded by # vertices
"""

# class Solution:
#     def validTree(self, n: int, edges: List[List[int]]) -> bool:
#         # create adjacency list
#         adj_list = [[] for _ in range(n)]
#         for a, b in edges:
#             adj_list[a].append(b)
#             adj_list[b].append(a)

#         # initialize seen set
#         seen = set()
#         # make stack
#         stack = [0]

#         # iterate through stack
#         while stack:
#             node = stack.pop()
#             neighbors = adj_list[node]

#             for neighbor in neighbors:
#                 if neighbor in seen:
#                     continue
#                 seen.add(neighbor)
#                 stack.append(neighbor)

#         return len(seen) == n


"""
Improved recursive DFS (use the fact that there must be exactly n-1 edges)
time: O(n) (each node visited once)
space: O(n) (adjacency list)
"""
# class Solution:
#     def validTree(self, n: int, edges: List[List[int]]) -> bool:
#         if len(edges) != n - 1:
#             return False

#         # create adj list
#         adj_list = [[] for _ in range(n)]
#         for a, b in edges:
#             adj_list[a].append(b)
#             adj_list[b].append(a)

#         # seen set
#         seen = {}

#         def dfs(node):
#             if node in seen:
#                 return
#             seen.add(node)
#             neighbors = adj_list[node]
#             for neighbor in neighbors:
#                 dfs(neighbor)

#         dfs(0)
#         return len(seen) == n

"""
Improved iterative BFS (use the fact that there must be exactly n-1 edges)
time: O(n) (each node visited once, and E is upper bounded by n)
space: O(n) (adjacency list)
"""
# class Solution:
#     def validTree(self, n: int, edges: List[List[int]]) -> bool:
#         if len(edges) != n - 1:
#             return False

#         # create adj list
#         adj_list = [[] for _ in range(n)]
#         for a, b in edges:
#             adj_list[a].append(b)
#             adj_list[b].append(a)

#         # seen
#         seen = {}
#         # queue
#         queue = deque([0])
#         # iterate
#         while queue:
#             node = queue.popleft()
#             seen.add(node)
#             for neighbor in adj_list[node]:
#                 if neighbor not in seen:
#                     queue.append(neighbor)

#         return len(seen) == n

"""
Non-optimized union search -> stop at very first cycle

"""
# class UnionFind:
#     def __init__(self, n):
#         self.parent = [node for node in range(n)]

#     def find(self, x):
#         while x != self.parent[x]:
#             x = self.parent[x]
#         return x

#     def union(self, x, y):
#         rootX = self.find(x)
#         rootY = self.find(y)
#         if rootX == rootY: # cycle
#             return False

#         self.parent[rootY] = rootX
#         return True

# class Solution:
#     def validTree(self, n: int, edges: List[List[int]]) -> bool:
#         if len(edges) != n - 1:
#             return False

#         unionFind = UnionFind(m)
#         for a, b in edges:
#             if not unionFind.union(a, b):
#                 return False

#         return True

"""
Optimized union find
time: O(n * a(n)) -> a(n) means near constant. worst case is O(n*2), when find is called for all of the chain
space: O(n)
"""


class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x):
        if x == self.root[x]:
            return x

        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:  # cycle
            return False
        elif self.rank[rootX] > self.rank[rootY]:
            self.root[rootY] = rootX
        elif self.rank[rootX] < self.rank[rootY]:
            self.root[rootX] = rootY
        else:
            self.root[rootY] = rootX
            self.rank[rootX] += 1

        return True


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        uf = UnionFind(n)

        for a, b in edges:
            if not uf.union(a, b):
                return False

        return True


"""
Recursive DFS (using adjacency map and set)
"""
# class Solution:
#     def validTree(self, n: int, edges: List[List[int]]) -> bool:
#         if len(edges) != n - 1:
#             return False

#         adj_list = [[] for _ in range(n)]
#         for a, b in edges:
#             adj_list[a].append(b)
#             adj_list[b].append(a)

#         seen = set()

#         def dfs(node, parent):
#             if node in seen:
#                 return False
#             seen.add(node)
#             for neighbor in adj_list[node]:
#                 if neighbor == parent:
#                     continue
#                 if neighbor in seen:
#                     return False
#                 result = dfs(neighbor, node)
#                 if not result:
#                     return False
#             return True

#         return dfs(0, -1) and len(seen) == n

"""
Iterative BFS
time: O(N + E) -> every edge & vertex crossed once
space: O(N + E)
"""


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adj_list = [[] for i in range(n)]
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)

        parent = {0: -1}
        queue = deque([0])

        while queue:
            node = queue.popleft()
            for neighbor in adj_list[node]:
                if neighbor == parent[node]:
                    continue
                elif neighbor in parent:
                    return False
                parent[neighbor] = node
                queue.append(neighbor)
        return len(parent) == n


"""
DFS
During DFS, should hit every node ONCE
time: O(n ^ 2)
space: O(n)
"""
# class Solution:
#     def validTree(self, n: int, edges: List[List[int]]) -> bool:
#         def dfs(i): # return True if there is valid tree with root i
#             if i in visited:
#                 return False

#             visited.add(i)

#             for j in range(n):
#                 if ((i,j) in edges_set or (j, i) in edges_set):
#                     if (i,j) in edges_set:
#                         edges_set.remove((i, j))
#                     else:
#                         edges_set.remove((j, i))
#                     if not dfs(j):
#                         return False
#             return True

#         # preprocess edges into set
#         edges_set = set()
#         for v1, v2 in edges:
#             edges_set.add((v1, v2))

#         visited = set()

#         return dfs(0) and len(visited) == n


"""
Union find
time: O(n log n)
space: O(n)
"""
# class UnionFind:
#     def __init__(self, size):
#         self.root = [i for i in range(size)]
#         self.rank = [1] * size
#         self.count = size

#     def find(self, x):
#         if x == self.root[x]:
#             return x
#         self.root[x] = self.find(self.root[x])
#         return self.root[x]

#     def union(self, x, y):
#         # if cycle return Fail, else return True
#         rootX = self.find(x)
#         rootY = self.find(y)

#         if rootX == rootY:  # cycle
#             return False

#         if self.rank[rootX] > self.rank[rootY]:
#             self.root[rootY] = rootX
#         elif self.rank[rootX] < self.rank[rootY]:
#             self.root[rootX] = rootY
#         else:
#             self.root[rootY] = rootX
#             self.rank[rootX] += 1

#         self.count -= 1
#         return True

#     def get_count(self):
#         return self.count

# class Solution:
#     def validTree(self, n: int, edges: List[List[int]]) -> bool:
#         uf = UnionFind(n)

#         for v1, v2 in edges:
#             if not uf.union(v1, v2):
#                 return False

#         return uf.get_count() == 1
