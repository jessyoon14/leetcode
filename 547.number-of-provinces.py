#
# @lc app=leetcode id=547 lang=python3
#
# [547] Number of Provinces
#

# @lc code=start
"""
DFS
Time: O(n^2) -> each row only traversed once!!!!! (complete matrix of size n^2 is traversed)
Space: O(n)
"""
# class Solution:
#     def findCircleNum(self, isConnected: List[List[int]]) -> int:
#         def visit(city: int):
#             if visited[city]:
#                 return

#             visited[city] = True
#             for i in range(num_cities):
#                 if isConnected[city][i]:
#                     visit(i)

#         num_cities = len(isConnected)
#         num_provinces = 0
#         visited = [False] * num_cities

#         for city in range(num_cities):
#             if not visited[city]:
#                 visit(city)
#                 num_provinces += 1

#         return num_provinces


"""
BFS
Time: O(n^2) -> complete matrix of size n^2 is traversed
Soace: O(n) -> queue & visited can grow to n
"""
# class Solution:
#     def findCircleNum(self, isConnected: List[List[int]]) -> int:

#         def visit(city): # use bfs to visit
#             queue = deque([city])
#             visited[city] = True

#             while queue:
#                 city = queue.pop()
#                 for other_city in range(num_cities):
#                     if isConnected[city][other_city] and not visited[other_city]:
#                         visited[other_city] = True
#                         queue.append(other_city)

#         num_cities = len(isConnected)
#         num_provinces = 0
#         visited = [False] * num_cities

#         for i in range(num_cities):
#             if not visited[i]:
#                 visit(i)
#                 num_provinces += 1

#         return num_provinces


"""
UnionFind
Time: O(n * n * log(n))
Space: O(n)

"""
# class UnionFind:
#     def __init__(self, size): # O(n)
#         self.root = [i for i in range(size)]
#         self.rank = [1] * size

#     def find(self, x): # log(n)
#         if x == self.root[x]:
#             return x
#         self.root[x] = self.find(self.root[x])
#         return self.root[x]

#     def union(self, x, y): # log(n)
#         rootX = self.find(x)
#         rootY = self.find(y)

#         if rootX != rootY:
#             if self.rank[rootX] > self.rank[rootY]:
#                 self.root[rootY] = rootX
#             elif self.rank[rootX] < self.rank[rootY]:
#                 self.root[rootX] = rootY
#             else:
#                 self.root[rootY] = rootX
#                 self.rank[rootX] += 1

#     def organize_roots(self):
#         for i in range(len(self.root)):
#             self.root[i] = self.find(self.root[i])

# class Solution:
#     def findCircleNum(self, isConnected: List[List[int]]) -> int:
#         num_cities = len(isConnected)
#         uf = UnionFind(num_cities)

#         for i in range(num_cities):
#             for j in range(i + 1, num_cities):
#                 if isConnected[i][j]:
#                     uf.union(i, j)

#         uf.organize_roots()
#         return len(set(uf.root))

"""
Better union find (increment number of unique roots with each union)
time: O(n*n) -> with path compression & rank, find & union is O(1) on average
space: O(n)
"""


class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size
        self.count = size

    def find(self, x):
        if x == self.root[x]:
            return x

        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            self.count -= 1
            if self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            elif self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            else:
                self.root[rootX] = rootY
                self.rank[rootY] += 1

    def get_count(self):
        return self.count


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        if not isConnected:
            return 0

        n = len(isConnected)
        uf = UnionFind(n)
        for row in range(n):
            for col in range(row + 1, n):
                if isConnected[row][col] == 1:
                    uf.union(row, col)

        return uf.get_count()

# @lc code=end
