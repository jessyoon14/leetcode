#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#

# @lc code=start
class Solution:

    # constant-space bottom-up dp
    def fib(self, n: int) -> int:
        if n < 2:
            return n

        prev1 = 0
        prev2 = 1

        for i in range(2, n + 1):
            curr = prev1 + prev2
            prev1 = prev2
            prev2 = curr

        return prev2

#     # bottom-up dp
#     def fib(self, n: int) -> int:
#         if n < 2:
#             return n
#         dp = [0] * (n + 1)
#         dp[1] = 1
#         for i in range(2, n + 1):
#             dp[i] = dp[-2] + dp[-1]

#         return dp[-1]

    # basic memoization (top-down dp)
#     mem = {0: 0, 1: 1}

#     def fib(self, n: int) -> int:
#         if n in self.mem:
#             return self.mem[n]

#         self.mem[n] = self.fib(n-1) + self.fib(n-2)
#         return self.mem[n]

    # basic recursion with decorator
#     @lru_cache(None) # or @cache
#     def fib(self, n: int) -> int:
#         if n < 2:
#             return n

#         return self.fib(n-1) + self.fib(n-2)

    # basic recursion
#     def fib(self, n: int) -> int:
#         if n < 2:
#             return n

#         return self.fib(n-1) + self.fib(n-2)
# @lc code=end
