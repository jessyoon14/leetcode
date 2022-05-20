#
# @lc app=leetcode id=2007 lang=python3
#
# [2007] Find Original Array From Doubled Array
#

# @lc code=start
class Solution:
    #     """
    #     Sort + dict
    #     time: n log n
    #     space: n
    #     """
    #     def findOriginalArray(self, changed: List[int]) -> List[int]:
    #         list.sort(changed)

    #         seen = defaultdict(int)
    #         result = []
    #         for i in changed:
    #             if seen[i/2] > 0:
    #                 result.append(i//2)
    #                 seen[i/2] -= 1
    #             else:
    #                 seen[i] += 1
    #         return result if len(result) == len(changed) / 2 else []

    """
    Sort + two pointer
    time: n log n
    space: n
    """
#     def findOriginalArray(self, changed: List[int]) -> List[int]:
#         if len(changed) < 2 or len(changed) % 2 > 0:
#             return []

#         list.sort(changed)
#         left = 0
#         result = []

#         for right in range(1, len(changed)):
#             if left == right:
#                 continue
#             elif changed[left] * 2 == changed[right]:
#                 changed[right] = -1
#                 result.append(changed[left])
#                 left += 1
#                 while left < len(changed) and changed[left] < 0:
#                     left += 1
#             elif changed[left] * 2 > changed[right]:
#                 continue
#             else:
#                 return []

#         return result if len(result) == len(changed) / 2 else []

    """
    Dict + sort
    time: O(N + k log k)
    space: O(n)
    """
#     def findOriginalArray(self, changed: List[int]) -> List[int]:
#         c = collections.Counter(changed)
#         if c[0] % 2 > 0:
#             return []
#         for x in sorted(c):
#             if c[x] > c[2*x]:
#                 return []
#             c[2*x] -= c[x] if x else c[x] // 2

#         return list(c.elements())

    """
    Greedy
    """
    # def findOriginalArray(self, changed: List[int]) -> List[int]:
    #     cnt, ans = Counter(changed), []
    #     for num in sorted(changed, key = lambda x: abs(x)):
    #         if cnt[num] == 0:
    #             continue
    #         if cnt[2*num] == 0:
    #             return []
    #         if num == 0 and cnt[num] <= 1:
    #             return []
    #         ans += [num]
    #         cnt[num] -= 1
    #         cnt[2*num] -= 1
    #    return ans

    """
    Counter + sort
    """

    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 == 1:
            return []

        original = []
        numbers = collections.Counter(changed)

        for n in sorted(changed):
            v = n * 2
            if numbers.get(n, 0) > 0 and numbers.get(v, 0) > 0:
                original.append(n)
                numbers[n] -= 1
                numbers[v] -= 1
            elif n // 2 not in numbers or n % 2 == 1:
                return []
        return original

    """
    dict without sort
    time: O(N)???
    space: O(n)
    """
#     def findOriginalArray(self, changed: List[int]) -> List[int]:
#         counter = collections.Counter(changed)
#         res = []
#         for k in counter.keys():
#             if k == 0:
#                 if counter[k] % 2 > 0:
#                     return []
#                 res += [0] * (counter[k] // 2)

#             elif counter[k] > 0:
#                 x = k
#                 while x % 2 == 0 and x // 2 in counter:
#                     x = x // 2

#                 while x in counter:
#                     if counter[x] > 0:
#                         res += [x] * counter[x]:
#                         if counter[x+x] < counter[x]:
#                             return[]
#                         counter[x+x] -= counter[x]
#                         counter[x] = 0
#                     x += x
#         return res

    """
    Incorrect approch: Get intersection -> can't process chains & duplicate values
    time: O(n)
    space: O(n)
    edge case
    - empty
    - length 1
    - odd & even
    - one value both orig & double (ex: 1, 2, 2, 4)
    - duplicate numbers
    - chain (2, 4, 8)
    """


# @lc code=end
