#
# @lc app=leetcode id=343 lang=python3
#
# [343] Integer Break
#

# @lc code=start
class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n-1

        div = n // 3
        mod = n % 3

        if mod == 0:
            return int(3**div)
        elif mod == 1:
            return int(3**(div-1)) * 4

        return int(3**div) * 2
# @lc code=end
