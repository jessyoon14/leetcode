#
# @lc app=leetcode id=653 lang=python3
#
# [653] Two Sum IV - Input is a BST
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
    Edge cases:
    - sum = one element * 2
    - target in root
    - target in middle
    - target in leaf
    """

    # 이 솔루션으로 꼭 다시풀기
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:

        left_stack, right_stack = [], []

        def push_left(node):
            # append while left
            while node:
                left_stack.append(node)
                node = node.left

        def push_right():
            while node:
                right_stack.append(node)
                node = node.right

        def get_next_left():
            # pop top
            curr = left_stack.pop()
            # append right child to left stack
            push_left(curr.right)
            # return val
            return curr.val

        def get_next_right():
            curr = right_stack.pop()
            push_right(curr.left)
            return curr.val

        while left < right:
            if left + right == k:
                return True
            elif left + right < k:
                right = get_next_right()
            else:
                left = get_next_left()
        return False

    """
    With two stacks, space complexity O(log h) (h: tree height)
    """

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        left_stack = [root]
        right_stack = [root]

        def push_left(root):
            while root:
                left_stack.append(root)
                root = root.left

        def push_right(root):
            while root:
                right_stack.append(root)
                root = root.right

        def next_left():
            node = left_stack.pop()
            push_left(node.right)
            return node.val

        def next_right():
            node = right_stack.pop()
            push_right(node.left)
            return node.val

        push_left(root)
        push_right(root)
        left = next_left()
        right = next_right()

        def update_left():
            curr = left_stack.pop()
            while curr:
                cur

        while left < right:
            # check current sum
            curr_sum = left + right
            if curr_sum == k:
                return True
            elif curr_sum < k:
                left = next_left()
            else:
                right = next_right()

        return False

    """
    With BST -> sorted list -> two pointer
    """
#     def findTarget(self, root: Optional[TreeNode], k: int) -> bool:

#         nums = []

#         # preprocess
#         def preprocess(root):
#             if not root:
#                 return
#             preprocess(root.left)
#             nums.append(root.val)
#             preprocess(root.right)

#         preprocess(root)
#         left = 0
#         right = len(nums) - 1

#         while left < right:
#             # check if k sum
#             curr_sum = nums[left] + nums[right]
#             if curr_sum == k:
#                 return True
#             elif curr_sum < k:
#                 left += 1
#             else:
#                 right -= 1
#         return False

    """
    BFS and Hashset
    """
#     def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
#         if not root:
#             return False

#         queue = deque([root])
#         vals = set()

#         while queue:
#             curr = queue.pop()
#             # check complement of current node
#             complement = k - curr.val
#             if complement in vals:
#                 return True
#             vals.add(curr.val)
#             if curr.left:
#                 queue.append(curr.left)
#             if curr.right:
#                 queue.append(curr.right)

#         return False

    # more efficient hashset -> insert while searching (look at each node once)
#     def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
#         vals = set()

#         # if complement in set, return. else, insert into set and recursively call
#         def rec(root):
#             if not root:
#                 return False
#             complement = k - root.val
#             if complement in vals:
#                 return True
#             vals.add(root.val)
#             return rec(root.left) or rec(root.right)

#         return rec(root)

    # hashset -> look at each node twice
#     def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
#         vals = set()

#         def preprocess(root):
#             if not root:
#                 return
#             vals.add(root.val)
#             preprocess(root.left)
#             preprocess(root.right)

#         preprocess(root)

#         for v in vals:
#             complement = k - v
#             if complement != v and complement in vals:
#                 return True

#         return False

    # recursive solution, n * log n
#     def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
#         def contains(root, target):
#             if not root:
#                 return False
#             elif root.val == target:
#                 return True
#             elif target < root.val:
#                 return contains(root.left, target)
#             else:
#                 return contains(root.right, target)


#         def rec(node, k):
#             if not node:
#                 return False
#             has_complement = contains(root, k - node.val) and k != node.val * 2

#             return has_complement or rec(node.left, k) or rec(node.right, k)

#         return rec(root, k)


# @lc code=end
