#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # recursion
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        reverse_next = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return reverse_next

    # iterative
#      def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         new_head = None

#         while head:
#             tail = head.next
#             head.next = new_head
#             new_head = head
#             head = tail
#         return new_head

    # tail recursion
    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     def rec(head, acc):
    #         if head is None:
    #             return acc
    #         else:
    #             curr = head
    #             tail = head.next
    #             curr.next = acc
    #             return rec(tail, curr)
    #     return rec(head, None)
# @lc code=end
