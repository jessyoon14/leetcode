/*
 * @lc app=leetcode id=136 lang=cpp
 *
 * [136] Single Number
 */

// @lc code=start
class Solution {
   public:
    int singleNumber(vector<int>& nums) {
        int acc = 0;
        for (int i : nums)
            acc ^= i;
        return acc;
    }
};
// @lc code=end
