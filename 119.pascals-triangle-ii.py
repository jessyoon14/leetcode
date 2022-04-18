#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#

# @lc code=start
class Solution:
    # combinatorics
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for r in range(1, rowIndex + 1):
            next_el = row[-1] * ((rowIndex - r + 1) / r)
            row.append(round(next_el))
        return row

#     # memory efficient dp
#     def getRow(self, rowIndex: int) -> List[int]:
#         row = [0 for i in range (rowIndex+1)]
#         row[0] = 1

#         for i in range(1, rowIndex + 1):
#             # i = 2 -> j = 1 only
#             # row[i] = 1
#             for j in range(i, 0, -1):
#                 row[j] = row[j] + row[j-1]

#         return row

    # recursion with memoization
#     def getRow(self, rowIndex: int) -> List[int]:

#         dp = [[0] * (i+1) for i in range(rowIndex + 1)]

#         def getEl(i, j):
#             if i == 0 or j == 0 or j == i:
#                 return 1
#             if dp[i][j]:
#                 return dp[i][j]
#             dp[i][j] = getEl(i-1, j-1) + getEl(i-1, j)
#             return dp[i][j]

#         result = []
#         for i in range(rowIndex + 1):
#             result.append(getEl(rowIndex, i))
#         return result

#     # basic recursion
#     def getRow(self, rowIndex: int) -> List[int]:
#         def getEl(i, j):
#             if i == 0 or j == 0 or i == j:
#                 return 1
#             return getEl(i-1, j-1) + getEl(i-1, j)

#         result = []
#         for i in range(rowIndex + 1):
#             result.append(getEl(rowIndex, i))
#         return result

    # bottom-up DP
#     def getRow(self, rowIndex: int) -> List[int]:

#         prev_row = [1]

#         for i in range(1, rowIndex + 1):
#             current_row = [1]
#             for j in range(i - 1):
#                 current_row.append(prev_row[j] + prev_row[j+1])
#             current_row.append(1)
#             prev_row = current_row

#         return prev_row

#     # my solution (Top-down dp)
#     def getRow(self, rowIndex: int) -> List[int]:
#         if rowIndex == 0:
#             return [1]
#         if rowIndex == 1:
#             return [1, 1]

#         prev_row = self.getRow(rowIndex - 1)

#         new_row = [1]
#         for i in range(len(prev_row) - 1):
#             new_row.append(prev_row[i] + prev_row[i+1])
#         new_row.append(1)

#         return new_row
# @lc code=end
