#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
# Brute force solution
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         max_sum = nums[0]
#         curr_sum = 0
#         for left in range(len(nums)):
#             curr_sum = 0
#             for right in range(left, len(nums)):
#                 curr_sum += nums[right]
#                 max_sum = max(max_sum, curr_sum)

#         return max_sum


# Divide-and-conqeur solution
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def maxSubArrayRecursive(left: int, right: int) -> int:
            if left > right:
                return -math.inf

            mid = (left + right) // 2
            curr_sum = best_left_sum = best_right_sum = 0

            # right
            for i in range(mid + 1, right + 1):
                curr_sum += nums[i]
                best_left_sum = max(best_left_sum, curr_sum)

            # left
            curr_sum = 0
            for i in range(mid - 1, left - 1, -1):
                curr_sum += nums[i]
                best_right_sum = max(best_right_sum, curr_sum)

            middle_subarr = nums[mid] + best_left_sum + best_right_sum
            left_subarr = maxSubArrayRecursive(left, mid - 1)
            right_subarr = maxSubArrayRecursive(mid + 1, right)

            return max(middle_subarr, left_subarr, right_subarr)

        return maxSubArrayRecursive(0, len(nums) - 1)
# Linear solution (DP)


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        curr_sum = 0
        max_sum = nums[0]

        for n in nums:
            curr_sum = max(n, n + curr_sum)
            max_sum = max(curr_sum, max_sum)

        return max_sum

# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:

#         curr_sum = 0
#         max_sum = nums[0]

#         for n in nums:
#             if curr_sum < 0:
#                 curr_sum = 0
#             curr_sum += n
#             max_sum = max(curr_sum, max_sum)

#         return max_sum


# @lc code=end
