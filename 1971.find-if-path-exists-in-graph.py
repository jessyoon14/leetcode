#
# @lc app=leetcode id=1971 lang=python3
#
# [1971] Find if Path Exists in Graph
#

# @lc code=start
# class Solution:
#     """
#     recursive DFS
#     time: O(e + v)
#     space: O(e + v)
#     """
#     def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
#         # recursive function
#         def has_path_to_dest(node):
#             # if source visited, return False
#             if node == destination:
#                 return True
#             if node in visited:
#                 return False
#             # iterate through neighbors of source
#             visited.add(node)
#             for neighbor in adj_list[node]:
#                 if has_path_to_dest(neighbor):
#                     return True
#             return False

#         # adj_list
#         adj_list = [[] for _ in range(n)]
#         for u, v in edges:
#             adj_list[u].append(v)
#             adj_list[v].append(u)

#         # visited set
#         visited = set()

#         return has_path_to_dest(source)


"""
Iterative DFS
"""


class Solution:
    """
    recursive DFS
    time: O(e + v)
    space: O(e + v)
    """

    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # recursive function
        def has_path_to_dest(node):
            # if source visited, return False
            if node == destination:
                return True
            if node in visited:
                return False
            # iterate through neighbors of source
            visited.add(node)
            for neighbor in adj_list[node]:
                if has_path_to_dest(neighbor):
                    return True
            return False

        # adj_list
        adj_list = [[] for _ in range(n)]
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        # visited set
        visited = set()

        return has_path_to_dest(source)
# @lc code=end
