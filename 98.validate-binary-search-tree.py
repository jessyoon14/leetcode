#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
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
    """
    Here, DFS is more efficient than BFS
    """
    # inorder traversal with iteration -> 아직 못품. 다시풀기!

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = []
        prev = -math.inf

        while stack or root:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            if root.val <= prev:
                return False
            prev = root.val
            root = root.right
        return True

    # inorder traversal with recursion, memory-optimized
#     def isValidBST(self, root: Optional[TreeNode]) -> bool:

#         def inorder(root):
#             if not root:
#                 return True
#             if not inorder(root.left):
#                 return False
#             if root.val <= self.prev:
#                 return False
#             self.prev = root.val
#             return inorder(root.right)

#         self.prev = -math.inf
#         return inorder(root)

    # inorder traversal with recursion
#     def isValidBST(self, root: Optional[TreeNode]) -> bool:
#         inorder = []

#         def rec(root):
#             if not root:
#                 return True
#             if not rec(root.left):
#                 return False
#             # check self
#             if inorder and root.val <= inorder[-1]:
#                 return False
#             inorder.append(root.val)
#             return rec(root.right)


#         return rec(root)


#     # iterative traversal with valid range
#     def isValidBST(self, root: Optional[TreeNode]) -> bool:
#         if root is None:
#             return False

#         stack = [(root, -math.inf, math.inf)]

#         while stack:
#             curr, lower, upper = stack.pop()

#             # check curr node
#             if curr.val < lower or curr.val > upper:
#                 return False

#             # if right, add right to stack
#             if curr.right:
#                 stack.append((curr.right, curr.val + 1, upper))

#             # if left, add left to stack
#             if curr.left:
#                 stack.append((curr.left, lower, curr.val - 1))

#         return True


#     # recursive traversal with valid range
#     def isValidBST(self, root: Optional[TreeNode]) -> bool:
#         def rec(root, lower, upper):
#             if root is None:
#                 return True
#             if root.val < lower or root.val > upper:
#                 return False
#             return rec(root.left, lower, root.val - 1) and rec(root.right, root.val + 1, upper)

#         return rec(root, -math.inf, math.inf)


# @lc code=end
