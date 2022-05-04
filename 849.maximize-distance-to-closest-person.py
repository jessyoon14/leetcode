#
# @lc app=leetcode id=849 lang=python3
#
# [849] Maximize Distance to Closest Person
#

# @lc code=start
class Solution:
    """
    Bottom-up DP (array of distance to people left / right)
    """

    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        left = [0] * n
        right = [0] * n

        for i in range(1, n):
            if not seats[i]:
                left[i] = left[i-1] + 1
            if not seats[n-1-i]:
                right[n-1-i] = right[n-i] + 1

        # get max distance between
        max_d = 0
        # test first and last positions
        max_d = max(right[0], left[n-1])
        for i in range(1, n-1):
            max_d = max(max_d, min(left[i], right[i]))
        return max_d

    """
    Bottom-up DP (array of distance to people left / right)
    """

    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        left = [n] * n
        right = [n] * n

        for i in range(n):
            if seats[i]:
                left[i] = 0
            elif i > 0:
                left[i] = left[i-1] + 1
        for i in range(n-1, -1, -1):
            if seats[i]:
                right[i] = 0
            elif i < n-1:
                right[i] = right[i+1] + 1
        return max(min(left[i], right[i]) for i, seat in enumerate(seats) if not seat)

    """
    Two pointer (my solution)
    """

    def maxDistToClosest(self, seats: List[int]) -> int:
        max_distance = 0
        l = -1  # position of last person seen
        for r in range(len(seats)):
            if seats[r]:
                if l == -1:
                    max_distance = r
                else:
                    max_distance = max(max_distance, (r - l) // 2)
                l = r

        max_distance = max(max_distance, len(seats) - 1 - l)

        return max_distance

    """
    Two pointer
    """

    def maxDistToClosest(self, seats: List[int]) -> int:
        people = (i for i, seat in enumerate(seats) if seat)
        prev, future = None, next(people)

        ans = 0
        for i, seat in enumerate(seats):
            if seat:
                prev = i
            else:
                while future is not None and future < i:
                    future = next(people, None)

                left = float('inf') if prev is None else i - prev
                right = float('inf') if future is None else future - i
                ans = max(ans, min(left, right))
        return ans

    """
    Group by zero
    """

    def maxDistToClosest(self, seats: List[int]) -> int:
        ans = seats.index(1)  # distance between left wall and leftmost person
        seats.reverse()
        ans = max(ans, seats.index(1))
        for seat, group in itertools.groupby(seats):
            if not seat:
                K = len(list(group))
                ans = max(ans, (K+1) // 2)
        return ans


# @lc code=end
