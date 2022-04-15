#
# @lc app=leetcode id=350 lang=python3
#
# [350] Intersection of Two Arrays II
#

# @lc code=start
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        count = {}

        for n in nums1:
            count[n] = count.get(n, 0) + 1

        for n in nums2:
            if n in count and count[n] > 0:
                result.append(n)
                count[n] -= 1

        return result


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        nums1.sort()
        nums2.sort()

        idx1, idx2 = 0, 0

        while idx1 < len(nums1) and idx2 < len(nums2):
            n1 = nums1[idx1]
            n2 = nums2[idx2]

            if n1 == n2:
                result.append(n1)
                idx1 += 1
                idx2 += 1
            elif n1 < n2:
                idx1 += 1
            else:
                idx2 += 1

        return result


# @lc code=end
