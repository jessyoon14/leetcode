#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
class Solution:
    """
    Brute force (DFS) -> generate all possible splits
    Time complexity: O(2^n) -> stars and bars! as many ways to slide many sliders into n + 1 slots
    Space complexity: O(n)    
    """

    # def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    #     words = set(wordDict)
    #     n = len(s)

    #     def rec(curr_word_start):
    #         if curr_word_start == n:
    #             return True
    #         for next_word_start in range(curr_word_start + 1, n + 1):
    #             if s[curr_word_start:next_word_start] in words and rec(next_word_start):
    #                 return True
    #         return False
    #     return rec(0)

    """
    BFS
    Time complexity: O(n^3) -> outer while: n^2, inner for: n
    Space complexity: O(n) -> max size of queue
    """

    # def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    #     word_set = set(wordDict)
    #     q = deque()
    #     visited = set()

    #     q.append(0)
    #     while q:
    #         start = q.popleft(0)
    #         if start in visited:
    #             continue
    #         for end in range(start + 1, len(s) + 1):
    #             if s[start:end] in word_set:
    #                 q.append(end)
    #                 if end == len(s):
    #                     return True
    #         visited.add(start)
    #     return False

    """
    Top-down DP
    Time complexity: O(m + n ^ 3), m: # words, n: len string
    Space complexity: O(n + size of wordDict)
    """

    # def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    #     words = set(wordDict)
    #     n = len(s)
    #     memo = [None] * n

    #     # @lru_cache(None)
    #     def dp(start):  # is s[i:] valid?
    #         if start == len(s):
    #             return True

    #         if memo[start] is not None:
    #             return memo[start]

    #         is_valid = False
    #         for next_word_start in range(start + 1, n + 1):
    #             first_word = s[start:next_word_start]  # str copy takes n time
    #             if first_word in words and dp(next_word_start):
    #                 is_valid = True
    #                 break

    #         memo[start] = is_valid
    #         return is_valid
    #     return dp(0)

    """
    Bottom-up DP
    Time complexity: n ^ 3
    Space complexity: n
    """

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[n] = True

        for start in range(n - 1, -1, -1):
            for next_word_start in range(start + 1, n + 1):
                first_word = s[start:next_word_start]
                if first_word in words and dp[next_word_start]:
                    dp[start] = True
                    break

        return dp[0]

# @lc code=end
