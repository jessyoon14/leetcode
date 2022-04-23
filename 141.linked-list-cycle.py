#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    # two pointers
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        left = head
        right = head.next

        while left != right:
            if right is None or right.next is None:
                return False
            left = left.next
            right = right.next.next

        return True

     # two pointers
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         if not head:
#             return False
#         left = head
#         right = head.next

#         while right is not None:
#             # check if left is right
#             if left is right:
#                 return True
#             # update right
#             right = right.next
#             if not right:
#                 return False
#             right = right.next
#             # update left
#             left = left.next
#         return False

    # use hashtable
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         nodes_seen = set()
#         while head is not None:
#             if head in nodes_seen:
#                 return True
#             nodes_seen.add(head)
#             head = head.next
#         return False


#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         visited = 10001

#         if head is None:
#             return False
#         elif head.val == visited:
#             return True
#         else:
#             head.val = visited
#             return self.hasCycle(head.next)
# @lc code=end
