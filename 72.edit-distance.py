#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = []
        for i in range(len(word1) + 1):  # w1 x w2
            dp.append([0 for i in range(len(word2) + 1)])

        for i in range(len(word1) + 1):
            for j in range(len(word2) + 1):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                elif word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        return dp[len(word1)][len(word2)]

# @lc code=end
