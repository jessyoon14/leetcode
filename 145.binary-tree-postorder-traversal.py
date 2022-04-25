#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # modularized solution
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def find_leaf(node):
            while node:
                stack.append(node)
                if node.left:
                    node = node.left
                else:
                    node = node.right

        def has_next():
            return len(stack) > 0

        def get_next():
            node = stack.pop()
            if stack and stack[-1].left == node:
                find_leaf(stack[-1].right)
            return node.val

        stack = []
        result = []
        find_leaf(root)

        while (has_next()):
            result.append(get_next())

        return result

    # iterative solution without visited flag -> 혼자 풀 수 있을 때까지 연습하기!
    # def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    #     stack, result = [], []
    #     while stack or root:
    #         # find leaf nodes
    #         while root:
    #             stack.append(root)
    #             if root.left:
    #                 root = root.left
    #             else:
    #                 root = root.right
    #         node = stack.pop()
    #         result.append(node.val)
    #         if stack and stack[-1].left == node:
    #             root = stack[-1].right
    #     return result

    # preorder (modified to read right subtree first), then reverse
#     def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         result, stack = [], [root]

#         while stack:
#             node = stack.pop()
#             if node:
#                 result.append(node.val)
#                 stack.append(node.left)
#                 stack.append(node.right)
#         return result[::-1]

    # iterative solution with visited flag
#     def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         result = []
#         stack = [(root, False)]

#         while stack:
#             node, visited = stack.pop()
#             if node:
#                 if visited:
#                     result.append(node.val)
#                 else:
#                     stack.append((node, True))
#                     stack.append((node.right, False))
#                     stack.append((node.left, False))
#         return result

    # memory efficient recursion
#     def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         result = []

#         def rec(root):
#             if root is None:
#                 return
#             rec(root.left)
#             rec(root.right)
#             result.append(root.val)

#         return rec(root)

    # basic recursion
    # def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    #     if root is None:
    #         return []
    #     return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
# @lc code=end
