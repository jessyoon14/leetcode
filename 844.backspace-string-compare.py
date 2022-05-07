#
# @lc app=leetcode id=844 lang=python3
#
# [844] Backspace String Compare
#

# @lc code=start
class Solution:
    """
    Stack
    Time complexity: O(m + n)
    Space complexity: O(m + n)
    """
#     def backspaceCompare(self, s: str, t: str) -> bool:
#         def process(a):
#             result = []
#             for i in range(len(a)):
#                 if a[i] != '#':
#                     result.append(a[i])
#                 elif result:
#                     result.pop()
#             return result

#         new_s = process(s)
#         new_t = process(t)

#         return new_s == new_t

    """
    Two Pointer
    Time complexity: O(N)
    Space complexity: O(1)
    """

    def backspaceCompare(self, s: str, t: str) -> bool:
        si, ti = len(s) - 1, len(t) - 1
        count_s = count_t = 0

        while si >= 0 or ti >= 0:
            while si >= 0:
                if s[si] == '#':
                    count_s += 1
                    si -= 1
                elif s[si] != '#' and count_s > 0:
                    count_s -= 1
                    si -= 1
                else:
                    break
            while ti >= 0:
                if t[ti] == '#':
                    count_t += 1
                    ti -= 1
                elif t[ti] != '#' and count_t > 0:
                    count_t -= 1
                    ti -= 1
                else:
                    break

            if (ti < 0 and si >= 0) or (si < 0 and ti >= 0):
                return False
            if (ti >= 0 and si >= 0) and s[si] != t[ti]:
                return False
            si -= 1
            ti -= 1
        return True

    # def backspaceCompare(self, s: str, t: str) -> bool:
    #     i, j = len(s), len(t)
    #     backs = backt = 0
    #     while True:
    #         while i >= 0 and (backs or s[i] == '#'):
    #             backs += 1 if s[i] == '#' else -1
    #             i -= 1
    #         while j >= 0 and (backt or t[j] == '#'):
    #             backt += 1 if t[j] == '#' else -1
    #             j -= 1
    #         if not (i>=0 and j>=0 and s[i] == t[j]):
    #             return i == j == -1
    #         i -= 1
    #         j -= 1

    """
    Two Pointer
    """
#     def backspaceCompare(self, s: str, t: str) -> bool:
#         def get_next_valid_idx(a, idx):
#             if a[idx] != '#':
#                 return idx
#             delete_count = 0
#             while idx > -1:
#                 if a[idx] == '#':
#                     delete_count += 1
#                 else:
#                     delete_count -= 1
#                 idx -= 1
#                 if delete_count < 1 and idx > -1 and a[idx] != '#':
#                     return idx
#             return idx

#         s_ptr = get_next_valid_idx(s, len(s) - 1)
#         t_ptr = get_next_valid_idx(t, len(t) - 1)

#         while s_ptr > -1 and t_ptr > -1:
#             if s[s_ptr] != t[t_ptr]:
#                 return False
#             s_ptr = get_next_valid_idx(s, s_ptr - 1)
#             t_ptr = get_next_valid_idx(t, t_ptr - 1)

#         return s_ptr < 0 and t_ptr < 0
# @lc code=end
