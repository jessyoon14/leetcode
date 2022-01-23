/*
 * @lc app=leetcode id=994 lang=cpp
 *
 * [994] Rotting Oranges
 */

// @lc code=start

class Solution {
   public:
    void update(vector<vector<int>> &grid, vector<vector<int>> &dist, int i, int j) {
        int rows = grid.size();
        int cols = grid[0].size();
        int step[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

        for (int k = 0; k < 4; k++) {
            int x = j + step[k][1];
            int y = i + step[k][0];

            if (x >= 0 && x < cols && y >= 0 && y < rows && grid[y][x] == 1) {
                if (dist[i][j] + 1 < dist[y][x]) {
                    dist[y][x] = dist[i][j] + 1;
                    update(grid, dist, y, x);
                }
            }
        }
    }

    int orangesRotting(vector<vector<int>> &grid) {
        int rows = grid.size();
        int cols = grid[0].size();

        const int UNREACHABLE = INT_MAX - 100000;

        vector<vector<int>> dist(rows, vector<int>(cols, UNREACHABLE));

        int freshCount = 0;

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid[i][j] == 2) {
                    dist[i][j] = 0;
                }

                if (grid[i][j] == 1)
                    freshCount++;
            }
        }

        if (freshCount == 0)
            return 0;

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid[i][j] == 2) {
                    update(grid, dist, i, j);
                }
            }
        }

        int maxTimeToRot = 0;
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid[i][j] == 1)
                    maxTimeToRot = maxTimeToRot > dist[i][j] ? maxTimeToRot : dist[i][j];
            }
        }

        if (maxTimeToRot == UNREACHABLE)
            maxTimeToRot = -1;

        return maxTimeToRot;
    }
};

// @lc code=end