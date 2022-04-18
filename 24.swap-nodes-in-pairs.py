#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy

        while head and head.next:
            first = head
            second = head.next

            # swap
            first.next = second.next
            second.next = first
            # connect to prev
            prev.next = second

            # update head
            head = first.next
            prev = first

        return dummy.next

    # iterative solution
#     def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if not head or not head.next:
#             return head

#         new_head = head.next

#         curr_node = head
#         # swap first two nodes
#         first = head
#         second = head.next
#         first.next = second.next
#         second.next = first
#         head = second

#         # iterate through sets of four for swap
#         curr_node = head.next
#         swap = True

#         while curr_node:
#             if curr_node.next and curr_node.next.next:
#                 first = curr_node.next
#                 second = first.next
#                 tail = second.next
#                 curr_node.next = second
#                 second.next = first
#                 first.next = tail
#                 curr_node = first
#             else:
#                 break

#         return head

#     def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         # base case: head is empty or length 1
#         if not head or not head.next:
#             return head

#         # first two nodes
#         first_node = head
#         second_node = head.next

#         # swap
#         first_node.next = self.swapPairs(second_node.next)
#         second_node.next = first_node

#         return second_node


# @lc code=end
