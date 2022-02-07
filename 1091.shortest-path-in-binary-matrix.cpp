/*
 * @lc app=leetcode id=1091 lang=cpp
 *
 * [1091] Shortest Path in Binary Matrix
 */

// @lc code=start
class Solution {
   private:
    const int step[8][2] = {{-1, -1}, {-1, 0}, {-1, 1}, {0, 1}, {1, 1}, {1, 0}, {1, -1}, {0, -1}};

   public:
    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
        int n = grid.size();
        if (grid[0][0] || grid[n - 1][n - 1]) return -1;  // first or last slot is filled
        if (n == 1) return 1;

        queue<pair<int, int>> next;
        next.push({0, 0});
        grid[0][0] = 1;  // mark as visited

        while (!next.empty()) {
            pair<int, int> curr = next.front();
            next.pop();
            int y = curr.first, x = curr.second;
            const bool edge[8] = {y == 0 || x == 0, y == 0, y == 0 || x == n - 1, x == n - 1,
                                  y == n - 1 || x == n - 1, y == n - 1, y == n - 1 || x == 0, x == 0};

            for (int i = 0; i < 8; i++) {
                int ny = y + step[i][0];
                int nx = x + step[i][1];
                if (!edge[i] && !grid[ny][nx]) {
                    next.push({ny, nx});
                    grid[ny][nx] = grid[y][x] + 1;
                    if (ny == n - 1 && nx == n - 1) return grid[ny][nx];  // found path!
                }
            }
        }

        return -1;
    }
};
// @lc code=end
