/*
 * @lc app=leetcode id=733 lang=cpp
 *
 * [733] Flood Fill
 */

// @lc code=start
class Solution
{
public:
    void try_insert(int width, int height, vector<int> &nextCandidates, int x, int y)
    {
        if (y < 0 || y >= height || x < 0 || x >= width)
            return;

        else
        {
            printf("inserting %i\n", y * width + x);
            nextCandidates.push_back(y * width + x);
        }
    }

    vector<vector<int>> floodFill(vector<vector<int>> &image, int sr, int sc, int newColor)
    {
        int height = image.size();
        int width = image[0].size();

        vector<int> candidates;
        vector<int> nextCandidates = {};

        // change color of initial pixel
        int oldColor = image[sr][sc];
        if (oldColor == newColor)
            return image;
        image[sr][sc] = newColor;
        nextCandidates.push_back(sr * width + sc);

        while (nextCandidates.size() > 0)
        {
            candidates = nextCandidates;
            nextCandidates = {};

            for (auto c : candidates)
            {

                sr = c / width;
                sc = c % width;

                int top = sr - 1;
                int bottom = sr + 1;
                int left = sc - 1;
                int right = sc + 1;
                int x, y;

                // check top neighbor
                if (top >= 0 && image[top][sc] == oldColor)
                {
                    x = sc;
                    y = top;

                    image[y][x] = newColor;
                    nextCandidates.push_back(y * width + x);
                }
                // check right neighbor
                if (right < width && image[sr][right] == oldColor)
                {
                    x = right;
                    y = sr;

                    image[y][x] = newColor;
                    nextCandidates.push_back(y * width + x);
                }
                // check bottom neighbor
                if (bottom < height && image[bottom][sc] == oldColor)
                {
                    x = sc;
                    y = bottom;
                    image[y][x] = newColor;
                    nextCandidates.push_back(y * width + x);
                }
                // check left neighbor
                if (left >= 0 && image[sr][left] == oldColor)
                {
                    x = left;
                    y = sr;

                    image[y][x] = newColor;
                    nextCandidates.push_back(y * width + x);
                }
            }
        }

        return image;
    }
};
// @lc code=end

// other solution
class Solution
{
public:
    vector<vector<int>> floodFill(vector<vector<int>> &image, int sr, int sc, int newColor)
    {
        int m = image.size();
        int n = image[0].size();
        queue<pair<int, int>> q;
        q.push(make_pair(sr, sc));
        int startColor = image[sr][sc];
        if (startColor == newColor)
            return image;
        int e[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        image[sr][sc] = newColor;
        while (!q.empty())
        {
            int r = q.front().first;
            int c = q.front().second;
            q.pop();
            for (int k = 0; k < 4; k++)
            {
                int x = r + e[k][0];
                int y = c + e[k][1];
                if (x >= 0 && y >= 0 && x < m && y < n && image[x][y] == startColor)
                {
                    image[x][y] = newColor;
                    q.push(make_pair(x, y));
                }
            }
        }
        return image;
    }
};