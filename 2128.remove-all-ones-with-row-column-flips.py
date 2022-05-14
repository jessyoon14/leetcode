"""


"""


class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        new_grid = [[0] * n for _ in range(m)]

        def flip_column(col):
            for i in range(m):
                new_grid[i][col] = 0 if new_grid[i][col] else 1

        def flip_row(row):
            for j in range(n):
                new_grid[row][j] = 0 if new_grid[row][j] else 1

        # match first row
        for j in range(n):
            if grid[0][j]:
                flip_column(j)

        # match first column
        for i in range(1, m):
            if grid[i][0] != new_grid[i][0]:
                flip_row(i)
        return grid == new_grid
