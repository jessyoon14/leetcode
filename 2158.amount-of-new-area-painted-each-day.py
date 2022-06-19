class Solution:
    '''
    brute force: keep track of which slots are painted:

    time O(n * d)
    space O(n + d)
    '''
#     def amountPainted(self, paint: List[List[int]]) -> List[int]:
#         _, width = max(paint, key=lambda x: x[1])

#         painted = [False] * width
#         worklog = []

#         for start, end in paint:
#             curr_work = 0
#             for i in range(start, end):
#                 if not painted[i]:
#                     curr_work += 1
#                     painted[i] = True
#             worklog.append(curr_work)
#         return worklog

    '''
    Jump line
    time O(n + m)
    space O(n + m)
    '''

    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        line, res = [0] * 50001, [0] * len(paint)
        for i, (start, end) in enumerate(paint):
            while start < end:
                jump = max(start + 1, line[start])
                res[i] += 1 if line[start] == 0 else 0
                line[start] = max(line[start], end)  # compression
                start = jump
        return res
