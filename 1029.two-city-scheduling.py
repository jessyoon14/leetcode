#
# @lc app=leetcode id=1029 lang=python3
#
# [1029] Two City Scheduling
#

# @lc code=start
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: x[0] - x[1])
        total = 0
        n = len(costs) // 2

        for i in range(n):
            total += costs[i][0] + costs[i+n][1]
        return total

#     def twoCitySchedCost(self, costs: List[List[int]]) -> int:
#         def divide_group(pairs):
#             a = []
#             b = []
#             for pair in pairs:
#                 if pair[0] < pair[1]:
#                     a.append(pair)
#                 else:
#                     b.append(pair)
#             return a, b

#         # divide into groups
#         a, b = divide_group(costs)

#         # get total cost
#         total_cost = 0
#         for pair in a:
#             total_cost += pair[0]
#         for pair in b:
#             total_cost += pair[1]

#         # get bigger group
#         move_from_0_to_1 = True
#         if len(b) > len(a):
#             a, b = b, a
#             move_from_0_to_1 = False

#         num_moves = len(a) - len(costs)//2

#         # get moving cost
#         moving_cost = []
#         for costs in a:
#             if move_from_0_to_1:
#                 moving_cost.append(costs[1] - costs[0])
#             else:
#                 moving_cost.append(costs[0] - costs[1])

#         # sort moving cost
#         list.sort(moving_cost)

#         # update total cost
#         return total_cost + sum(moving_cost[:num_moves])


# @lc code=end
