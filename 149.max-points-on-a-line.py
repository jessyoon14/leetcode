#
# @lc app=leetcode id=149 lang=python3
#
# [149] Max Points on a Line
#

# @lc code=start
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) < 2:
            return len(points)

        max_count = 0

        for i in range(len(points) - 1):
            point_count = dict()
            for j in range(i + 1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]

                if (x1 == x2 and y1 == y2):
                    continue
                if x1 == x2:
                    slope = float(inf)
                else:
                    slope = (y2 - y1) / (x2-x1)
                point_count[slope] = point_count.get(slope, 0) + 1
            max_count = max(max_count, max(point_count.values()) + 1)

        return max_count

# @lc code=end
