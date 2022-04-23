#
# @lc app=leetcode id=203 lang=python3
#
# [203] Remove Linked List Elements
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# edge cases
# empty list
# list of length one: remove & not remove
# remove first element
# remove last element
# remove alternating elements
# remove continuous elements

class Solution:
    # recursion
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return head

        head.next = self.removeElements(head.next, val)
        if head.val == val:
            return head.next
        else:

            return head
#     def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
#         sentinel = ListNode()
#         sentinel.next = head

#         prev = sentinel
#         curr = head

#         while curr:
#             if curr.val == val:
#                 prev.next = curr.next
#             else:
#                 prev = curr
#             curr = curr.next
#         return sentinel.next

#     def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
#         dummy = ListNode(val+1)
#         dummy.next = head

#         curr = dummy

#         while curr.next is not None:
#             # need to remove next node
#             if curr.next.val == val:
#                 curr.next = curr.next.next

#             # can keep next node
#             else:
#                 curr = curr.next

#         return dummy.next
# @lc code=end
