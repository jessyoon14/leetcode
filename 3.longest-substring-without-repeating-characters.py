#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    """
    Edge case:
    - empty list
    - list length 1
    - list is repetition of one char
    - entire list is substring
    - target at head / tail
    - normal case
    """

    """
    Brute force: generate all possible substrings then check
    """
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         def is_unique(s):
#             return len(set(s)) == len(s)

#         max_len = 0
#         for i in range(len(s)):
#             for j in range(i+1, len(s)):
#                 if is_unique(s[i:j+1]):
#                     max_len = max(max_len, j + 1 -i)

#         return max_len

    """
    Sliding window with char list: O(2n) solution
    """
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         chars = [0] * 128
#         left = right = 0
#         res = 0
#         while right < len(s):
#             r = s[right]
#             chars[ord(r)] += 1
#             while chars[ord(r)] > 1:
#                 l = s[left]
#                 chars[ord(l)] -= 1
#                 left += 1
#             res = max(res, right - left + 1)
#             right += 1

#         return res

    """
    Optimized sliding window, O(n)
    """

    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = [None] * 128
        left = right = 0
        res = 0
        while right < len(s):
            r = s[right]
            index = chars[ord(r)]
            if index != None and index >= left:
                left = index + 1
            res = max(res, right - left + 1)
            chars[ord(r)] = right
            right += 1
        return res

    """
    My solution: use sliding window
    """
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         if not s:
#             return 0
#         max_len = 0
#         left = 0
#         chars = {}
#         for right in range(len(s)):
#             if s[right] in chars and chars[s[right]] >= left:
#                 # update left
#                 left = chars[s[right]] + 1
#             else:
#                 # update max_len
#                 max_len = max(max_len, right - left + 1)
#             # update chars
#             chars[s[right]] = right

#         return max_len


# @lc code=end
