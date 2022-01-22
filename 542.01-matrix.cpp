/*
 * @lc app=leetcode id=542 lang=cpp
 *
 * [542] 01 Matrix
 */

// @lc code=start
class Solution
{
public:
    int getDistance(vector<vector<int>> &mat, int x, int y)
    {
        int NOT_FOUND = 20001;
        printf("getDistance, y: %i, x: %i\n", y, x);

        if (x < 0 || x >= mat[0].size() || y < 0 || y >= mat.size())
            return NOT_FOUND; // not found or already called

        if (mat[y][x] == -NOT_FOUND)
            return -mat[y][x];

        // current slot is zero
        if (!mat[y][x])
            return 0;

        int minDistance = mat[y][x] > 0 ? NOT_FOUND : -mat[y][x];

        if (mat[y][x] == 1)
            mat[y][x] = -NOT_FOUND; // mark this node as already called

        int step[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

        int currDistance;

        for (int i = 0; i < 4; i++)
        {
            // printf("in iter 1, minDistance: %i\n", minDistance);

            int currX = x + step[i][0];
            int currY = y + step[i][1];
            if (currX < 0 || currX >= mat[0].size() || currY < 0 || currY >= mat.size())
                continue;
            // printf("mat value: %i\n", mat[y + step[i][1]][x + step[i][0]]);
            // printf("before if: y: %i, x: %i \n", y + step[i][1], x + step[i][0]);
            if (minDistance == mat[y + step[i][1]][x + step[i][0]])
            {
                continue;
            }

            if (minDistance < mat[y + step[i][1]][x + step[i][0]])
            {
                // printf("enter if\n");
                mat[y + step[i][1]][x + step[i][0]] = minDistance + 1;
            }

            // printf("reach 1\n");
            currDistance = getDistance(mat, x + step[i][0], y + step[i][1]);
            minDistance = minDistance > currDistance ? currDistance : minDistance;
        }

        for (int i = 0; i < 4; i++)
        {
            // printf("in iter 2\n");
            int currX = x + step[i][0];
            int currY = y + step[i][1];
            if (currX < 0 || currX >= mat[0].size() || currY < 0 || currY >= mat.size())
                continue;
            if (-mat[currY][currX] > minDistance)
                getDistance(mat, x + step[i][0], y + step[i][1]);
        }

        mat[y][x] = -(minDistance + 1);

        // printf("distance to [%i][%i] is %i\n", y, x, minDistance + 1);
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
