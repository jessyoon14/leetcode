#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
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
    # iterative solution with stack
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = []
        if root is not None:
            stack.append((1, root))

        depth = 0
        while stack != []:
            current_depth, root = stack.pop()
            if root is not None:
                depth = max(depth, current_depth)
                stack.append((current_depth + 1, root.left))
                stack.append((current_depth + 1, root.right))
        return depth

    # # tail recursion (still uses O(n) memory, due to next_level. Could use dequeue outside of rec, which still requires N/2 memory)
    # def maxDepth(self, root: Optional[TreeNode]) -> int:
    #     def rec(nodes, acc):
    #         next_level = []
    #         for n in nodes:
    #             if n:
    #                 next_level.append(n.left)
    #                 next_level.append(n.right)
    #         if next_level:
    #             return rec(next_level, acc+1)
    #         else:
    #             return acc
    #     return rec([root], 0)

    # def maxDepth(self, root: Optional[TreeNode]) -> int:
    #     if root is None:
    #         return 0
    #     return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
# @lc code=end
