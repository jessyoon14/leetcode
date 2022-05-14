#
# @lc app=leetcode id=1146 lang=python3
#
# [1146] Snapshot Array
#

# @lc code=start
class SnapshotArray:
    """
    Hashmap + Binary search
    time: O(log s)
    space: O(s)
    """

    def __init__(self, length: int):
        self.snap_id = 0
        self.map = defaultdict(list)

    def set(self, index: int, val: int) -> None:
        if self.map[index] and self.map[index][-1][0] == self.snap_id:
            self.map[index][-1][1] = val
            return
        self.map[index].append([self.snap_id, val])

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        arr = self.map[index]
        left, right, ans = 0, len(arr) - 1, -1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid][0] <= snap_id:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        if ans == -1:
            return 0
        return arr[ans][1]

    """
    Optimized
    time: O(log s)
    space: O(s)
    """
#     def __init__(self, length: int):
#         self.snap_id = 0
#         self.snaps = [[(0, 0)] for _ in range(length)] # list of lists of (snap_id, value)

#     def set(self, index: int, val: int) -> None:
#         if self.snaps[index][-1][0] == self.snap_id:
#             self.snaps[index].pop()
#         self.snaps[index].append((self.snap_id, val))

#     def snap(self) -> int:
#         self.snap_id += 1
#         return self.snap_id - 1

#     def binary_search(self, history, snap_id):
#         left = 0
#         right = len(history) - 1

#         while left < right:
#             mid = (left + right + 1) // 2
#             mid_id = history[mid][0]
#             if mid_id == snap_id:
#                 return history[mid][1]
#             elif mid_id < snap_id:
#                 left = mid
#             else:
#                 right = mid - 1
#         return history[left][1]

    # def get(self, index: int, snap_id: int) -> int:
    #     history = self.snaps[index]
    #     return self.binary_search(history, snap_id)

    """
    List + binary search
    Space: O (n * m), m: # times snap is called
    """
#     def __init__(self, length: int):
#         self.snap_id = 0
#         self.array = [0] * length
#         self.snaps = []

#     def set(self, index: int, val: int) -> None:
#         self.array[index] = val

#     def snap(self) -> int:
#         self.snap_id += 1
#         self.snaps.append(self.array[:])
#         return self.snap_id - 1

#     def get(self, index: int, snap_id: int) -> int:
#         return self.snaps[snap_id][index]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
# @lc code=end
