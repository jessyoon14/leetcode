#
# @lc app=leetcode id=528 lang=python3
#
# [528] Random Pick with Weight
#

# @lc code=start
class Solution:

    """
    Prefix sum + linear search
    Constructor:
        time: O(n)
        space: O(n)
    pick:
        time: O(n)
        space: O(1)
    """
#     def __init__(self, w: List[int]):
#         self.prefix_sums = []
#         prefix_sum = 0
#         for weight in w:
#             prefix_sum += weight
#             self.prefix_sums.append(prefix_sum)
#         self.total_sum = prefix_sum

#     def pickIndex(self) -> int:
#         target = self.total_sum * random.random()
#         for i, prefix_sum in enumerate(self.prefix_sums):
#             if target < prefix_sum:
#                 return i

    """
    Prefix sum + linear search
    Constructor:
        time: O(n)
        space: O(n)
    pick:
        time: O(log n)
        space: O(1)
    """

    def __init__(self, w: List[int]):
        self.prefix_sums = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefix_sums.append(prefix_sum)
        self.total_sum = prefix_sum

    def pickIndex(self) -> int:
        target = self.total_sum * random.random()
        left, right = 0, len(self.prefix_sums) - 1

        while left < right:
            mid = (left + right) // 2
            if self.prefix_sums[mid] >= target:
                right = mid
            else:
                left = mid + 1

        return left

    """
    Prefix sum + binary search
    Assign each index a region in the number line with length corresponding to its probability
    In pick, pick a random numb
    """
#     def __init__(self, w: List[int]):
#         acc_probs = []
#         weight_sum = sum(w)
#         acc_prob = 0
#         for weight in w:
#             acc_prob += weight/weight_sum
#             acc_probs.append(acc_prob)

#         self.acc_probs = acc_probs

#     def pickIndex(self) -> int:
#         target = random.random()
#         # find index of first value >= to target -> all bounds are left-excl, right-incl
#         left, right = 0, len(self.acc_probs) - 1
#         while left < right:
#             mid = (left + right) // 2
#             if self.acc_probs[mid] == target:
#                 return mid
#             elif self.acc_probs[mid] > target:
#                 right = mid
#             else:
#                 left = mid + 1
#         return left

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
# @lc code=end
