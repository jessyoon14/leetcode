#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
# one-pass
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        nums_dict = {}  # val -> idx
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in nums_dict:
                return i, nums_dict[complement]
            nums_dict[nums[i]] = i

        return [-1, -1]

# Two-pass
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         nums_dict = {} # val -> idx
#         for i in range(len(nums)):
#             nums_dict[nums[i]] = i

#         for i in range(len(nums)):
#             complement_idx = nums_dict.get(target - nums[i])
#             if complement_idx and complement_idx != i:
#                 return [complement_idx, i]

#         return [-1, -1]

# @lc code=end
