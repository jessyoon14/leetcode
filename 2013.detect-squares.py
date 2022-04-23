#
# @lc app=leetcode id=2013 lang=python3
#
# [2013] Detect Squares
#

# @lc code=start
class DetectSquares:

    def __init__(self):
        self.x_points = defaultdict(list)  # dict never raises keyerror
        self.point_count = defaultdict(int)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.x_points[x].append(y)
        self.point_count[(x, y)] += 1

    def count(self, point: List[int]) -> int:
        ans = 0
        x1, y1 = point

        for y2 in self.x_points[x1]:
            if y2 == y1:
                continue
            width = abs(y2 - y1)

            x3, y3 = x1 - width, y2
            x4, y4 = x1 - width, y1
            ans += self.point_count[(x3, y3)] * self.point_count[(x4, y4)]

            x3, y3 = x1 + width, y2
            x4, y4 = x1 + width, y1
            ans += self.point_count[(x3, y3)] * self.point_count[(x4, y4)]

        return ans


# class DetectSquares:

#     def __init__(self):
#         self.point_count = Counter()

#     def add(self, point: List[int]) -> None:
#         self.point_count[tuple(point)] += 1

#     def count(self, point: List[int]) -> int:
#         ans = 0
#         x1, y1 = point
#         for (x3, y3), cnt in self.point_count.items():
#             if abs(x1-x3) == 0 or abs(x1 - x3) != abs(y1 - y3):
#                 continue
#             ans += cnt * self.point_count[(x1, y3)] * self.point_count[(x3, y1)]
#         return ans


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)

# class DetectSquares:

#     def __init__(self):
#         self.xs = {}
#         self.point_counts = {}


#     def add(self, point: List[int]) -> None:
#         point_tup = (point[0], point[1])
#         self.point_counts[point_tup] = self.point_counts.get(point_tup, 0) + 1

#         x_list = self.xs.get(point[0])
#         if x_list is None:
#             self.xs[point[0]] = [point[1]]
#         else:
#             x_list.append(point[1])

#     def count(self, point: List[int]) -> int:
#         def get_point_count(point: tuple[int, int]) -> int:
#             return self.point_counts.get(point, 0)

#         x = point[0]
#         y = point[1]

#         y_candidates = self.xs.get(x, [])

#         square_count = 0

#         for y_candidate in y_candidates:
#             # find height
#             height = abs(y - y_candidate)
#             if height == 0:
#                 continue

#             # find x_aligned point (2 candidates)
#             point = (x - height, y)
#             # find point x - height, y
#             if get_point_count(point) > 0:
#                 diagonal_point = (x - height, y_candidate)
#                 # find diagonal: x - height, y_candidate
#                 if get_point_count(diagonal_point) > 0:
#                     square_count += get_point_count(point) * get_point_count(diagonal_point)

#             # find point x + height, y
#             point = (x + height, y)
#             # find point x - height, y
#             if get_point_count(point) > 0:
#                 diagonal_point = (x + height, y_candidate)
#                 # find diagonal: x + height, y_candidate
#                 if get_point_count(diagonal_point) > 0:
#                     square_count += get_point_count(point) * get_point_count(diagonal_point)

#         return square_count


# # Your DetectSquares object will be instantiated and called as such:
# # obj = DetectSquares()
# # obj.add(point)
# # param_2 = obj.count(point)


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
# @lc code=end
