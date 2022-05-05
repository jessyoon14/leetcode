# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    """
    Two pass
    -> can replace with dict to use N space instead of 2N
    """

    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        # create sentinel node
        sentinel = ListNode(val=-1, next=head)

        # set to store seen values
        seen = set()
        # set to store nonunique values
        nonunique = set()

        # first pass: find duplicating values
        curr = head
        while curr:
            # check value
            if curr.val in seen:
                nonunique.add(curr.val)
            else:
                seen.add(curr.val)
            curr = curr.next

        # second pass: remove duplicate nodes
        curr = sentinel
        while curr.next:
            # check curr.next value
            if curr.next.val in nonunique:
                # if nonunique, delete (x update curr)
                curr.next = curr.next.next
            # else update curr
            else:
                curr = curr.next
        return sentinel.next
