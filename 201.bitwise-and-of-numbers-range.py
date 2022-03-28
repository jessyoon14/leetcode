#
# @lc app=leetcode id=201 lang=python3
#
# [201] Bitwise AND of Numbers Range
#

# @lc code=start
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if not left or not right:
            return 0
        elif left == right:
            return left

        len1 = math.floor(math.log2(left))
        len2 = math.floor(math.log2(right))

        if len1 != len2:
            return 0

        index_of_different_msb = math.floor(math.log2(left ^ right))
        return left & (-1 << (index_of_different_msb + 1))


# @lc code=end
