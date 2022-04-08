#
# @lc app=leetcode id=552 lang=python3
#
# [552] Student Attendance Record II
#

# @lc code=start
class Solution:
    def checkRecord(self, n: int) -> int:
        if n == 1:
            return 3

        # initialize counts for n = 2
        # 0, 1, 2: A = 0, end with 1 L, end with 2 Ls, end with P
        # 3, 4, 5, 6: A = 1, end with one L, 2 Ls, P, A
        counts = [1, 1, 2, 1, 0, 1, 2]
        next_counts = [0 for i in range(7)]
        mod = (10**9) + 7

        for i in range(3, n + 1):
            next_counts[0] = counts[2]  # 2
            next_counts[1] = counts[0]  # 1
            next_counts[2] = (counts[0] + counts[1] + counts[2]) % mod  # 4

            next_counts[3] = (counts[5] + counts[6]) % mod  # 3
            next_counts[4] = counts[3]  # 1
            next_counts[5] = (counts[3] + counts[4] +
                              counts[5] + counts[6]) % mod  # 4
            next_counts[6] = (counts[0] + counts[1] + counts[2]) % mod  # 4

            temp = counts
            counts = next_counts
            next_counts = temp

        return sum(counts) % mod

# @lc code=end
