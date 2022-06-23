#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

# @lc code=start
'''
1. normal permutations + use set to remove duplicates
2. normal permutations + skip same numbers (either sort or keep set of seen)

[1, 1, 2]

for i in nums
    1  + [1, 2]
    1 -> x
    2 + [1, 1]
'''


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        nums.sort()
        results = []
        curr_perm = []
        self.permute(nums, curr_perm, results)

        return results

    def permute(self, nums, curr_perm, results):
        if len(nums) == 0:
            results.append(curr_perm[:])
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]:
                continue
            prev = num
            curr_perm.append(num)
            new_nums = nums[:i] + nums[i + 1:]
            self.permute(new_nums, curr_perm, results)
            curr_perm.pop()

    '''
    Use counter to process unique elem once
    time, space same
    less time overhead (linear) but need linear space overhead
    '''

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        results = []

        def backtrack(comb, counter):
            if len(comb) == len(nums):
                results.append(comb[:])

            for num in counter:
                if counter[num] > 0:
                    comb.append(num)
                    counter[num] -= 1
                    backtrack(comb, counter)
                    comb.pop()
                    counter[num] += 1
        backtrack([], Counter(nums))
        return results


# @lc code=end
