/*
 * @lc app=leetcode id=74 lang=cpp
 *
 * [74] Search a 2D Matrix
 */

// @lc code=start
class Solution {
   public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int height = matrix.size(), width = matrix[0].size();
        int left = 0, right = height * width - 1;

        while (left <= right) {
            int mid = (left + right) / 2;
            int y = mid / width, x = mid % width;

            if (matrix[y][x] > target)
                right = mid - 1;
            else if (matrix[y][x] < target)
                left = mid + 1;
            else
                return true;
        }

        return false;
    }
};
// @lc code=end
