#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]

        for i in range(1, numRows):
            curr_row = [1]
            for j in range(i-1):
                curr_row.append(result[-1][j] + result[-1][j+1])
            curr_row.append(1)
            result.append(curr_row)
        return result
# @lc code=end
