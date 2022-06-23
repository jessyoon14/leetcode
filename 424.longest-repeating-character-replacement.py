#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
class Solution:
    '''
    AABABBA
    A2 B1 A1 B2 A1

    2 -1 1 -2 1
    2 

    AABABBA
    AAAAA
       AAAA
    '''
#     def characterReplacement(self, s: str, k: int) -> int:
#         if len(s) == 0:
#             return 0
#         max_length = 0
#         for i in range(26):
#             c = chr(ord('A') + i)

#             left = 0
#             c_count = 0
#             for right in range(len(s)):
#                 next_c = s[right]
#                 # if curr left, right OK, update length
#                 if next_c == c:
#                     c_count += 1
#                 else:
#                     while left <= right and right - left + 1 - c_count > k:
#                         c_count -= 1 if s[left] == c else 0
#                         left += 1
#                 max_length = max(max_length, right - left + 1)

#         return max_length

    def characterReplacement(self, s: str, k: int) -> int:
        counts = [0] * 26
        start = 0
        maxCharCount = 0
        n = len(s)
        result = 0
        for end in range(n):
            c_idx = ord(s[end]) - ord('A')
            counts[c_idx] += 1
            maxCharCount = max(maxCharCount, counts[c_idx])

            while (end - start + 1 - maxCharCount > k):
                counts[ord(s[start]) - ord('A')] -= 1
                start += 1
                maxCharCount = max(counts)

            result = max(result, end - start + 1)

        return result
# @lc code=end
