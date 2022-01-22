/*
 * @lc app=leetcode id=542 lang=cpp
 *
 * [542] 01 Matrix
 */

// @lc code=start
class Solution
{
public:
    void updateDistance(vector<vector<int>> &mat, int x, int y, int distance)
    {
        int step[4][2] = {{-1, 0}, {0, -1}, {1, 0}, {0, 1}}; // (y, x)

        // update four courners
        for (int i = 0; i < 4; i++)
        {
            int currX = x + step[i][1];
            int currY = y + step[i][0];

            // out of range
            if (currX < 0 || currX >= mat[0].size() || currY < 0 || currY >= mat.size())
                continue;

            // the direction we just came from || already up-to-date
            else if (mat[currY][currX] == -distance || mat[currY][currX] == -distance - 1)
                continue;

            else if (mat[currY][currX] == 0)
            {
                if (mat[y][x] != 0 && mat[y][x] != -1)
                {
                    mat[y][x] = -1;
                    updateDistance(mat, x, y, 1);
                }
                continue;
            }
            else if (mat[currY][currX] == 1 || mat[currY][currX] < -distance - 1)
            {
                mat[currY][currX] = -distance - 1;
                updateDistance(mat, currX, currY, distance + 1);
            }
        }
    }

    vector<vector<int>> updateMatrix(vector<vector<int>> &mat)
    {
        int height = mat.size();
        int width = mat[0].size();
        for (int y = 0; y < height; y++)
            for (int x = 0; x < width; x++)
                if (mat[y][x] == 0)
                {
                    updateDistance(mat, x, y, 0);
                }

        for (int y = 0; y < height; y++)
            for (int x = 0; x < width; x++)
                mat[y][x] = -mat[y][x];

        return mat;
    }
};
// @lc code=end
