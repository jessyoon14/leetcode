#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # clearner iterative solution -> 이거 혼자 못풀었음! 꼭 다시보기
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        curr = root

        if curr or stack:
            while curr:
                stack.append()
                curr = curr.left
            curr = stack.pop()
            result.append(curr.val)
            curr = curr.right

        return result

    # memory efficient recursion
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def rec(root):
            if root is None:
                return
            rec(root.left)
            result.append(root.val)
            rec(root.right)

        rec(root)

        return result

    # basic recursion

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

    # iteration

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return

        stack, result = [], []
        curr = root

        while curr:
            # go to left most node
            if curr.left:
                stack.append(curr)
                curr = curr.left
            elif curr.right:
                result.append(curr.val)
                curr = curr.right
            else:
                result.append(curr.val)
                curr = None
                while curr is None and stack:
                    parent = stack.pop()
                    result.append(parent.val)
                    curr = parent.right
                if not curr and not stack:
                    break

        return result


#     # memory efficient recursion
#     def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         result = []

#         def rec(root):
#             if root is None:
#                 return
#             rec(root.left)
#             result.append(root.val)
#             rec(root.right)

#         rec(root)

#         return result

    # basic recursion
    # def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    #     if root is None:
    #         return []
    #     return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
# @lc code=end
