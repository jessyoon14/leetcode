#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        to_fill = len(nums1) - 1
        i1, i2 = m - 1, n - 1

        while i1 > -1 and i2 > -1:
            if nums1[i1] > nums2[i2]:
                nums1[to_fill] = nums1[i1]
                i1 -= 1
            else:
                nums1[to_fill] = nums2[i2]
                i2 -= 1
            to_fill -= 1

        for i in range(i2+1):
            nums1[i] = nums2[i]

# cleaner for loop


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # Set p1 and p2 to point to the end of their respective arrays.
        p1 = m - 1
        p2 = n - 1

        # And move p backwards through the array, each time writing
        # the smallest value pointed at by p1 or p2.
        for p in range(n + m - 1, -1, -1):
            if p2 < 0:
                break
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
# @lc code=end
