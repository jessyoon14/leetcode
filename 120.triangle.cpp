/*
 * @lc app=leetcode id=120 lang=cpp
 *
 * [120] Triangle
 */

// @lc code=start
class Solution {
   public:
    int minimumTotal(vector<vector<int>>& triangle) {
        int rows = triangle.size();
        int prevSum[rows];
        int currSum[rows];

        prevSum[0] = triangle[0][0];

        for (int i = 1; i < rows; i++) {
            currSum[0] = prevSum[0] + triangle[i][0];  // first column
            for (int j = 1; j < i; j++) {
                currSum[j] = prevSum[j - 1] < prevSum[j] ? prevSum[j - 1] : prevSum[j];
                currSum[j] += triangle[i][j];
            }
            currSum[i] = prevSum[i - 1] + triangle[i][i];  // last column
            memcpy(prevSum, currSum, sizeof(prevSum));
        }

        int min = prevSum[0];
        for (int s : prevSum)
            min = min < s ? min : s;

        return min;
    }
};

// @lc code=end
