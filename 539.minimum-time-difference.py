#
# @lc app=leetcode id=539 lang=python3
#
# [539] Minimum Time Difference
#

# @lc code=start
class Solution:
    """
    Amazing Triangle solution
    Time: O(n)
    Space: O(1)

    """

#     def findMinDifference(self, timePoints: List[str]) -> int:

#         def parse(s):
#             return int(s[:2]) * 60 + int(s[3:])

#         time_set = set(timePoints)
#         if len(time_set) != len(timePoints):
#             return 0

#         MINUTES = 24 * 60
#         times = [False] * MINUTES

#         for time in timePoints:
#             times[parse(time)] = True

#         # find minimum distance between two Trues
#         last_true_idx = float('-inf')
#         min_distance = float('inf')

#         for i in range(MINUTES * 2):
#             if times[i % MINUTES]:
#                 curr_distance = i - last_true_idx
#                 min_distance = min(min_distance, curr_distance)
#                 last_true_idx = i
#                 if i > MINUTES - 1:
#                     break
#         return min_distance

    """
    Sort
    !!! Don't forget to update prev
    Time: O(n log n)
    Space: O(n)
    
    """

    def findMinDifference(self, timePoints: List[str]) -> int:
        def parse(s):
            return int(s[:2]) * 60 + int(s[3:])

        time_set = set(timePoints)

        if len(time_set) != len(timePoints):
            # exists duplicates
            return 0

        list.sort(timePoints)

        min_time_diff = float('inf')
        prev = parse(timePoints[-1])

        for i in range(len(timePoints)):
            curr = parse(timePoints[i])
            min_time_diff = min((curr - prev) % (24 * 60), min_time_diff)
            prev = curr

        return min_time_diff

        # check last element ~ first element

# @lc code=end
