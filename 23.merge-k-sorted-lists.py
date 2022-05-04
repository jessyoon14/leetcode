#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    Brute force: collect all values then sort
    Time complexity: O(n * log(n)), n: num nodes
    Space complexity: O(2n)
    """
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         acc = []
#         for l in lists: # O(n)
#             while l:
#                 acc.append(l.val)
#                 l = l.next

#         acc.sort(reverse=True) # O(nlogn)
#         result = None
#         for i in range(len(acc)): # O(n)
#             result = ListNode(val=acc[i], next=result)
#         return result

    """
    꼭 다시 보기!!!
    Compare one by one, optimized with priority queue
    """
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         class Wrapper():
#             def __init__(self, node):
#                 self.node = node
#             def __lt__(self, other):
#                 return self.node.val < other.node.val
#         from queue import PriorityQueue
#         head = point = ListNode(0) # head: sentinel node, point: tail
#         q = PriorityQueue()
#         for l in lists:
#             if l:
#                 q.put(Wrapper(l))

#         while not q.empty():
#             node = q.get().node
#             point.next = ListNode(node.val)
#             point = point.next
#             node = node.next
#             if node:
#                 q.put(Wrapper(node))
#         return head.next

    """
    Merge lists one by one
    Time complexity: O(kN), k: # linked lists, N: # nodes
    Space complexity: O(1)
    """
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         def sum_two_lists(a, b):
#             if not a:
#                 return b
#             if not b:
#                 return a

#             result_head = ListNode(0)
#             result_tail = result_head
#             while a and b:
#                 if a.val > b.val:
#                     a, b = b, a
#                 tail = a.next
#                 a.next = None
#                 result_tail.next = a
#                 result_tail = result_tail.next
#                 a = tail
#             if b:
#                 result_tail.next = b

#             return result_head.next

#         if not lists:
#             return None

#         result = lists[0]
#         for i in range(1, len(lists)):
#             result = sum_two_lists(result, lists[i])

#         return result

    """
    VERY IMPORTANT: Divide and conquer
    Time complexity: O(N log k), k: num linked lists. 
        -> each level takes N comparisons, and log k levels!!!!
        -> CAREFUL: time complexity is NOT O(N*k)
    Space complexity: O(1)
    """

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge_two_lists(a, b):
            if not a or not b:
                return a if a else b

            result_head = ListNode(0)
            result_tail = result_head

            while a and b:
                if a.val > b.val:
                    a, b = b, a
                a_tail = a.next
                a.next = None
                result_tail.next = a
                result_tail = result_tail.next
                a = a_tail

            if b:
                result_tail.next = b
            return result_head.next

        if not lists:
            return None

        queue = deque(lists)

        while len(queue) > 1:
            list_count = len(queue)
            # iterate through current level
            for i in range(list_count // 2):
                a = queue.pop()
                b = queue.pop()
                queue.append(merge_two_lists(a, b))

        return queue.pop()

    """
    My solution: choose min head each time (TLE)
    """
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         def reverse(node):
#             if not node:
#                 return None
#             acc = None
#             curr = node
#             while curr:
#                 head = curr
#                 curr = curr.next
#                 head.next = acc
#                 acc = head
#             return acc

#         acc = None
#         # iterate through heads of each linked list
#         m = len(lists)
#         while True:
#             min_idx = -1
#             for i in range(m):
#                 # choose minimum head, remove, and attach head to acc
#                 if lists[i] and (min_idx < 0 or lists[min_idx].val > lists[i].val):
#                     min_idx = i
#             if min_idx > -1:
#                 head = lists[min_idx]
#                 tail = lists[min_idx].next
#                 lists[min_idx] = tail
#                 head.next = acc
#                 acc = head
#             else:
#                 break

#         return reverse(acc)


# @lc code=end
