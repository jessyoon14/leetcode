#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    '''
    Basic recursion
    '''
    # def permute(self, nums: List[int]) -> List[List[int]]:
    #     if len(nums) < 2:
    #         return [nums]
    #     result = []
    #     for i in range(len(nums)):
    #         tail = nums[:i] + nums[i + 1:]
    #         tail_perms = self.permute(tail)
    #         for tail_perm in tail_perms:
    #             result.append(tail_perm + [nums[i]])
    #     return result

    """
    Recursion with helper function
    """
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         result = []
#         self.permute_rec([], nums, result)
#         return result

#     def permute_rec(self, prefix: List[int], nums: List[int], result: List[List[int]]):
#         if len(nums) == 0:
#             result.append(prefix)
#             return
#         for i in range(len(nums)):
#             self.permute_rec(prefix + [nums[i]], nums[:i] + nums[i+1:], result)

    '''
    Recursion with swap
    
    n + n * n-1 + n * (n-1) * (n-2) + ... + n!
    '''

    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.permute_rec(nums, 0, result)
        return result

    def permute_rec(self, nums: List[int], first: int, result: List[List[int]]):
        if first >= len(nums) - 1:
            result.append(nums[:])
            return

        for i in range(first, len(nums)):
            nums[first], nums[i] = nums[i], nums[first]
            self.permute_rec(nums, first + 1, result)
            nums[first], nums[i] = nums[i], nums[first]

    '''
    Iterative version with stack
    '''


# @lc code=end
