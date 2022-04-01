#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start

# Solution 1: Brute force
# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         def calculateChange(coin_idx: int, curr_amount: int) -> int:
#             if curr_amount == 0:
#                 return 0
#             if coin_idx < len(coins) and amount > 0:
#                 max_count = curr_amount // coins[coin_idx]
#                 min_count = curr_amount + 1
#                 for i in range(max_count + 1):
#                     res = calculateChange(
#                         coin_idx + 1, curr_amount - coins[coin_idx] * i)
#                     if res > -1:
#                         min_count = min(min_count, res + i)
#                 result = min_count if min_count < curr_amount + 1 else -1
#                 return result
#             else:
#                 return -1

#         return calculateChange(0, amount)

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


# @lc code=end
