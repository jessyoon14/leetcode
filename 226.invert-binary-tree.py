#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#

# @lc code=start

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # iterative
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        queue = deque([root])

        while queue:
            curr = queue.popleft()
            curr.left, curr.right = curr.right, curr.left
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        return root

    # recursive
#     def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
#         if root is None:
#             return root

#         new_left = self.invertTree(root.right)
#         new_right = self.invertTree(root.left)
#         root.right = new_right
#         root.left = new_left
#         return root

#     def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
#         if root is None:
#             return root

#         def rec(root):
#             if root is None:
#                 return
#             root.left, root.right = root.right, root.left
#             rec(root.left)
#             rec(root.right)

#         rec(root)
#         return root
# @lc code=end
