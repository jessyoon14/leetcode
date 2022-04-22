#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = collections.Counter(s)

        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx
        return -1


#     def firstUniqChar(self, s: str) -> int:
#         # initialize array of size 26 to len+1
#         n = len(s)

#         unseen = n + 1
#         seen = n + 2
#         chars = [unseen] * 26


#         # traverse string. For each char, if unseen(len+10), set to idx. if seen, set to len + 2
#         for i in range(n):
#             c_idx = ord(s[i]) - ord('a')
#             if chars[c_idx] == unseen:
#                 chars[c_idx] = i
#             else:
#                 chars[c_idx] = seen

#         # return min idx of array. if greater than len - 1, return -1
#         result = min(chars)
#         return result if result < n else -1


# @lc code=end
