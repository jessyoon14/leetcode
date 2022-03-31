# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        def get_height(root: Optional[TreeNode]) -> int:
            # if leaf, add to result and return 0
            if not root:
                return -1

            # else, get height of right child and left child
            right_child_height = get_height(root.right)
            left_child_height = get_height(root.left)

            # get current node's height
            height = max(right_child_height, left_child_height) + 1

            # extend result list if necessary
            if len(result) == height:
                result.append([])

            # add current node to appropriate place in result
            result[height].append(root.val)

            # return height
            return height

        get_height(root)
        return result


# Attempt 1
# class Solution:
#     result = []
#     def getHeight(self, root: Optional([TreeNode])) -> int:


#     def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
#         # is root
#         if not (root.left or root.right):
#             return [[root.val]]

#         # is not root
#         # has left child
#         left_result = []
#         if root.left:
#             left_result = self.findLeaves(root.left)
#         # has right child
#         right_result = []
#         if root.right:
#             right_result = self.findLeaves(root.right)

#         # concatenate results
#         result = []

#         j = 0
#         for i in range(len(left_result)):
#             left = left_result[i]
#             right = []
#             if j < len(right_result):
#                 right = right_result[j]
#                 j += 1

#             result.append(left + right)

#         if j < len(right_result):
#             result += right_result[j:]

#         result += [[root.val]]

#         return result
