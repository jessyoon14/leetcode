#
# @lc app=leetcode id=566 lang=python3
#
# [566] Reshape the Matrix
#

# @lc code=start
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        # check if parameters legal
        if len(mat) * len(mat[0]) != r * c:
            return mat

        result = [[0] * c for j in range(r)]
        n = len(mat[0])
        for i in range(r):
            for j in range(c):
                prev_i = (i*c + j) // n
                prev_j = (i*c + j) % n
                result[i][j] = mat[prev_i][prev_j]

        return result
# @lc code=end
