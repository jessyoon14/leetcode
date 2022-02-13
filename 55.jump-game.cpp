/*
 * @lc app=leetcode id=55 lang=cpp
 *
 * [55] Jump Game
 */

// @lc code=start
class Solution {
   public:
    bool canJump(vector<int>& nums) {
        int len = nums.size();
        int i = 0;

        for (int reach = 0; i < len && i <= reach; i++)
            reach = max(reach, i + nums[i]);

        return i == len;
    }
};
// @lc code=end

// class Solution {
//    public:
//     bool canJump(vector<int>& nums) {
//         int len = nums.size();
//         int maxPos = 0;

//         for (int i = 0; i < len; i++) {
//             if (maxPos < i) return false;
//             if (maxPos >= len - 1) return true;
//             maxPos = max(maxPos, i + nums[i]);
//         }
//         return false;
//     }
// };