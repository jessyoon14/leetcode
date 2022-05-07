#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:

    """
    Longest Common Substring
    Get the longest common substring between s & s-reversed
    (Must check that indices are same!!!)
    Time complexity: O(n^2)
    Space complexity: O(n^2) -> can be improved to O(n)
    """

    def longestPalindrome(self, s: str) -> str:
        is s is '':
            return ''

        rev = s[::-1]
        n = len(s)
        dp[[0] * n for _ in range(n)]
        max_len = 0
        max_end = 0
        for i in range(n):
            for j in range(n):
                if s[i] == rev[j]:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i-1][j-1] + 1
                if dp[i][j] > max_len:
                    if i - dp[i][j] + 1 == len(s) - 1 - j:
                        max_len = dp[i][j]
                        max_end = i
        return s[max_end - max_len + 1:max_end + 1]

    """
    Longest Common Substring with 1D DP
    Time complexity: O(n^2)
    Space complexity: O(n^2)
    """

    def longestPalindrome(self, s: str) -> str:
        is s is '':
            return ''

        rev = s[::-1]
        n = len(s)
        dp = [0] * n
        max_len = 0
        max_end = 0
        for i in range(n):
            for j in range(n):
                if s[i] == rev[j]:
                    if i == 0 or j == 0:
                        dp[j] = 1
                    else:
                        dp[j] = dp[j-1] + 1
                else:
                    dp[j] = 0
                if dp[j] > max_len:
                    if i - dp[j] + 1 == len(s) - 1 - j:
                        max_len = dp[j]
                        max_end = i
        return s[max_end - max_len + 1:max_end + 1]

    """
    Brute force: pick all possible substrings and check if palindrome
    Time complexity: O(n^3)
    Space complexity: O(1)
    """

    def longestPalindrome(self, s: str) -> str:
        def is_palindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1

            return True

        if s is '':
            return ''
        n = len(s)
        max_pal_start = 0
        max_pal_length = 1
        for left in range(n):
            for right in range(left + 1, n):
                if is_palindrome(left, right) and right - left + 1 > max_pal_length:
                    max_pal_start = left
                    max_pal_length = right-left+1
        return s[max_pal_start:max_pal_start + max_pal_length]

    """
    Dynamic Programming (improving brute force)
    Time complexity: O(n^2)
    Space complexity: O(n^2)
    """

    def longestPalindrome(self, s: str) -> str:
        if s is '':
            return s
        res = ''
        n = len(s)
        dp = [[None] * n for _ in range(n)]

        for j in range(n):
            for i in range(j+1):
                if i == j:
                    dp[j][i] = True
                elif j == i + 1:
                    dp[j][i] = (s[i] == s[j])
                else:
                    dp[j][j] = dp[j-1][i+1] and s[i] == s[j]
                if dp[j][i] and j - i + 1 > len(res):
                    res = s[i: j+1]
        return res

    """
    Dynamic Programming (better space complexity)
    Time complexity: O(n^2)
    Space complexity: O(n)
    """

    def longestPalindrome(self, s: str) -> str:
        if s is '':
            return s
        res = ''
        n = len(s)
        dp = [None] * n

        for j in range(n):
            for i in range(j+1):
                if i == j:
                    dp[i] = True
                elif j == i + 1:
                    dp[i] = (s[i] == s[j])
                else:
                    dp[j] = dp[i+1] and s[i] == s[j]
                if dp[i] and j - i + 1 > len(res):
                    res = s[i: j+1]
        return res

    """
    Expand from center
    Time complexity: O(n^2)
    Space complexity: O(1)
    """

    def longestPalindrome(self, s: str) -> str:
        self.maxlen = 0
        self.start = 0

        for i in range(len(s)):
            self.expandFromCenter(s, i, i)
            self.expandFromCenter(s, i, i+1)
        return s[self.start:self.start + self.maxlen]

    def expandFromCenter(self, s, l, r):
        while l > -1 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        if self.maxlen < r-l-1:
            self.maxlen = r-l-1
            self.start = l+1

    """
    Brute force: Get all palindromes for each middle character
    Time complexity: n ^ 2
    Space complexity: 1
    """
#     def longestPalindrome(self, s: str) -> str:
#         def find_palindrome(i):
#             left = i - 1
#             right = i + 1
#             while left >= 0 and right < len(s) and s[left] == s[right]:
#                 left -= 1
#                 right += 1
#             left += 1
#             right -= 1

#             # if next char is same, repeat with right = i + 2
#             if i < len(s) - 1 and s[i] == s[i+1]:
#                 left2 = i - 1
#                 right2 = i + 2
#                 while left2 >= 0 and right2 < len(s) and s[left2] == s[right2]:
#                     left2 -= 1
#                     right2 += 1
#                 left2 += 1
#                 right2 -= 1

#                 if right2 - left2 > right - left:
#                     return s[left2: right2 + 1]

#             return s[left: right + 1]


#         max_p = ''
#         for i in range(len(s)):
#             # find palindrome
#             curr_p = find_palindrome(i)
#             if len(max_p) < len(curr_p):
#                 max_p = curr_p

#         return max_p

# @lc code=end
