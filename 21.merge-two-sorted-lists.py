#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
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
class Solution:
    # iterative solution
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()  # dummy, must remove before return
        prev = head

        while list1 and list2:
            if list1.val < list2.val:
                prev.next = list1
                prev = prev.next
                list1 = list1.next
            else:
                prev.next = list2
                prev = prev.next
                list2 = list2.next

        prev.next = list1 if list1 else list2

        return head.next

    # simpler recursive solution
    # def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    #     if list1 is None:
    #         return list2
    #     elif list2 is None:
    #         return list1
    #     if list1.val < list2.val:
    #         list1.next = self.mergeTwoLists(list1.next, list2)
    #         return list1
    #     else:
    #         list2.next = self.mergeTwoLists(list1, list2.next)
    #         return list2


#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

#         def merge(list1, list2, acc):
#             if not list1 and not list2:
#                 return acc
#             elif list2 is None or (list1 and list1.val < list2.val):
#                 list1_tail = list1.next
#                 list1.next = acc
#                 return merge(list1_tail, list2, list1)
#             else:
#                 list2_tail = list2.next
#                 list2.next = acc
#                 return merge(list1, list2_tail, list2)

#         def reverse(node, acc):
#             if node is None:
#                 return acc
#             tail = node.next
#             node.next = acc
#             return reverse(tail, node)

#         result = merge(list1, list2, None)
#         return reverse(result, None)

# @lc code=end
