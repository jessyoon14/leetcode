#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
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
    # in this case, BFS is less efficient than DFS (except for the worst case, when the two are the same)
    # iterative BFS
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        queue = deque([(root, root.val)])

        # 정확한 level이 중요한게 아니라서 굳이 레벨별로 따로 돌 필요는 없음
        while queue:
            curr_node, curr_sum = queue.popleft()
            # check if this is leaf
            if not curr_node.left and not curr_node.right and curr_sum == targetSum:
                return True

            # else, calculate next level
            if curr_node.left:
                queue.append((curr_node.left, curr_sum + curr_node.left.val))

            if curr_node.right:
                queue.append((curr_node.right, curr_sum + curr_node.right.val))
        return False

    # iterative dfs with stack of tuples
    # def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
    #     if not root:
    #         return False
    #     stack = [(root, root.val)]
    #     while stack:
    #         curr, val = stack.pop()
    #         if not curr.left and not curr.right and val == targetSum:
    #             return True
    #         if curr.right:
    #             stack.append((curr.right, val + curr.right.val))
    #         if curr.left:
    #             stack.append((curr.left, val + curr.left.val))
    #     return False

    # iterative dfs
#     def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
#         if not root:
#             return False

#         curr_sum = 0
#         stack = [root.val]

#         while stack:
#             curr_node = stack.pop()
#             curr_sum += curr_node.val

#             # check leaf
#             if not curr_node.left and not curr_node.right:
#                 if curr_sum == targetSum:
#                     return True
#                 else:
#                     curr_sum -= curr_node.val
#                     continue

#             if curr_node.right:
#                 stack.append(curr_node.right)

#             if curr_node.left:
#                 stack.append(curr_node.left)

        # return False

    # cleaner recursive dfs

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        if not root.left and not root.right and root.val == targetSum:
            return True
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)

    # recursive dfs
#     def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
#         def rec(root, curr_sum):
#             if root is None: # path does not end in leaf
#                 return False

#             # check if leaf
#             new_sum = curr_sum + root.val
#             if not (root.left or root.right):
#                 return new_sum == targetSum

#             # check left path & check right path
#             return rec(root.left, new_sum) or rec(root.right, new_sum)

#         if root is None:
#             return False
#         return rec(root, 0)


# @lc code=end
