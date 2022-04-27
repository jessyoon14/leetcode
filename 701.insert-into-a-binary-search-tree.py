#
# @lc app=leetcode id=701 lang=python3
#
# [701] Insert into a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # iteration
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = root
        while node:
            if val < node.val:
                if not node.left:
                    node.left = TreeNode(val)
                    return root
                else:
                    node = node.left

            else:
                if not node.right:
                    node.right = TreeNode(val)
                    return root
                else:
                    node = node.right
        return TreeNode(val)


#     # iteration
#     def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
#         new_node = TreeNode(val)

#         if not root:
#             return new_node

#         parent = root
#         while True:
#             if parent.val > val:
#                 if parent.left:
#                     parent = parent.left
#                 else:
#                     parent.left = new_node
#                     return root
#             else:
#                 if parent.right:
#                     parent = parent.right
#                 else:
#                     parent.right = new_node
#                     return root


#     # recursion
#     def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
#         if not root:
#             return TreeNode(val)

#         # check if leaf
#         if val < root.val:
#             root.left = self.insertIntoBST(root.left, val)

#         else:
#             root.right = self.insertIntoBST(root.right, val)

#         return root

# @lc code=end
