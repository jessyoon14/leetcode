#
# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#

# @lc code=start
class Solution:
    """
    Top down DP
    Time complexity: O(n)
    Space complexity: O(n)
    """
#     def minCostClimbingStairs(self, cost: List[int]) -> int:
#         def dp(i):
#             if i == 0:
#                 return 0
#             if i == 1:
#                 return 0

#             if i not in memo:
#                 memo[i] = min(dp(i-1) + cost[i-1], dp(i-2) + cost[i-2])

#             return memo[i]

#         memo = {}
#         return dp(len(cost))

    """
    Bottom up DP
    Time complexity: O(n)
    Space complexity: O(n) -> can be optimized to O(1)
    """
#     def minCostClimbingStairs(self, cost: List[int]) -> int:
#         n = len(cost)
#         if n < 2:
#             return 0
#         if n < 3:
#             return min(cost)

#         dp = [0] * (n+1)

#         for i in range(2, n+1):
#             dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])

#         return dp[n]

    """
    Bottom up DP with constant space
    Time complexity: O(n)
    Space complexity: O(1)
    """

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n < 2:
            return 0
        if n < 3:
            return min(cost)

        down_one = 0
        down_two = 0

        for i in range(2, n+1):
            curr_cost = min(down_one + cost[i-1], down_two + cost[i-2])
            down_two = down_one
            down_one = curr_cost

        return down_one
# @lc code=end
