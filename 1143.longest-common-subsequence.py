#
# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#

# @lc code=start
class Solution:
    """
    Top down
    Time complexity: O(m*n)
    Space complexity: O(m*n)
    """
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         # from functools import lru_cache
#         @lru_cache(2000)
#         def dp(i, j):
#             if i == 0 or j == 0:
#                 return 0

#             if text1[i-1] == text2[j-1]:
#                 return dp(i-1, j-1) + 1
#             else:
#                 return max(dp(i, j - 1), dp(i - 1, j))

#         n, m = len(text1), len(text2)
#         return dp(n, m)

#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         # from functools import lru_cache
#         def dp(i, j):
#             if i == 0 or j == 0:
#                 return 0

#             if (i, j) in memo:
#                 return memo[(i, j)]

#             if text1[i-1] == text2[j-1]:
#                 memo[(i, j)] = dp(i-1, j-1) + 1
#             else:
#                 memo[(i, j)] = max(dp(i, j - 1), dp(i - 1, j))
#             return memo[(i, j)]

#         n, m = len(text1), len(text2)
#         memo = {}
#         return dp(n, m)

    """
    Bottom up
    Time complexity: O(m * n)
    Space complexity: O(m * n)
    """
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         n, m = len(text1), len(text2)
#         dp = [[0] * (m+1) for _ in range(n+1)]

#         for i in range(1, n + 1):
#             for j in range(1, m + 1):
#                 if text1[i - 1] == text2[j - 1]:
#                     dp[i][j] = dp[i-1][j-1] + 1
#                 else:
#                     dp[i][j] = max(dp[i][j-1], dp[i-1][j])
#         return dp[n][m]

    """
    Bottom up
    Time complexity: O(m * n)
    Space complexity: O(n)
    """

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text2) > len(text1):
            text1, text2 = text2, text1

        n, m = len(text1), len(text2)
        curr = [0] * (m+1)
        prev = [0] * (m+1)

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if text1[i - 1] == text2[j - 1]:
                    curr[j] = prev[j-1] + 1
                else:
                    curr[j] = max(curr[j-1], prev[j])
            prev, curr = curr, prev
        return prev[m]

# @lc code=end
