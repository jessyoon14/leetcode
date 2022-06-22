#
# @lc app=leetcode id=437 lang=python3
#
# [437] Path Sum III
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

    '''
    Brute force: generate all possible paths
    '''
#     def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
#         if root is None:
#             return 0

#         # for each node, check each path that starts from node
#         count = self.pathSumFrom(root, targetSum, 0)

#         count += self.pathSum(root.left, targetSum)
#         count += self.pathSum(root.right, targetSum)
#         return count

#     def pathSumFrom(self, root, targetSum, currSum):
#         if root is None:
#             return 0

#         count = 0
#         currSum = currSum + root.val
#         if currSum == targetSum:
#             count += 1

#         count += self.pathSumFrom(root.left, targetSum, currSum)
#         count += self.pathSumFrom(root.right, targetSum, currSum)

#         return count

    '''
    Optimized with prefix sum set
    
    time O(n)
    space O(h) -> O(n)
    '''

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        sums = {0: 1}
        return self.pathSumAt(root, sums, targetSum, 0)

    def pathSumAt(self, root, sums, targetSum, currSum):
        if root is None:
            return 0

        count = 0
        currSum += root.val

        if currSum - targetSum in sums:
            count += sums[currSum - targetSum]

        sums[currSum] = sums[currSum] + 1 if currSum in sums else 1

        count += self.pathSumAt(root.left, sums, targetSum, currSum)
        count += self.pathSumAt(root.right, sums, targetSum, currSum)

        sums[currSum] -= 1

        return count


# @lc code=end
