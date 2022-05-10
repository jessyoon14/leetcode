#
# @lc app=leetcode id=740 lang=python3
#
# [740] Delete and Earn
#

# @lc code=start
class Solution:
    """
    Top down DP
    Time complexity: O(n + k) (k: max number)
    Space complexity: O(n + k)
    """
#     def deleteAndEarn(self, nums: List[int]) -> int:
#         points = defaultdict(int)
#         max_number = 0
#         for num in nums:
#             points[num] += num
#             max_number = max(max_number, num)

#         @cache
#         def max_points(num):
#             if num == 0:
#                 return 0
#             if num == 1:
#                 return points[1]
#             return max(max_points(num - 1), max_points(num - 2) + points[num])

#         return max_points(max_number)

    """
    Bottom up DP -> 무조건 가장 간단하게 짜고 추후 optimize하자
    Time complexity: O(n + k)
    Space complexity: O(n + k)
    """
#     def deleteAndEarn(self, nums: List[int]) -> int:
#         points = defaultdict(int)
#         max_number = 0

#         for num in nums:
#             points[num] += num
#             max_number = max(max_number, num)

#         max_points = [0] * (max_number + 1)
#         max_points[1] = points[1]

#         for num in range(2, len(max_points)):
#             max_points[num] = max(max_points[num-1], max_points[num-2] + points[num])

#         return max_points[max_number]

    """
    Space optimized Bottom up DP
    Time complexity: O(n + k)
    Space complexity: O(n)
    """

    # def deleteAndEarn(self, nums: List[int]) -> int:
    # points = defaultdict(int)
    # max_number = 0

    # for num in nums:
    #     points[num] += num
    #     max_number = max(max_number, num)

    # two_back = points[1]
    # one_back = 0

    # for num in range(2, max_number + 1):
    #     curr = max(one_back, two_back + points[num])
    #     one_back, two_back = curr, one_back

    # return one_back
    """
    Time optimized Bottom-up DP
    Time complexity: O( n log n)
    Space complexity: O(n)
    """

    def deleteAndEarn(self, nums: List[int]) -> int:
        points = defaultdict(int)
        for num in nums:
            points[num] += num

        elements = sorted(points.keys())
        two_back = 0
        one_back = points[elements[0]]
        for i in range(1, len(elements)):
            current_element = elements[i]
            if current_element == elements[i-1] + 1:
                two_back, one_back = one_back, max(
                    one_back, two_back + points[current_element])
            else:
                two_back, one_back = one_back, one_back + \
                    points[current_element]
        return one_back

    """
    Bottom up DP
    Time complexity: O(n)
    Space complexity: O(n)
    dp(i) = max(dp(i-2) + i, dp(i-1)) -> max points when choosing value i
    """
#     def deleteAndEarn(self, nums: List[int]) -> int:
#         # from collections import Counter
#         # preprocess
#         count = Counter(nums)
#         max_num = max(nums)
#         min_num = min(nums)
#         dp = [0] * (max_num+ 1)
#         if min_num == 1:
#             dp[1] = count[1]
#             min_num = 2
#         # dp through min ~ max values of nums
#         for i in range(min_num, max_num + 1):
#             # if i not in keys, use previous value
#             if i not in count:
#                 dp[i] = dp[i-1]

#             # with k
#             with_i = i * count[i] + dp[i-2]
#             # without k
#             without_i = dp[i-1]

#             dp[i] = max(with_i, without_i)

#        return dp[max_num]

# @lc code=end
