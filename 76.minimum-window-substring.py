#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
class Solution:

    """
    Sliding window solution with dict
    Time complexity: O(n + m)
    Space complexity: O(1), (bound by number of unique characters)
    """

    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ''
        dict_t = Counter(t)
        required = len(dict_t)
        l, r = 0, 0
        formed = 0
        window_counts = {}
        ans = (float('inf'), None, None)
        while r < len(s):
            # add one char
            character = s[r]
            window_counts[character] = window_counts.get(character, 0) + 1
            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1

            while l <= r and formed == required:
                character = s[l]
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)
                window_counts[character] -= 1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1
                l += 1
            r += 1
        return '' if ans[0] == float('inf') else s[ans[1]:ans[2]+1]

    """
    Optimized sliding window, when n >> m
    Remove characters from n that are not in m
    """
    def char_to_idx(c):
        dict_t = Counter(t)
        required = len(dict_t)

        filtered_s = []
        for i, char in enumerate(s):
            if char in dict_t:
                filtered_s.append((i, char))

        l, r = 0, 0
        formed = 0
        window_counts = {}

        ans = (float('inf'), None, None)

        while r < len(filtered_s):
            character = filtered_s[r][1]
            window_counts[character] = window_counts.get(character, 0) + 1
            if window_counts[character] == dict_t[character]:
                formed += 1
            while l <= r and formed == required:
                character = filtered_s[l][1]

                end = filtered_s[r][0]
                start = filtered_s[l][0]
                if end-start+1 < ans[0]:
                    ans = (end-start+1, start, end)
                window_counts[character] -= 1
                if window_counts[character] < dict_t[character]:
                    formed -= 1
                l += 1
            r += 1
        return '' if ans[0] == float('inf') else s[ans[1]: ans[2] + 1]

    """
    Sliding window solution with char array[52]
    """
#     def char_to_idx(c):
#         if c >= 'A' and c <= 'Z':
#             return ord(c) - ord('A')
#         else:
#             return 26 + ord(c) - ord('a')

#     def all_chars_found(chars):
#         for i in chars:
#             if i > 0:
#                 return False
#         return True

#     def minWindow(self, s: str, t: str) -> str:
#         n, m = len(s), len(t)
#         best_l, best_r = 0, n
#         chars = [0] * 52
#         for i in range(m):
#             chars[self.char_to_idx(t[i])] += 1
#         l = 0
#         for r in range(n):
#             chars[self.char_to_idx(s[r])] -= 1
#             while self.all_chars_found(chars):
#                 if (r-l+1) <= (best_r - best_l + 1):
#                     best_r = r
#                     best_l = l
#                 chars[self.char_to_idx(s[l])] += 1
#                 l += 1

#         return s[best_l:best_r + 1] if best_r < n else ''

# @lc code=end
