#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
'''
Use prefix sums in set
time O(n)
space O(n)
'''


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sums = {0: 1}
        curr_sum = 0
        count = 0
        for i, num in enumerate(nums):
            curr_sum += num

            if curr_sum - k in prefix_sums:
                count += prefix_sums[curr_sum - k]

            prefix_sums[curr_sum] = prefix_sums[curr_sum] + \
                1 if curr_sum in prefix_sums else 1

        return count

# @lc code=end
