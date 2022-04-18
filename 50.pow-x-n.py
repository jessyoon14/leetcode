#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    # iterative solution (TLE)
    #     def myPow(self, x: float, n: int) -> float:
    #         if n < 0:
    #             x = 1/x
    #             n = -n

    #         result = 1
    #         for i in range(n):
    #             result *= x
    #         return result

    # fast iterative solution
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1/x
            n = -n

        result = 1
        curr_product = x
        power = n
        while power > 0:
            if power % 2 > 0:
                result *= curr_product
            curr_product = curr_product * curr_product
            power //= 2
        return result

    # fast recursion
    # def myPow(self, x: float, n: int) -> float:
    #     def rec(x, n):
    #         if n == 0:
    #             return 1
    #         sqrt = rec(x, n // 2)
    #         if n % 2 > 0:
    #             return sqrt * sqrt * x
    #         else:
    #             return sqrt * sqrt
    #     if n >= 0:
    #         return rec(x, n)
    #     else:
    #         return 1 / rec(x, -n)

#     def myPow(self, x: float, n: int) -> float:
#         def rec(x, n, acc):
#             if n == 0:
#                 return acc
#             return rec(x, n-1, acc * x)

#         if n >= 0:
#             return rec(x, n, 1)
#         else:
#             return 1 / rec(x, -n, 1)
# @lc code=end
