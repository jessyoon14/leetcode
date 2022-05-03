#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    """
    Backtracking 1:
    Simulate all possible steps
    Time complexity: O(n^2), since 2^n maximum bound for possible steps to take (binary counting)
    Space complexity: O(n) for max recursion depth
    """
#     def canJump(self, nums: List[int]) -> bool:
#         def can_reach_end(n):
#             if n == len(nums) - 1:
#                 return True
#             for i in range(n + 1, min(n + nums[n] + 1, len(nums))):
#                 if can_reach_end(i):
#                     return True
#             return False


#         return can_reach_end(0)

    """
    Backtracking 2:
    Simulate all possible steps. For one step, iterate from max possible step to min possible step
    """
#     def canJump(self, nums: List[int]) -> bool:
#         def can_reach_end(n):
#             if n == len(nums) - 1:
#                 return True
#             for i in range(min(n + nums[n], len(nums) - 1), n, -1):
#                 if can_reach_end(i):
#                     return True
#             return False

#         return can_reach_end(0)

    """
    Top-down DP (aka optimized backtracking)
    Time complexity: O(n^2)
    Space complexity: O(n)
    """

    def canJump(self, nums: List[int]) -> bool:
        mem = [None] * len(nums)
        mem[-1] = True

        def can_reach_end(n):
            if mem[n] == False:
                return False
            for i in range(n + 1, min(n + nums[n] + 1, len(nums))):
                if can_reach_end(i):
                    return True
            mem[n] = False
            return False

        return can_reach_end(0)

    """
    Top-down DP
    f(n): furthest idx reachable from idx n
    f(n) = n + nums[n]
    """
#     def canJump(self, nums: List[int]) -> bool:
#         mem = [-1] * (len(nums))
#         mem[0] = nums[0]
#         def rec(n):
#             if mem[n] > -1:
#                 return mem[n]
#             prev = rec(n-1)
#             result = n
#             if prev >= n:
#                 result = max(prev, n + nums[n])
#             mem[n] = result
#             return result

#         if len(nums) == 1:
#             return True

#         rec(len(nums) - 1)
#         return mem[-2] >= len(nums) - 1

    """
    Bottom-up DP
    Time complexity: O(n^2)
    Space complexity: O(n)
    """
#     def canJump(self, nums: List[int]) -> bool:
#         dp = [False] * len(nums)
#         dp[-1] = True

#         for i in range(len(nums) - 2, -1, -1):
#             if i + nums[i] >= len(nums):
#                 dp[i] = True
#             for j in range(i + 1, i + nums[i] + 1,):
#                 if dp[j]:
#                     dp[i] = True
#                     break
#         return dp[0]

    """
    Greedy
    Time complexity: O(n)
    Space complexity: O(1)
    """

    def canJump(self, nums: List[int]) -> bool:
        leftmost_good = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= leftmost_good:
                leftmost_good = i
        return leftmost_good == 0

    """
    My solution: one pass
    """
#     def canJump(self, nums: List[int]) -> bool:
#         farthest_idx = 0
#         for i in range(len(nums)):
#             if i > farthest_idx: # cannot cross
#                 return False
#             farthest_idx = max(farthest_idx, i + nums[i])
#             if farthest_idx >= len(nums) - 1:
#                 return True


# @lc code=end
