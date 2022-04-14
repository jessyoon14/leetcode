#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start

class Solution:
    # optimal, with swap
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1

    # easy O(n), move all nonzeros to front
#    def moveZeroes(self, nums: List[int]) -> None:
#         last_nonzero = 0

#         for cur in range(len(nums)):
#             if nums[cur] != 0:
#                 nums[last_nonzero] = nums[cur]
#                 last_nonzero += 1

#         for i in range(last_nonzero, len(nums)):
#             nums[i] = 0

#     first attempt. unnecessarily complicated. Don't need to calculate left.
#     def moveZeroes(self, nums: List[int]) -> None:
#         left = 0
#         for right in range(0, len(nums)):
#             if nums[right] == 0:
#                 continue
#             while left < right - 1 and nums[left] != 0:
#                 left += 1
#             if nums[left] == 0:
#                 nums[left], nums[right] = nums[right], nums[left]
#         return nums

# @lc code=end
