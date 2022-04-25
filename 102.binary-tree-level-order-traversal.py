#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
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
    # recursive solution
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []

        if root is None:
            return root

        def rec(root, level):
            if len(levels) - 1 < level:
                levels.append([])

            levels[level].append(root.val)
            if root.left:
                rec(root.left, level + 1)
            if root.right:
                rec(root.right, level + 1)

        rec(root, 0)
        return levels

    # iterative solution
#     def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         if root is None:
#             return root

#         next_level = deque([root])
#         result = []

#         while next_level:
#             count = len(next_level)
#             curr_level = []
#             for i in range(count):
#                 curr_node = next_level.popleft()
#                 curr_level.append(curr_node.val)
#                 if curr_node.left:
#                     next_level.append(curr_node.left)
#                 if curr_node.right:
#                     next_level.append(curr_node.right)
#             result.append(curr_level)

#         return result


# @lc code=end
