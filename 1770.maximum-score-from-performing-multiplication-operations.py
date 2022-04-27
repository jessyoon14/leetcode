#
# @lc app=leetcode id=1770 lang=python3
#
# [1770] Maximum Score from Performing Multiplication Operations
#

# @lc code=start
class Solution:
    # bottom-up DP -> need to redo!
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n, m = len(nums), len(multipliers)

        # initialize dp with width (m + 1) ** 2
        dp = [[0] * (m+1) for i in range(m+1)]

        for i in range(m-1, -1, -1):
            for j in range(i + 1):
                right = n - i + j - 1
                dp[i][j] = max(dp[i+1][j] + multipliers[i]*nums[right],
                               dp[i+1][j+1] + multipliers[i]*nums[j])

        return dp[0][0]
    """
    recurrence relation:
    dp(i, left) = max(
                    mult*nums[left] + dp[i+1, left+1], 
                    mult*nums[right] + dp[i+1, left])d
    """
    # top-down DP
#     def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
#         @lru_cache(2000)
#         def dp(i, left):
#             if i == m:
#                 return 0

#             mult = multipliers[i]
#             right = n - 1 - (i-left)
#             return max(mult * nums[left] + dp(i+1, left+1),
#                       mult * nums[right] + dp(i+1, left))
#         n, m = len(nums), len(multipliers)
#         return dp(0,0)

    # top-down recursion but tle
#     def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
#         n, m = len(nums), len(multipliers)

#         @lru_cache(2000)
#         def dp(l, i):
#             if i == m:
#                 return 0
#             pick_left = dp(l+1, i+1) + nums[l] * multipliers[i]
#             pick_right = dp(l, i+1) + nums[n-(i-l)-1] * multipliers[i]
#             return max(pick_left, pick_right)

#         return dp(0,0)

    # my initial memoization solution
#     def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
#         dp = dict()
#         def rec(i, left, right):
#             # base case
#             if i == len(multipliers):
#                 return 0

#             # check dp
#             if dp.get((i, left, right)):
#                 return dp[(i, left, right)]

#             # choose head
#             head_score = multipliers[i] * nums[left] + rec(i+1, left + 1, right)

#             # choose tail
#             tail_score = multipliers[i] * nums[right] + rec(i+1, left, right - 1)

#             dp[(i, left, right)] = max(head_score, tail_score)
#             return dp[(i, left, right)]

#         return rec(0, 0, len(nums) - 1)

# @lc code=end
