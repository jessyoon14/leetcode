#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#

# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        # find drop
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:  # ith is drop element
                # swap drop element with minimum element from tail that's greater than drop
                j = len(nums) - 1
                while nums[j] <= nums[i]:
                    j -= 1
                nums[i], nums[j] = nums[j], nums[i]
                reverse(i+1, len(nums) - 1)
                return

        # if no drop, sort everything
        reverse(0, len(nums) - 1)

# @lc code=end
