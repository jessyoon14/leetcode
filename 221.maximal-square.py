#
# @lc app=leetcode id=221 lang=python3
#
# [221] Maximal Square
#

# @lc code=start
class Solution:

    """
    Brute force
    Time complexity: O(m^2 * n^2)
    Space complexity: O(1)
    """
#     def maximalSquare(self, matrix: List[List[str]]) -> int:
#         def find_largest_square(start_i, start_j):
#             if matrix[start_i][start_j] == '0':
#                 return 0

#             size = 1
#             while start_i + size - 1 < n and start_j + size - 1 < m:
#                 # check new row
#                 for j in range(start_j, start_j + size):
#                     if matrix[start_i][j] == '0':
#                         return size

#                 # check new column
#                 for i in range(start_i, start_i + size):
#                     if matrix[i][start_j + size - 1] == '0':
#                         return size

#                 # check new corner
#                 if matrix[start_i + size - 1][start_j + size - 1] == '0':
#                     return size

#                 size += 1
#             return size - 1


#         n, m = len(matrix), len(matrix[0])
#         max_square = 0
#         for i in range(n):
#             for j in range(m):
#                 max_square = max(max_square, find_largest_square(i, j))
#         return max_square

    """
    Bottom-up DP -> simpler implementation
    Time complexity: O(n * m)
    Space complexity: O(n * m)
    """
#     def maximalSquare(self, matrix: List[List[str]]) -> int:
#         n, m = len(matrix), len(matrix[0])
#         dp = [[0] * (m + 1) for _ in range(n + 1)]

#         max_side = 0

#         for i in range(1, n + 1):
#             for j in range(1, m + 1):
#                 if matrix[i][j] == '1':
#                     dp[i][j] = min(dp[i - 1][j], dp[i-1][j-1], dp[i][j-1]) + 1
#                     max_side = max(max_side, curr)

#         return max_side ** 2

    """
    Space-optimized Bottom-up DP -> simpler implementation
    Time complexity: O(n * m)
    Space complexity: O(m)
    """

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n, m = len(matrix), len(matrix[0])
        prev = [0] * (m + 1)
        curr = [0] * (m + 1)

        max_side = 0

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if matrix[i-1][j-1] == '1':
                    curr[j] = min(prev[j], prev[j-1], curr[j-1]) + 1
                    max_side = max(max_side, curr[j])
                else:
                    curr[j] = 0  # CAREFUL: memory-optimize requires reset!!!!
            prev, curr = curr, prev

        return max_side ** 2

    """
    Bottom up DP
    """
#     def maximalSquare(self, matrix: List[List[str]]) -> int:
#         n, m = len(matrix), len(matrix[0])
#         dp = [[0] * m for _ in range(n)]

#         max_side = 0

#         for i in range(n):
#             for j in range(m):
#                 curr = 0
#                 if i == 0 or j == 0:
#                     curr = 0 if matrix[i][j] == '0' else 1
#                 elif matrix[i][j] == '1':
#                     curr = min(dp[i - 1][j], dp[i-1][j-1], dp[i][j-1]) + 1
#                 else:
#                     curr = 0
#                 dp[i][j] = curr
#                 max_side = max(max_side, curr)

#         return max_side ** 2

    """
    Top down DP - FAIL!
    Time complexity: O(n * m)
    Space complexity: O(n * m)
    """
#     def maximalSquare(self, matrix: List[List[str]]) -> int:
#         def dp(i, j):
#             curr = 0
#             if i == 0 or j == 0:
#                 curr = 0 if matrix[i][j] == '0' else 1

#             elif matrix[i][j] == '1':
#                 curr = min(dp(i - 1, j), dp(i-1, j-1), dp(i, j-1)) + 1
#             else:
#                 curr = 0

#             nonlocal max_side
#             max_side = max(max_side, curr)

#             return curr

#         n, m = len(matrix), len(matrix[0])
#         max_side = 0
#         return dp(n - 1, m - 1) ** 2
# @lc code=end
