/*
 * @lc app=leetcode id=413 lang=cpp
 *
 * [413] Arithmetic Slices
 */

// @lc code=start
class Solution {
   public:
    int numberOfArithmeticSlices(vector<int>& nums) {
        int result = 0, currSliceSize = 2;

        for (int i = 2; i < nums.size(); i++) {
            if (nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]) {
                currSliceSize++;
            } else if (currSliceSize < 3) {
                continue;
            } else {
                result += (currSliceSize - 1) * (currSliceSize - 2) / 2;
                currSliceSize = 2;
            }
        }

        if (currSliceSize > 2) {
            result += (currSliceSize - 1) * (currSliceSize - 2) / 2;
            currSliceSize = 2;
        }

        return result;
    }
};
// @lc code=end
