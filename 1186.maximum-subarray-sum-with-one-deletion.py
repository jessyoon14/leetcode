#
# @lc app=leetcode id=1186 lang=python3
#
# [1186] Maximum Subarray Sum with One Deletion
#

# @lc code=start
class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)

        remove0 = [0] * n
        remove1 = [0] * n
        remove0[0] = arr[0]
        remove1[0] = arr[0]

        for i in range(1, n):
            remove0[i] = max(remove0[i-1] + arr[i], arr[i])
            remove1[i] = max(remove1[i-1] + arr[i], arr[i])

            if i >= 2:
                remove1[i] = max(remove1[i], remove0[i-2] + arr[i])

        return max(remove1)


#     def maximumSum(self, arr: List[int]) -> int:
#         if min(arr) > -1:
#             return sum(arr)
#         elif max(arr) <= 0:
#             return max(arr)

#         min_el = min(arr) - 1

#         left_sum = [min_el] * len(arr)
#         left_sum[0] = max(0, arr[0])
#         right_sum = [min_el] * len(arr)
#         right_sum[-1] = max(0, arr[-1])

#         def getMaxSumLeft(right):
#             if right < 0:
#                 return 0
#             if left_sum[right] > min_el:
#                 return left_sum[right]

#             left_sum[right] = max(0, arr[right] + getMaxSumLeft(right - 1))
#             return left_sum[right]

#         def getMaxSumRight(left):
#             if left >= len(arr):
#                 return 0
#             if right_sum[left] > min_el:
#                 return right_sum[left]

#             # arr[left]만 비교해야할듯
#             right_sum[left] = max(0, arr[left] + getMaxSumRight(left + 1))
#             return right_sum[left]


#         max_sum = 0
#         for i, n in enumerate(arr):
#             if n > 0:
#                 continue
#             else:
#                 curr_left_sum = getMaxSumLeft(i - 1)
#                 curr_right_sum = getMaxSumRight(i + 1)
#                 max_sum = max(max_sum, curr_left_sum + curr_right_sum)
#         return max_sum

# @lc code=end
