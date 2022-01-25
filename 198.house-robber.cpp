/*
 * @lc app=leetcode id=198 lang=cpp
 *
 * [198] House Robber
 */

// @lc code=start
class Solution {
   public:
    int rob(vector<int>& nums) {
        if (nums.size() == 1) return nums[0];

        int money[nums.size()];
        money[0] = nums[0];
        money[1] = nums[0] > nums[1] ? nums[0] : nums[1];

        for (int i = 2; i < nums.size(); i++) {
            int withCurr = money[i - 2] + nums[i];
            int withoutCurr = money[i - 1];
            money[i] = withCurr > withoutCurr ? withCurr : withoutCurr;
        }

        return money[nums.size() - 1];
    }
};
// @lc code=end
