#
# @lc app=leetcode id=1376 lang=python3
#
# [1376] Time Needed to Inform All Employees
#

# @lc code=start
class Solution:
    """
    DFS
    time: O(n)
    space: O(n)
    """

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        subordinates = defaultdict(list)    # could use list instead of dict
        for sub, man in enumerate(manager):
            subordinates[man].append(sub)

        def find_time(emp):
            max_time = 0
            for sub in subordinates[emp]:
                max_time = max(max_time, find_time(sub))
            return max_time + informTime[emp]

        return find_time(headID)

    """
    BFS
    time: O(n)
    space: O(n)
    """

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        subordinates = defaultdict(list)
        for emp, man in enumerate(manager):
            subordinates[man].append(emp)

        queue = deque([(headID, 0)])
        max_time = 0

        while queue:
            man, time = queue.popleft()
            time += informTime[man]
            max_time = max(max_time, time)

            for sub in subordinates[man]:
                queue.appendleft((sub, time))

        return max_time


# @lc code=end
