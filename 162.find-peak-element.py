#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#

# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if mid == left:
                if nums[left] < nums[right]:
                    left += 1
                break

            left_is_small = nums[mid-1] < nums[mid]
            right_is_small = nums[mid+1] < nums[mid]
            if left_is_small:
                left = mid
            if right_is_small or not left_is_small:
                right = mid

        return left

# @lc code=end

# Better iterative solution
# public class Solution {
#     public int findPeakElement(int[] nums) {
#         int l = 0, r = nums.length - 1;
#         while (l < r) {
#             int mid = (l + r) / 2;
#             if (nums[mid] > nums[mid + 1])
#                 r = mid;
#             else
#                 l = mid + 1;
#         }
#         return l;
#     }
# }

# Recursive solution
# public class Solution {
#     public int findPeakElement(int[] nums) {
#         return search(nums, 0, nums.length - 1);
#     }
#     public int search(int[] nums, int l, int r) {
#         if (l == r)
#             return l;
#         int mid = (l + r) / 2;
#         if (nums[mid] > nums[mid + 1])
#             return search(nums, l, mid);
#         return search(nums, mid + 1, r);
#     }
