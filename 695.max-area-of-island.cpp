/*
 * @lc app=leetcode id=695 lang=cpp
 *
 * [695] Max Area of Island
 */

// @lc code=start

// attempt 1: dynamic programming -> possible, but not clean

// attempt 2: dfs
class Solution
{
public:
    // get area with bfs
    int get_area(vector<vector<int>> &grid, int x, int y)
    {
        int height = grid.size();
        int width = grid[0].size();
        int area = 1;
        queue<pair<int, int>> q;
        q.push(make_pair(x, y));
        grid[y][x] = -1;
        int directions[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

        while (!q.empty())
        {
            int currX = q.front().first;
            int currY = q.front().second;
            q.pop();

            for (int i = 0; i < 4; i++)
            {
                int x = currX + directions[i][0];
                int y = currY + directions[i][1];

                if (x >= 0 && x < width && y >= 0 && y < height && grid[y][x] == 1)
                {
                    area++;
                    grid[y][x] = -1;
                    q.push(make_pair(x, y));
                }
            }
        }
        return area;
    }

    int maxAreaOfIsland(vector<vector<int>> &grid)
    {
        int height = grid.size();
        int width = grid[0].size();
        int max_area = 0;

        for (int y = 0; y < height; y++)
        {
            for (int x = 0; x < width; x++)
            {
                if (grid[y][x] <= 0)
                    continue; // already processed, or 0
                int area = get_area(grid, x, y);
                max_area = area > max_area ? area : max_area;
            }
        }

        return max_area;
    }
};
// @lc code=end
