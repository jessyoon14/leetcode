#
# @lc app=leetcode id=1937 lang=python3
#
# [1937] Maximum Number of Points with Cost
#

# @lc code=start
"""
1. brute force : calculate points for all possible combinations -> O(n ^ m)
2. DP 
    time: O(m * n)
    space: O(n)
    
    f(i, j) = max score possible until (i, j), containing (i, j)
    f(i, j) = max(f(i-1, k) - abs(k - j)) where k: 0 ~ n-1
"""


class Solution:
    """
    Bottom-up DP
    time: O(m * n)
    space: O(m * n)
    """
#     def maxPoints(self, points: List[List[int]]) -> int:
#         n, m = len(points[0]), len(points)
#         dp = [[0] * n for _ in range(m)]

#         for j in range(n):
#             dp[0][j] = points[0][j]
#         for i in range(1, m):
#             # get max points from left
#             dp[i][0] = dp[i-1][0]
#             for j in range(1, n):
#                 dp[i][j] = max(dp[i-1][j], dp[i][j-1] - 1)
#             for j in range(n-2, -1, -1):
#                 dp[i][j] = max(dp[i][j+1] - 1, dp[i][j])
#             for j in range(n):
#                 dp[i][j] = dp[i][j] + points[i][j]
#         return max(dp[-1])

    """
    Optimized bottom-up DP
    time: O(m * n)
    space: O(n)
    """

    # def maxPoints(self, points: List[List[int]]) -> int:
    #     n, m = len(points[0]), len(points)
    #     prev = [0] * n
    #     curr = [0] * n

    #     for j in range(n):
    #         prev[j] = points[0][j]
    #     for i in range(1, m):
    #         # get max points from left
    #         curr[0] = prev[0]
    #         for j in range(1, n):
    #             curr[j] = max(prev[j], curr[j-1] - 1)
    #         for j in range(n-2, -1, -1):
    #             curr[j] = max(curr[j+1] - 1, curr[j])
    #         for j in range(n):
    #             curr[j] = curr[j] + points[i][j]
    #         curr, prev = prev, curr
    #     return max(prev)

    """
    In-place dp
    time = O(m*n)
    space = O(1)
    """

    def maxPoints(self, points: List[List[int]]) -> int:
        for i, row in enumerate(points[:-1]):
            for j in range(1, len(row)):
                row[j] = max(row[j], row[j-1] - 1)
            for j in range(len(row) - 2, -1, -1):
                row[j] = max(row[j], row[j+1] - 1)
            for j in range(len(row)):
                points[i+1][j] += points[i][j]
        return max(points[-1])

    # @lc code=end
