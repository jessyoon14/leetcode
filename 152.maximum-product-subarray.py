#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#

# @lc code=start
class Solution:
    """
    Brute Force
    Time complexity: O(n * 2)
    Space complexity: O(1)
    """
#     def maxProduct(self, nums: List[int]) -> int:
#         if not nums:
#             return 0

#         n = len(nums)
#         max_product = nums[0]
#         for left in range(n):
#             curr_product = 1
#             for right in range(left, n):
#                 curr_product *= nums[right]
#                 max_product = max(max_product, curr_product)
#         return max_product

    """
    Dynamic Programming
    Time complexity: O(N)
    Space complexity: O(1)
    Keep track of max_so_far, min_so_far (both calculated with curr, max_so_far*curr, min_so_far*curr)
    0 resets max_so_far and min_so_far
    """

    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        max_so_far = nums[0]
        min_so_far = nums[0]
        result = max_so_far

        for i in range(1, len(nums)):
            curr = nums[i]
            temp_max = max(curr, max_so_far * curr, min_so_far * curr)
            min_so_far = min(curr, max_so_far * curr, min_so_far * curr)
            max_so_far = temp_max

            result = max(max_so_far, result)
        return result

    """
    Failed attempt at DP...
    """

#    def maxProduct(self, nums: List[int]) -> int:
#         n = len(nums)
#         last_neg_idx = -1
#         last_zero_idx = -1
#         max_product = nums[0]
#         dp = [0] * n
#         dp[0] = nums[0]
#         if nums[0] < 0:
#             last_neg_idx = 0

#         for i in range(1, n):
#             if nums[i] < 0:
#                 if last_neg_idx < 0:        # first neg number
#                     dp[i] = nums[i]
#                 elif last_neg_idx < last_zero_idx < i:
#                     dp[i] = 0
#                 else:                       # product including last neg number
#                     # max product before last neg
#                     before_last_neg = dp[last_neg_idx - 1] if last_neg_idx > 0 else 1
#                     # last neg
#                     last_neg = nums[last_neg_idx]
#                     # nums between last neg and curr neg
#                     after_last_neg = dp[i-1] if (dp[last_neg_idx] <= 0 and last_neg_idx < i - 1) else dp[i-1] // dp[last_neg_idx]
#                     dp[i] = before_last_neg * last_neg * after_last_neg * nums[i]
#                 last_neg_idx = i
#             elif nums[i] == 0:
#                 last_zero_idx = i
#                 dp[i] = 0
#             else:
#                 if dp[i-1] > 0:
#                     dp[i] = dp[i-1] * nums[i]
#                 else:
#                     dp[i] = nums[i]
#             max_product = max(max_product, dp[i])

#         return max_product


# @lc code=end
