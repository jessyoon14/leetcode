#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#

# @lc code=start
class Solution:

    def rotate(self, matrix: List[List[int]]) -> None:
        self.transpose(matrix)
        self.reflect(matrix)

    def transpose(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    def reflect(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(n//2):
                matrix[i][j], matrix[i][n-1-j] = matrix[i][n-1-j], matrix[i][j]

    """
    Switch four elements at a time
    """
#     def rotate(self, matrix: List[List[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         n = len(matrix)
#         for i in range(n//2):
#             for j in range(i, n - 1 - i):
#                 matrix[i][j], matrix[j][n-1-i], matrix[n-1-i][n-1-j], matrix[n-j-1][i] =  matrix[n-j-1][i], matrix[i][j], matrix[j][n-1-i], matrix[n-1-i][n-1-j]

# @lc code=end
