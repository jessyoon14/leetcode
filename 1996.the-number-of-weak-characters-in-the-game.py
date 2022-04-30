#
# @lc app=leetcode id=1996 lang=python3
#
# [1996] The Number of Weak Characters in the Game
#

# @lc code=start
class Solution:
    """
    Could not solve. Must redo!
    """

    """
    O(n)
    """

    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        max_defense = [0] * 100002
        res = 0
        for p in properties:
            max_defense[p[0]] = max(max_d[p[0]], p[1])

        for i in range(100000, 0, -1):
            max_defense[i-1] = max(max_defense[i-1], max_defense[i])

        for p in properties:
            if max_defense[p[0] + 1] > p[1]:
                res += 1
        return res

    """
    With stack
    """

    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (x[0], -x[1]))
        stack = []
        ans = 0

        for a, d in properties:
            # new element is stronger than the strongest so far
            while stack and stack[-1] < d:
                stack.pop()
                ans += 1
            stack.append(d)
        return ans

    """
    With 2d sort (inc & dec)
    """

    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (-x[0], x[1]))

        ans = 0
        curr_max = 0

        for _, d in properties:
            if d < curr_max:
                ans += 1
            else:
                curr_max = d
        return ans

#     def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
#         properties.sort(key=lambda x: (x[0], -x[1]))

#         max_defense = math.min()
#         ans = 0

#         for i in range(len(properties), -1, -1):
#             if properties[i][1] < max_defense:
#                 ans += 1
#             elif properties[i][1] > max_defense:
#                 max_defense = properties[i][1]

#         return weak_count


# @lc code=end
