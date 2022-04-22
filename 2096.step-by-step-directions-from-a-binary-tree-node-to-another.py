#
# @lc app=leetcode id=2096 lang=python3
#
# [2096] Step-By-Step Directions From a Binary Tree Node to Another
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def find(n: TreeNode, val: int, path: List[str]) -> bool:
            if n.val == val:
                return True
            elif n.left and find(n.left, val, path):
                path += 'L'
            elif n.right and find(n.right, val, path):
                path += 'R'
            return path

        start_path, dest_path = [], []
        find(root, startValue, start_path)
        find(root, destValue, dest_path)

        while start_path and dest_path and (start_path[-1] == dest_path[-1]):
            start_path.pop()
            dest_path.pop()

        return ''.join('U' * len(start_path)) + ''.join(reversed(dest_path))


#     def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
#         path = []

#         start_path = []
#         dest_path = []

#         def find_path_to(root):
#             nonlocal start_path, dest_path
#             if root is None:
#                 return None
#             elif root.val == startValue:
#                 start_path = path[:]
#             elif root.val == destValue:
#                 dest_path = path[:]

#             path.append('L')
#             left = find_path_to(root.left)
#             path.pop()
#             if start_path and dest_path:
#                 return
#             path.append('R')
#             right = find_path_to(root.right)
#             path.pop()
#             if start_path and dest_path:
#                 return

#         def flip_path(path):
#             for i in range(len(path)):
#                 if path[i] != 'U':
#                     path[i] = 'U'
#             path.reverse()

#         find_path_to(root)

#         while start_path and dest_path and (start_path[0] == dest_path[0]):
#             start_path.pop(0)
#             dest_path.pop(0)

#         flip_path(start_path)
#         complete_path = start_path + dest_path
#         return ''.join(complete_path)

#     def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
#         path = []

#         def find_path_to(root, target):
#             if root is None:
#                 return None
#             if root.val == target:
#                 return path[:]

#             path.append('L')
#             left = find_path_to(root.left, target)
#             path.pop()
#             if left:
#                 return left
#             path.append('R')
#             right = find_path_to(root.right, target)
#             path.pop()
#             if right:
#                 return right
#             return None

#         def flip_path(path):
#             for i in range(len(path)):
#                 if path[i] != 'U':
#                     path[i] = 'U'
#             path.reverse()

#         start_path = find_path_to(root, startValue)
#         dest_path = find_path_to(root, destValue)

#         if start_path is None or dest_path is None:
#             return ''

#         while start_path and dest_path and (start_path[0] == dest_path[0]):
#             start_path.pop(0)
#             dest_path.pop(0)

#         flip_path(start_path)
#         complete_path = start_path + dest_path
#         return ''.join(complete_path)
# @lc code=end
