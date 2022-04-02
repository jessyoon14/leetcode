#
# @lc app=leetcode id=384 lang=python3
#
# [384] Shuffle an Array
#

# @lc code=start

# Solution: Fisher-Yates -> Fails the solution checker though
class Solution:

    def __init__(self, nums: List[int]):
        self.array = nums
        self.original = list(nums)

    def reset(self) -> List[int]:
        self.array = self.original
        self.original = list(self.original)
        return self.array

    def shuffle(self) -> List[int]:
        for i in range(len(self.array)):
            swap_idx = random.randrange(i, len(self.array))
            temp = self.array[swap_idx]
            self.array[swap_idx] = self.array[i]
            self.array[i] = temp
            return self.array


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
# @lc code=end

# using python's random number generator
# class Solution:

#     def __init__(self, nums: List[int]):
#         self.nums = nums
#         self.shuffled_nums = nums.copy()
#         self.shuffled = False

#     def reset(self) -> List[int]:
#         return self.nums.copy()

#     def shuffle(self) -> List[int]:
#         random.shuffle(self.shuffled_nums)
#         return self.shuffled_nums.copy()

# Solution: Naive shuffle (slow, pick from a bag)
# class Solution:

#     def __init__(self, nums: List[int]):
#         self.array = nums
#         self.original = list(nums)

#     def reset(self) -> List[int]:
#         self.array = self.original
#         self.original = list(self.original)
#         return self.array


#     def shuffle(self) -> List[int]:
#         aux = list(self.array)

#         for idx in range(len(self.array)):
#             remove_idx = random.randrange(len(aux))
#             self.array[idx] = aux.pop(remove_idx)
#         return self.array
