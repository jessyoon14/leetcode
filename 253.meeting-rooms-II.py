class Solution:
    """
    Chronological Ordering
    """

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        starts = sorted([i[0] for i in intervals])
        ends = sorted([i[1] for i in intervals])

        s_ptr = 0
        e_ptr = 0
        room_count = 0
        while s_ptr < len(intervals):
            if starts[s_ptr] >= ends[e_ptr]:
                e_ptr += 1
            else:
                room_count += 1
            s_ptr += 1
        return room_count

    """
    Priority queue (or min-heap)
    Sort the given meetings by their start time.
    Initialize a new min-heap and add the first meeting's ending time to the heap. We simply need to keep track of the ending times as that tells us when a meeting room will get free.
    For every meeting room check if the minimum element of the heap i.e. the room at the top of the heap is free or not.
    If the room is free, then we extract the topmost element and add it back with the ending time of the current meeting we are processing.
    If not, then we allocate a new room and add it to the heap.
    After processing all the meetings, the size of the heap will tell us the number of rooms allocated. This will be the minimum number of rooms needed to accommodate all the meetings.
    
    Time complexity: O(N log N)
    Space complexity: O(N) -> 사실상 O(max number of concurrent meetings)

    """
    # def minMeetingRooms(self, intervals: List[List[int]]) -> int:
    #     if not intervals:
    #         return 0
    #     intervals.sort(key=lambda x: x[0])
    #     heap = []
    #     heapify(heap)
    #     heappush(heap, intervals[0][1])
    #     for i in range(1, len(intervals)):
    #         # check if free
    #         if intervals[i][0] >= heap[0]:
    #             heappop(heap)
    #         heappush(heap, intervals[i][1])
    #     return len(heap)

    """
    My solution: very slow... 
    Time complexity: O(N + T), T: max time
    Space complexity: O(N)
    """
#     def minMeetingRooms(self, intervals: List[List[int]]) -> int:
#         d = {}
#         max_time = 0
#         for interval in intervals:
#             d[interval[0]] = d.get(interval[0], []) + [interval[1]]
#             max_time = max(max_time, interval[1])
#         current_meetings = {}
#         max_concurrent_meetings = 0
#         num_current_meetings = 0
#         for time in range(max_time):
#             # add new meetings
#             if time in d:
#                 for finishing_time in d[time]:
#                     current_meetings[finishing_time] = current_meetings.get(finishing_time, 0) + 1
#                 num_current_meetings += len(d[time])
#             # remove finished meetings
#             if time in current_meetings:
#                 num_current_meetings -= current_meetings[time]
#                 del current_meetings[time]
#             max_concurrent_meetings = max(max_concurrent_meetings, num_current_meetings)

#         return max_concurrent_meetings
