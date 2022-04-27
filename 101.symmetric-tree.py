#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # cleaner bfs queue solution
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        q = deque()
        q.append(root)
        q.append(root)
        while q:
            node1 = q.popleft()
            node2 = q.popleft()
            if node1 is None and node2 is None:
                continue
            if node1 is None or node2 is None:
                return False
            if node1.val == node2.val:
                q.append(node1.left)
                q.append(node2.right)
                q.append(node1.right)
                q.append(node2.left)
            else:
                return False
        return True

    # bfs queue solution -> too complicated
#     def isSymmetric(self, root: Optional[TreeNode]) -> bool:
#         if root is None:
#             return False

#         if (root.left or root.right) and not (root.left and root.right):
#             return False

#         queue = deque([root.left, root.right])
#         next_queue = deque()


#         while queue:
#             # get next level
#             queue_size = len(queue)
#             if queue_size > 1 and queue_size % 2 > 0:
#                 return False
#             for i in range(queue_size//2):
#                 right = queue.pop()
#                 left = queue.popleft()
#                 if right is None and left is None:
#                     continue
#                 elif right is None or left is None:
#                     return False
#                 elif right.val != left.val:
#                     return False
#                 else:
#                     next_queue.appendleft(left.right)
#                     next_queue.appendleft(left.left)
#                     next_queue.append(right.left)
#                     next_queue.append(right.right)
#             queue, next_queue = next_queue, queue
#         return True

    # recursive solution
#     def isSymmetric(self, root: Optional[TreeNode]) -> bool:
#         if root is None:
#             return False

#         def is_mirror_twin(node1, node2):
#             if node1 is None and node2 is None:
#                 return True
#             if node1 is None or node2 is None:
#                 return False
#             return node1.val == node2.val and is_mirror_twin(node1.right, node2.left) and is_mirror_twin(node1.left, node2.right)

#         return is_mirror_twin(root.left, root.right)


# @lc code=end
