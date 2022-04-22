#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    # iterative binary search
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # input validation
        h = len(matrix)
        w = len(matrix[0])
        if h == 0:
            return False

        def get_2d_idx(num):
            return num // w, num % w

        left = 0
        right = h*w - 1

        while left <= right:
            mid = (left + right) // 2
            i, j = get_2d_idx(mid)
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                right = mid - 1
            else:
                left = mid + 1

        return False

    # recursive binary search
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         # input validation
#         h = len(matrix)
#         w = len(matrix[0])
#         if h == 0:
#             return False

#         def get_2d_idx(num):
#             return num // w, num % w

#         def binary_search(left, right) -> bool:
#             if left > right:
#                 return False
#             mid = (left + right) // 2
#             i, j = get_2d_idx(mid)
#             if matrix[i][j] == target:
#                 return True
#             elif matrix[i][j] > target:
#                 return binary_search(left, mid-1)
#             else:
#                 return binary_search(mid + 1, right)

#         return binary_search(0, h*w-1)
# @lc code=end
