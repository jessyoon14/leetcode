#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start

# Solution 1: Brute force
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def calculateChange(coin_idx: int, curr_amount: int) -> int:
            if curr_amount == 0:
                return 0
            if coin_idx < len(coins) and amount > 0:
                max_count = curr_amount // coins[coin_idx]
                min_count = curr_amount + 1
                for i in range(max_count + 1):
                    res = calculateChange(
                        coin_idx + 1, curr_amount - coins[coin_idx] * i)
                    if res > -1:
                        min_count = min(min_count, res + i)
                result = min_count if min_count < curr_amount + 1 else -1
                return result
            else:
                return -1

        return calculateChange(0, amount)

# Solution: bottom-up dynamic programming


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x-coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1

# first attempt
# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         dp = [amount + 1 for i in range(amount + 1)]
#         dp[0] = 0

#         for i in range(1, amount + 1):
#             for j in range(len(coins)):
#                 if i == coins[j]:
#                     dp[i] = 1
#                 elif i-coins[j] < 0 or dp[i-coins[j]] == -1:
#                     continue
#                 else:
#                     dp[i] = min(dp[i-coins[j]] + 1, dp[i])

#             if dp[i] > amount:
#                 dp[i] = -1

#         return dp[-1]


class Solution:
    """
    Brute force
    Time complexity: amount ^ # coins
    Space complexity: # coins
    """
#     def coinChange(self, coins: List[int], amount: int) -> int:

#         def rec(left, amount):
#             if amount == 0:
#                 return 0
#             elif amount < 0:
#                 return -1
#             elif left >= len(coins):
#                 return -1

#             min_count = amount + 1
#             coin = coins[left]
#             for i in range(amount // coin + 1):
#                 next_count = rec(left + 1, amount - coin * i)
#                 if next_count > -1:
#                     min_count = min(min_count, next_count + i)
#             return min_count if min_count <= amount else -1

#         return rec(0, amount)

    """ 
    Top down DP 1
    """

    def coinChange(self, coins: List[int], amount: int) -> int:
        mem = {}

        def rec(left, amount):
            if amount == 0:
                return 0
            elif amount < 0:
                return -1
            elif left >= len(coins):
                return -1

            if (left, amount) in mem:
                return mem[(left, amount)]

            min_count = amount + 1
            coin = coins[left]
            for i in range(amount // coin + 1):
                next_count = rec(left + 1, amount - coin * i)
                if next_count > -1:
                    min_count = min(min_count, next_count + i)
            mem[(left, amount)] = min_count if min_count <= amount else -1
            return mem[(left, amount)]
        return rec(0, amount)

    """
    Good top down dp solution
    """

    def coinChange(self, coins: List[int], amount: int) -> int:
        @lru_cache(None)
        def dp(i, amount):
            if amount == 0:
                return 0
            if i == -1:
                return math.inf

            ans = dp(i-1, amount)  # Skip ith coin
            if amount >= coins[i]:  # Used ith coin
                ans = min(ans, dp(i, amount - coins[i]) + 1)
            return ans

        n = len(coins)
        ans = dp(n-1, amount)
        return ans if ans != math.inf else -1

    """
    Top down DP
    f(amount) = min(f(amount-a1), f(amount-a2), ...) + 1
    Time complexity: O(N * amount)
    Space complexity: O(amount)
    """
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         mem = {}
#         def rec(amount):
#             if amount == 0:
#                 return 0
#             elif amount < 0:
#                 return -1

#             if amount in mem:
#                 return mem[amount]

#             min_change = amount + 1
#             for c in coins:
#                 if amount >= c:
#                     min_change = min(min_change, rec(amount - c) + 1)
#             mem[amount] = min_change if min_change <= amount else -1
#             return mem[amount]

#         return rec(amount)

    """
    Bottom up DP
    Time complexity: O(amount * # coins)
    Space complexity: O(amount)
    """
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         # f(i) = min(f(i-a1), f(i-a2), ...) + 1 where a1, a2 are the coin denominations
#         dp = [amount + 1] * (amount + 1)
#         dp[0] = 0

#         for i in range(1, amount + 1):
#             for c in coins:
#                 if i >= c:
#                     dp[i] = min(dp[i], dp[i-c] + 1)

#         return dp[amount] if dp[-1] <= amount else -1


# @lc code=end
