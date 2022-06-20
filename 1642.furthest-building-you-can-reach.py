#
# @lc app=leetcode id=1642 lang=python3
#
# [1642] Furthest Building You Can Reach
#

# @lc code=start
import heapq

# class Solution:
#     def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
#         # preprocess jumps
#         jumps = []
#         n = len(heights)
#         for i, height in enumerate(heights):
#             if i < n - 1:
#                 jump = heights[i + 1] - height
#                 if jump > 0:
#                     jumps.append([jump, i + 1])
#                 elif jumps:
#                     jumps[-1][1] = i + 1
#                 else:
#                     jumps.append([0, i + 1])

#         heap = []

#         for jump_idx, (jump, reachable_idx) in enumerate(jumps):
#             if len(heap) < ladders:
#                 if jump > 0:
#                     heapq.heappush(heap, jump)
#             else:
#                 # check if this jump should be ladder
#                 min_ladder_jump = heap[0] if heap else float('inf')
#                 if min_ladder_jump < jump:
#                     evicted_ladder_jump = heapq.heappop(heap)
#                     bricks -= evicted_ladder_jump
#                     heapq.heappush(heap, jump)
#                 else:
#                     bricks -= jump

#             if bricks < 0:
#                 if jump_idx == 0:
#                     return 0
#                 return jumps[jump_idx - 1][1]

#         return n - 1

'''
1: use min-heap to allocate ladders to tallest climbs
insight
- 제일 큰거 n개만 저장해야한다면 heap/priority queue 사용!

time: N * log min(L, N)
space: min(N, L)
'''


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        ladder_allocations = []
        for i in range(len(heights) - 1):
            climb = heights[i + 1] - heights[i]
            if climb <= 0:
                continue
            heapq.heappush(ladder_allocations, climb)
            if len(ladder_allocations) <= ladders:
                continue
            bricks -= heapq.heappop(ladder_allocations)
            if bricks < 0:
                return i
        return len(heights) - 1


'''
use max-heap to allocate bricks to shortest climbs
time O(N log N)
space O(N)
'''
# class Solution:
#     def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
#         brick_allocations = []
#         for i in range(len(heights) - 1):
#             climb = heights[i + 1] - heights[i]

#             # don't need tools
#             if climb <= 0:
#                 continue

#             # use bricks
#             bricks -= climb
#             heapq.heappush(brick_allocations, -climb)

#             # exceeded number of bricks
#             if bricks < 0:
#                 # exchange tallest bricks for ladders
#                 bricks += - heapq.heappop(brick_allocations)
#                 ladders -= 1

#             if ladders < 0:
#                 return i

#         return len(heights) - 1

'''
    Binary search for final reachable building
    - can be optimized to sort all climbs at first with index attached -> then only takes time O(n log n)
    time O(n (log n) ^ 2)
    space O(n)
    '''
# def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
#     def is_reachable(building_index):
#         climbs = []
#         for h1, h2 in zip(heights[:building_index], heights[1:building_index + 1]):
#             if h2 - h1 > 0:
#                 climbs.append(h2 - h1)
#         climbs.sort()
#         bricks_remaining = bricks
#         ladders_remaining = ladders
#         for climb in climbs:
#             if climb <= bricks_remaining:
#                 bricks_remaining -= climb
#             elif ladders_remaining >= 1:
#                 ladders_remaining -= 1
#             else:
#                 return False
#         return True
#     lo = 0
#     hi = len(heights) - 1
#     while lo < hi:
#         mid = lo + (hi - lo + 1) // 2
#         if is_reachable(mid):
#             lo = mid
#         else:
#             hi = mid - 1
#    return hi


# @lc code=end
