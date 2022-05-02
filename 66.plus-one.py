#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    #     def plusOne(self, digits: List[int]) -> List[int]:
    #         carry = 0
    #         digits[-1] = digits[-1] + 1
    #         for i in range(len(digits) - 1, -1, -1):
    #             new_digit = digits[i] + carry
    #             digits[i] = new_digit % 10
    #             carry = new_digit // 10
    #         if carry:
    #             digits.insert(0, 1)
    #         return digits

    """
    Identify 9's
    """
    # def plusOne(self, digits: List[int]) -> List[int]:
    #     if digits[-1] == 9:
    #         i = len(digits) - 1
    #         while i > -1 and digits[i] == 9:
    #             digits[i] = 0
    #             i -= 1
    #         if i >= 0:
    #             digits[i] += 1
    #         else:
    #             digits.insert(0, 1)
    #     else:
    #         digits[-1] = digits[-1] + 1
    #     return digits

    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)

        for i in range(n-1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        return [1] + digits

# @lc code=end
