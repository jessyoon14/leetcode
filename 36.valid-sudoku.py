#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9

        rows = [0] * N
        cols = [0] * N
        boxes = [0] * N

        for r in range(N):
            for c in range(N):
                if board[r][c] == '.':
                    continue
                digit = int(board[r][c]) - 1
                digit_bitmask = 1 << digit

                if rows[r] & digit_bitmask:
                    return False
                elif cols[c] & digit_bitmask:
                    return False
                elif boxes[(r // 3) * 3 + c//3] & digit_bitmask:
                    return False

                # update
                rows[r] |= digit_bitmask
                cols[c] |= digit_bitmask
                boxes[(r // 3) * 3 + c//3] |= digit_bitmask

        return True


# @lc code=end
