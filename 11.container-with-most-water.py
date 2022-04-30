#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:

    """
    Brute force: O(n^2)
    """

    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        for i in range(len(height) - 1):
            for j in range(i+1, len(height)):
                max_area = max(max_area, min(height[i], height[j]) * (j - i))
        return max_area

    """
    Two pointer
    """

    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_water = 0
        while left < right:
            # get curr water & update max_water
            lh, rh = height[left], height[right]
            if lh > rh:
                max_water = max(max_water, rh * (right - left))
                right -= 1
            else:
                max_water = max(max_water, lh * (right - left))
                left += 1
        return max_water

# @lc code=end
