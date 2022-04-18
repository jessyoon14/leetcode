#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    # clean bitvector solution
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = []

        for i in range(2**n, 2**(n+1)):
            bitmask = bin(i)[3:]
            output.append([nums[j] for j in range(n) if bitmask[j] == '1'])

        return output

    # backtracking
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         def backtrack(first = 0, curr = []):
#             if len(curr) == k:
#                 output.append(curr[:])
#                 return
#             for i in range(first, n):
#                 curr.append(nums[i])
#                 backtrack(i + 1, curr)
#                 curr.pop()

#         output = []
#         n = len(nums)
#         for k in range(n+1):
#             backtrack()
#         return output

    # bit vector solution
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         def generate_subset(i): # generate subsets from idx 0 ~ i inclusive
#             curr_mask = 1 << (len(nums) - 1)
#             result = []
#             for val in nums:
#                 if (curr_mask & i) > 0:
#                     result.append(val)
#                 curr_mask //= 2
#             return result

#         result = []
#         for i in range(1 << len(nums)):
#             result.append(generate_subset(i))
#         return result

    # cleaner iterative solution
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         n = len(nums)
#         output = [[]]

#         for num in nums:
#             output += [cur + [num] for curr in output]
#         return output

    # iterative solution
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         result = [[]]

#         for n in nums:
#             count = len(result)
#             for i in range(count):
#                 result.append(result[i] + [n])

#         return result


#     # recursive solution (memory optimized)
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         def rec(end_idx: int):
#             if end_idx < 0:
#                 return [[]]

#             subsets_without = rec(end_idx - 1)
#             count = len(subsets_without)

#             for i in range(count):
#                 subsets_without.append(subsets_without[i] + [nums[end_idx]])
#             return subsets_without

#         return rec(len(nums) - 1)

#     # recursive solution (upoptimized)
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         if nums == []:
#             return [[]]

#         subsets_without = self.subsets(nums[1:])
#         count = len(subsets_without)

#         for i in range(count):
#             subsets_without.append(subsets_without[i] + [nums[0]])
#         return subsets_without


# @lc code=end
