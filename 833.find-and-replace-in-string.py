#
# @lc app=leetcode id=833 lang=python3
#
# [833] Find And Replace in String
#

# @lc code=start
"""
1) check which replacements should happen
2) create new list and append the replacements

method 2:
preprocess replacements
sort by indices -> space / time: O(k)
1) iterate through s from left to right -> O(n)
    2) check if valid replacement at that index 
    3) if so, build result
    4) update current index to be after substring
    
time: O(n + k + k * max length of replacement string)
space: O(k * max length of replacement string + n)



"""


class Solution:
    """
    Process right to left (prevent index change)
    Time: 
    Space: 
    """

    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        for i, src, t in sorted(zip(indices, sources, targets), reverse=True):
            s = s[:i] + t + s[i + len(src):] if s[i:i + len(src)] == src else s
        return s

    """
    build string from left to right
    Time: O(n*y + k * x), n: # s. k: # replacements. x: max source length, y: max dest length 
    Space: O(max(len s, len result))
    """

    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        modified = list(s)
        for index, source, target in zip(indices, sources, targets):
            if not s[index:].startswith(source):
                continue
            else:
                modified[index] = target
                for i in range(index + 1, len(source) + index):
                    modified[i] = ''
        return ''.join(modified)

    """
    Build string linearly
    Time: O(n + k*n + k log k)
    Space: O(k + n)
    """
#     def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:

#         def has_replacement(i, j):
#             if j >= k:
#                 return '', '', j

#             while j < k and replacements[j][0] < i:
#                  j += 1

#             while j < k and replacements[j][0] == i:
#                 source, target = replacements[j][1]
#                 if s[i:i+len(source)] == source:
#                     return source, target, j + 1
#                 j += 1

#             return '', '', j

#         # preproecess replacements
#         replacements = list(zip(indices, zip(sources, targets))) # list of tup(int, tup(str, str))
#         list.sort(replacements)
#         # iterate through s
#         i, j = 0, 0
#         n, k = len(s), len(replacements)
#         result = []

#         while i < n:
#             # check if there is replacement starting at i
#             source, target, next_j = has_replacement(i, j)
#             j = next_j
#             if source:  # if replacement, build string with replacement and update i
#                 result.append(target)
#                 i += len(source)

#             else:       # if no replacement, build string and increment i
#                 result.append(s[i])
#                 i += 1

#         return ''.join(result)
# @lc code=end
