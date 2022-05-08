#
# @lc app=leetcode id=410 lang=python3
#
# [410] Split Array Largest Sum
#

# @lc code=start
class Solution:
    """
    Bottom up dynamic programming
    Time complexity: O(n^2 * m)
    Space complexity: O(n * m)
    """
#     def splitArray(self, nums: List[int], m: int) -> int:
#         n = len(nums)
#         memo = [[0] * (m+1) for _ in range(n)]
#         prefix_sum = [0] + list(itertools.accumulate(nums))

#         for subarray_count in range(1, m+1):
#             for curr_index in range(n):
#                 if subarray_count == 1: # base case
#                     memo[curr_index][subarray_count] = prefix_sum[n] - prefex_sum[curr_index]
#                     continue

#                 # recurrence relation
#                 minimum_largest_split_sum = prefix_sum[n]
#                 for i in range(curr_index, n - subarray_count + 1):
#                     first_split_sum = prefix_sum[i+1] - prefix_sum[curr_index]
#                     largest_split_sum = max(first_split_sum, memo[i+1][subarray_count - 1])

#                     minimum_largest_split_sum = min(minimum_largest_split_sum, largest_split_sum)
#                     if first_split_sum >= minimum_largest_split_sum:
#                         break

#                 memo[curr_index][subarray_count] = minimum_largest_split_sum

#         return memo[0][m]

    """
    Top Down Dynamic Programming
    Time complexity: O(n^2 * m) -> must visit each state (n, m), and each state needs O(n) because of for loop
    Space complexity: O(n*m)
    """
#     def splitArray(self, nums: List[int], m: int) -> int:
#         n = len(nums)
#         prefix_sum = [0] + list(itertools.accumulate(nums))

#         @functools.lru_cache(None)
#         def get_min_largest_split_sum(curr_index: int, subarray_count: int):
#             if subarray_count == 1:
#                 return prefix_sum[n] - prefix_sum[curr_index]

#             minimum_largest_split_sum = prefix_sum[n]
#             for i in range(curr_index, n - subarray_count + 1):
#                 first_split_sum = prefix_sum[i + 1] - prefix_sum[curr_index]
#                 largest_split_sum = max(first_split_sum, get_min_largest_split_sum(i+1, subarray_count - 1))
#                 minimum_largest_split_sum = min(minimum_largest_split_sum, largest_split_sum)
#                 if first_split_sum >= minimum_largest_split_sum:
#                     break
#             return minimum_largest_split_sum
#         return get_min_largest_split_sum(0, m)

    """
    Binary search
    Time complexity: O(n * log(s)), s: sum of ints in array
    Space complexity: O(1)
    """

    def splitArray(self, nums: List[int], m: int) -> int:
        def min_subarrays_required(max_sum_allowed: int) -> int:
            current_sum = 0
            splits_required = 0

            for element in nums:
                if current_sum + element <= max_sum_allowed:
                    current_sum += element
                else:
                    current_sum = element
                    splits_required += 1
            return splits_required + 1

        left = max(nums)
        right = sum(nums)
        while left <= right:
            max_sum_allowed = (left + right) // 2
            if min_subarrays_required(max_sum_allowed) <= m:
                right = max_sum_allowed - 1
                minimum_largest_split_sum = max_sum_allowed
            else:
                left = max_sum_allowed + 1
        return minimum_largest_split_sum

    """
    Top Down Dynamic Programming
    """
#     def splitArray(self, nums: List[int], m: int) -> int:
#         n = len(nums)
#         dp = {}

#         def get_max_partial_sum(start, m):
#             if (start, m) in dp:
#                 return dp[(start, m)]

#             if m == 1:
#                 dp[(start, m)] = sum(nums[start:])
#                 return dp[(start, m)]
#             if n - start + 1 == m:
#                 dp[(start, m)] = max(nums[start:])
#                 return dp[(start, m)]

#             min_sum = float('inf')
#             curr_group_sum = nums[start]
#             for i in range(start + 1, n - m + 2):
#                 other_groups_sum = get_max_partial_sum(i, m - 1)
#                 min_sum = min(min_sum, max(curr_group_sum, other_groups_sum))
#                 curr_group_sum += nums[i]

#             dp[(start, m)] = min_sum
#             return min_sum

#         return get_max_partial_sum(0, m)
# @lc code=end
