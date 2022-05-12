#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
class Solution:
    """
    Top-down DP
    Time complexity: O(n^2)
    Space complexity: O(n)
    dp[i] = max(dp[j] + 1) for all j where nums[j] < nums[i] and j < i
    """
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         self.max_len = 1

#         # @lru_cache(None)
#         def dp(right): # len of longest increasing subsequence ending with index i
#             if memo[right]:
#                 return memo[right]

#             curr_len = 1
#             for i in range(right - 1, -1, -1):
#                 if nums[i] < nums[right]:
#                     curr_len = max(curr_len, dp(i) + 1)
#             self.max_len = max(self.max_len, curr_len)
#             memo[right] = curr_len
#             return curr_len

#         n = len(nums)
#         memo = [0] * n

#         for i in range(n-1, -1, -1):
#             dp(i)
#         return self.max_len

    """
    Bottom-up DP
    Time complexity: O(n^2)
    Space complexity: O(n)
    """
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         n = len(nums)
#         dp = [1] * n
#         for i in range(1, n):
#             for j in range(i-1, -1, -1):
#                 if nums[j] < nums[i]:
#                     dp[i] = max(dp[i], dp[j] + 1)

#         return max(dp)

    """
    Intelligently build a subsequence
    Time complexity: O(n ^ 2)
    Space complexity: O(n)
    """
    # def lengthOfLIS(self, nums: List[int]) -> int:
    #     subsequence = [nums[0]]
    #     n = len(nums)
    #     for i in range(1, n):
    #         # if new element is larger than the largest in subsequence
    #         if nums[i] > subsequence[-1]:
    #             subsequence.append(nums[i])
    #         else:
    #             j = 0
    #             while nums[i] > subsequence[j]:
    #                 j += 1
    #             subsequence[j] = nums[i]
    #             # for j in range(len(subsequence)):
    #             #     if subsequence[j] >= nums[i]:
    #             #         subsequence[j] = nums[i]
    #             #         break
    #     return len(subsequence)

    """
    Binary search
    Time complexity: O(n * log n)
    Space complexity: O(n)
    """

    def lengthOfLIS(self, nums: List[int]) -> int:
        def binary_search(num):
            left = 0
            right = len(subsequence)

            while left < right:
                mid = (left + right) // 2
                mid_val = subsequence[mid]
                if mid_val >= num:
                    right = mid
                else:
                    left = mid + 1
            return left

        subsequence = [nums[0]]
        n = len(nums)
        for i in range(1, n):
            # if new element is larger than the largest in subsequence
            if nums[i] > subsequence[-1]:
                subsequence.append(nums[i])
            else:
                # index of first element greater than or equal to num
                j = binary_search(nums[i])
                subsequence[j] = nums[i]
        return len(subsequence)
# @lc code=end
