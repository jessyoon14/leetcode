#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # morris algorithm -> 이해안되니까 나중에 다시보기

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        stack, output = [root, ], []

        while stack:
            root = stack.pop()
            if root is not None:
                output.append(root.val)
                if root.right is not None:
                    stack.append(root.right)
                if root.left is not None:
                    stack.append(root.left)
        return output

    # iterative
#     def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         stack = []
#         result = []
#         curr = root

#         while curr:
#             # process curr
#             result.append(curr.val)
#             stack.append(curr)
#             # update curr
#             curr = curr.left
#             while curr is None:
#                 if not stack:
#                     break
#                 parent = stack.pop()
#                 curr = parent.right
#         return result

#     # recursive (trivial)
#     def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         def rec(root, result):
#             if root is None:
#                 return
#             result.append(root.val)
#             rec(root.left, result)
#             rec(root.right, result)

#         result = []
#         rec(root, result)
#         return result
# @lc code=end
