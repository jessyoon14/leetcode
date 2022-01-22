/*
 * @lc app=leetcode id=542 lang=cpp
 *
 * [542] 01 Matrix
 */

// @lc code=start
class Solution
{
public:
    void updateDistance(vector<vector<int>> &mat, int x, int y)
    {
        int step[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}}; // (y, x)

        for (int i = 0; i < 4; i++)
        {

            int nextX = x + step[i][1];
            int nextY = y + step[i][0];

            if (nextX < 0 || nextX >= mat[0].size() || nextY < 0 || nextY >= mat.size())
                continue;

            int currDistance = getDistance(mat, nextX, nextY);
            minDistance = minDistance < currDistance ? minDistance : currDistance;
            if (minDistance == 0)
                break;
        }
    }

    int getDistance(vector<vector<int>> &mat, int x, int y)
    {
        if (mat[y][x] == 0)
            return 0;

        int minDistance = 20001;

        if (mat[y][x] < 0)
            return -mat[y][x];
        else
            mat[y][x] = -minDistance;

        int step[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}}; // (y, x)

        for (int i = 0; i < 4; i++)
        {

            int nextX = x + step[i][1];
            int nextY = y + step[i][0];

            if (nextX < 0 || nextX >= mat[0].size() || nextY < 0 || nextY >= mat.size())
                continue;

            int currDistance = getDistance(mat, nextX, nextY);
            minDistance = minDistance < currDistance ? minDistance : currDistance;
            if (minDistance == 0)
                break;
        }

        for (int i = 0; i < 4; i++)
        {

            int nextX = x + step[i][1];
            int nextY = y + step[i][0];

            if (nextX < 0 || nextX >= mat[0].size() || nextY < 0 || nextY >= mat.size())
                continue;
            // need to update
            if (mat[nextY][nextX] < 0 && mat[nextY][nextX] < -minDistance - 2)
            {
                mat[nextY][nextX] = -minDistance - 2;
                updateDistance(mat, nextX, nextY);
            }
        }

        mat[y][x] = -(minDistance + 1);
        return minDistance + 1;
    }
    vector<vector<int>> updateMatrix(vector<vector<int>> &mat)
    {
        int height = mat.size();
        int width = mat[0].size();
        for (int y = 0; y < height; y++)
            for (int x = 0; x < width; x++)
                if (mat[y][x] > 0)
                {
                    printf("in updateMatrix, call getDistance\n");
                    getDistance(mat, x, y);
                }

        for (int y = 0; y < height; y++)
            for (int x = 0; x < width; x++)
                mat[y][x] = -mat[y][x];

        return mat;
    }
};
// @lc code=end
