/*
 * @lc app=leetcode id=200 lang=cpp
 *
 * [200] Number of Islands
 */

// @lc code=start
class Solution {
   public:
    int numIslands(vector<vector<char>>& grid) {
        int h = grid.size(), w = grid[0].size(), count = 0;
        vector<pair<int, int>> coords = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        queue<pair<int, int>> next;
        int curr_y = 0, curr_x = 0, x = 0, y = 0;

        for (int i = 0; i < h; i++) {
            for (int j = 0; j < w; j++) {
                if (grid[i][j] == '1') {
                    count++;
                    next.push({i, j});
                    while (!next.empty()) {
                        pair<int, int> curr = next.front();
                        next.pop();
                        curr_y = curr.first;
                        curr_x = curr.second;
                        if (grid[curr_y][curr_x] == '1') {
                            grid[curr_y][curr_x] = '0';
                            for (int k = 0; k < 4; k++) {
                                y = curr_y + coords[k].first;
                                x = curr_x + coords[k].second;
                                if (x >= 0 && x < w && y >= 0 && y < h && grid[y][x] > 0)
                                    next.push({curr_y + coords[k].first, curr_x + coords[k].second});
                            }
                        }
                    }
                }
            }
        }

        return count;
    }
};
// @lc code=end

/*

class Solution {
   public:
    void markIsland(vector<vector<char>>& grid, int i, int j) {
        int h = grid.size(), w = grid[0].size();
        queue<pair<int, int>> next;
        next.push({i, j});

        vector<pair<int, int>> coords = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

        int count = 0;

        while (!next.empty()) {
            pair<int, int> curr = next.front();
            next.pop();
            i = curr.first;
            j = curr.second;
            if (grid[i][j] == '1') {
                // printf("mark i:%i, j: %i\n", i, j);

                grid[i][j] = '0';
                count++;
                for (int k = 0; k < 4; k++) {
                    int y = i + coords[k].first;
                    int x = j + coords[k].second;
                    if (x >= 0 && x < w && y >= 0 && y < h && grid[y][x] > 0)
                        next.push({i + coords[k].first, j + coords[k].second});
                }
            }
        }
        // printf("island size: %i\n", count);
    }

    int numIslands(vector<vector<char>>& grid) {
        int h = grid.size(), w = grid[0].size(), count = 0;
        for (int i = 0; i < h; i++) {
            for (int j = 0; j < w; j++) {
                // printf("i: %i, j: %i\n", i, j);
                if (grid[i][j] == '1') {
                    count++;
                    // printf("found new island!\n");
                    markIsland(grid, i, j);
                }
            }
        }

        return count;
    }
};
*/