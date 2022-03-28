#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
class Solution:
    height = 0
    width = 0

    def markIsland(self, grid: List[List[str]], i: int, j: int):
        grid[i][j] = "0"
        # adjacent_land = [(i, j)]
        adjacent_land = deque([(i, j)])

        # fill adjacent land
        # iterate through adjacent_land, mark "0" and fill adjacent_land
        while adjacent_land:
            i, j = adjacent_land.popleft()
            steps = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            for di, dj in steps:
                next_i = i + di
                next_j = j + dj
                if next_i > -1 and next_i < self.height and next_j > -1 and next_j < self.width and grid[next_i][next_j] == "1":
                    grid[next_i][next_j] = "0"
                    adjacent_land.append((next_i, next_j))

    def numIslands(self, grid: List[List[str]]) -> int:
        island_count = 0
        self.height = len(grid)
        self.width = len(grid[0])
        for i in range(self.height):
            for j in range(self.width):
                if grid[i][j] == "1":
                    # found island
                    island_count += 1
                    self.markIsland(grid, i, j)

        return island_count


# @lc code=end
