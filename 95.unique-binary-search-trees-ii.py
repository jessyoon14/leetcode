#
# @lc app=leetcode id=95 lang=python3
#
# [95] Unique Binary Search Trees II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

        mem = {}

        def rec(left: int, right: int) -> List[Optional[TreeNode]]:
            if left > right:
                return [None]
            elif left == right:
                return [TreeNode(left)]

            elif mem.get((left, right)):
                return mem.get((left, right))

            result = []

            for i in range(left, right + 1):
                left_subtrees = rec(left, i-1)
                right_subtrees = rec(i+1, right)

                for left_subtree in left_subtrees:
                    for right_subtree in right_subtrees:
                        result.append(TreeNode(i, left_subtree, right_subtree))

            mem[(left, right)] = result
            return result

        return rec(1, n) if n else []

# @lc code=end
