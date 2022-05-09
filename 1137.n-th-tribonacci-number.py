#
# @lc app=leetcode id=1137 lang=python3
#
# [1137] N-th Tribonacci Number
#

# @lc code=start
class Solution:
    """
    Top down DP
    Time complexity: O(n)
    Space complexity: O(n)
    """
#     def tribonacci(self, n: int) -> int:
#         def dp(i):
#             if i == 0:
#                 return 0
#             elif i == 1 or i == 2:
#                 return 1

#             if i in memo:
#                 return memo[i]

#             memo[i] = dp(i-1) + dp(i-2) + dp(i-3)
#             return memo[i]

#         memo = {}
#         return dp(n)

    """
    Bottom up DP
    Time complexity: O(n)
    Space complexity: O(n)
    """
#     def tribonacci(self, n: int) -> int:
#         if n == 0:
#             return 0
#         elif n == 1 or n == 2:
#             return 1

#         dp = [0] * (n + 1)
#         dp[1] = 1
#         dp[2] = 1

#         for i in range(3, n + 1):
#             dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

#         return dp[n]

    """
    Bottom up DP (Space optimized)
    Time complexity: O(n)
    Space complexity: O(1)
    """

    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1

        prev1 = 0
        prev2 = 1
        prev3 = 1

        for i in range(3, n + 1):
            curr = prev1 + prev2 + prev3
            prev1, prev2, prev3 = prev2, prev3, curr

        return prev3
# @lc code=end
