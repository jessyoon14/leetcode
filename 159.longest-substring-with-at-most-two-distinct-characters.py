class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        curr_chars = {}  # char and last index of this char

        l = 0
        max_len = 0
        for r in range(len(s)):
            curr_chars[s[r]] = r
            if len(curr_chars) < 3:
                # update max
                max_len = max(max_len, r - l + 1)
            else:
                # update left until curr_chars is 2 or less
                del_idx = min(curr_chars.values())
                del curr_chars[s[del_idx]]
                l = del_idx + 1
        return max_len
