#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr is not None and curr.next is not None:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head

#     def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if head is None:
#             return head

#         left = head
#         right = head.next

#         while right is not None:
#             if left.val != right.val:
#                 left.next = right
#                 left = left.next
#             right = right.next

#         left.next = right
#         return head
# @lc code=end
