#
# @lc app=leetcode id=779 lang=python3
#
# [779] K-th Symbol in Grammar
#

# @lc code=start
class Solution:

    def kthGrammar(self, n: int, k: int) -> int:
        # check initial conditions if necessary

        if k == 1:
            return 0
        elif k == 2:
            return 1

        parent = self.kthGrammar(n - 1, (k+1) // 2)
        if parent == 0:
            return 0 if k % 2 > 0 else 1
        else:
            return 1 if k % 2 > 0 else 0


#     def kthGrammar(self, N, K):
#         # Think of the base case, already given here though
#         if N == 1 and K == 1:
#             return 0

#         # We need to do some observation here:
#         # 1 - Calculate the length of every row which is as below
#         mid = (2 ** (N-1))//2

#         # If the K lies in the first half, it is actually same as prev row
#         if K <= mid:
#             return int(self.kthGrammar(N-1, K))

#         else:
#             # Else it subtract the first half and then it is same as
#             # complement of the prev row
#             return  int(not self.kthGrammar(N-1, K-mid))


#     def kthGrammar(self, n: int, k: int) -> int:
#         m = math.ceil(math.log(k, 2)) + 1
#         row = deque()

#         def get_row(m):
#             if m == 1:
#                 row.append(0)
#                 return
#             get_row(m-1)
#             for i in range(2 ** (m-2)):
#                 curr = row.popleft()
#                 if curr == 0:
#                     row.extend([0,1])
#                 else:
#                     row.extend([1,0])

#         get_row(m)

#         for i in range(k-1):
#             row.popleft()
#         return row.popleft()

# @lc code=end
