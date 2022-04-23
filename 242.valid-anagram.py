#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = list(s)
        t_list = list(t)
        s_list.sort()
        t_list.sort()

        return s_list == t_list

    # one pass char count array

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_count = [0] * 26

        for i in range(len(s)):
            s_char_idx = ord(s[i]) - ord('a')
            t_char_idx = ord(t[i]) - ord('a')
            char_count[s_char_idx] += 1
            char_count[t_char_idx] -= 1

        for i in range(26):
            if char_count[i] != 0:
                return False
        return True

    # char count array
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False

#         char_count = collections.Counter(s)

#         for c in t:
#             count = char_count.get(c)
#             if count == None or count <= 0:
#                 return False
#             else:
#                 char_count[c] = count - 1

#         return True
# @lc code=end
