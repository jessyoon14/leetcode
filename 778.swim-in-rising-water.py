#
# @lc app=leetcode id=778 lang=python3
#
# [778] Swim in Rising Water
#

# @lc code=start
'''
binary search + BFS or DFS
time O(n^2 log n)
space O(n^2) -> BFS를 쓰든, DFS를 쓰든 Queue/Stack에 최대 n^2 element가 한번이 있을 수 있다!!!
'''
from collections import deque


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        if n < 2:
            return 0

        lower = 0
        upper = n * n - 1
        while lower < upper:
            mid = (lower + upper) // 2

            can_reach_end = self.can_reach_end_at(grid, mid)
            if can_reach_end:
                upper = mid
            else:
                lower = mid + 1

        return lower

    def can_reach_end_at(self, grid, time):
        if grid[0][0] > time:
            return False

        n = len(grid)
        visited = [[False for j in range(n)] for i in range(n)]
        queue = deque([(0, 0)])

        while queue:
            i, j = queue.popleft()

            neighbors = self.get_neighbors(n, i, j)

            for ni, nj in neighbors:
                if not visited[ni][nj] and grid[ni][nj] <= time:
                    if ni == n - 1 and nj == n - 1:
                        # print(time)
                        return True
                    visited[ni][nj] = True
                    queue.append((ni, nj))
        return False

    def can_reach_end_at_dfs(self, grid, time):
        stack = [(0, 0)]
        seen = {(0, 0)}
        while stack:
            r, c = stack.pop()
            if r == c == N-1:
                return True
            for cr, cc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                if (0 <= cr < N and 0 <= cc < N) and (cr, cc) not in seen and grid[cr][cc] <= time:
                    stack.apped((cr, cc))
                    seen.add((cr, cc))
        return False

    def get_neighbors(self, n, i, j):
        neighbors = []
        if i > 0:
            neighbors.append((i - 1, j))

        if j > 0:
            neighbors.append((i, j - 1))

        if i < n - 1:
            neighbors.append((i + 1, j))

        if j < n - 1:
            neighbors.append((i, j + 1))

        return neighbors


'''
1. Heap (priority queue)
time: O(n^2 log n)
space: O(n^2)
'''


# class Solution:
#     def swimInWater(self, grid: List[List[int]]) -> int:
#         N = len(grid)

#         seen = {(0, 0)}
#         pq = [(grid[0][0], 0, 0)]
#         ans = 0
#         while pq:
#             d, r, c = heapq.heappop(pq)
#             ans = max(ans, d)
#             if r == c == N-1:
#                 return ans
#             for cr, cc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
#                 if 0 <= cr < N and 0 <= cc < N and (cr, cc) not in seen:
#                     heapq.heappush(pq, (grid[cr][cc], cr, cc))
#                     seen.add((cr, cc))


'''
3. Minimal spanning tree algorithm (union find)
TODO
'''
# class Solution:
#     def swimInWater(self, grid: List[List[int]]) -> int:


# @lc code=end
