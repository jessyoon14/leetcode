/*
 * @lc app=leetcode id=994 lang=cpp
 *
 * [994] Rotting Oranges
 */

// @lc code=start
class Solution {
   public:
    int orangesRotting(vector<vector<int>> &grid) {
        int rows = grid.size();
        int cols = grid[0].size();

        const int UNREACHABLE = INT_MAX - 100000;

        vector<vector<int>> dist(rows, vector<int>(cols, UNREACHABLE));  // 왜 -100000?

        int freshCount = 0;
        // DP 1: top to bottom, left to right
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                // is rotten
                if (grid[i][j] == 2)
                    dist[i][j] = 0;

                // is fresh
                else if (grid[i][j] == 1) {
                    freshCount++;
                    if (i > 0)
                        dist[i][j] = min(dist[i][j], dist[i - 1][j] + 1);
                    if (j > 0)
                        dist[i][j] = min(dist[i][j], dist[i][j - 1] + 1);
                }
                printf("dist[%i][%i]: %i\n", i, j, dist[i][j]);
            }
        }

        if (freshCount == 0)
            return 0;

        printf("freshCount: %i\n", freshCount);

        int maxTimeToRot = 0;

        // DP 2: bottom to top, right to left
        for (int i = rows - 1; i >= 0; i--) {
            for (int j = cols - 1; j >= 0; j--) {
                if (grid[i][j] == 1) {
                    if (i < rows - 1)
                        dist[i][j] = min(dist[i][j], dist[i + 1][j] + 1);
                    if (j < cols - 1)
                        dist[i][j] = min(dist[i][j], dist[i][j + 1] + 1);
                    // this orange will never rot
                    if (dist[i][j] == UNREACHABLE)
                        return -1;
                    maxTimeToRot = maxTimeToRot > dist[i][j] ? maxTimeToRot : dist[i][j];
                }
                printf("dist[%i][%i]: %i\n", i, j, dist[i][j]);
            }
        }

        return maxTimeToRot;
    }
};
// @lc code=end
