/*
 * @lc app=leetcode id=209 lang=cpp
 *
 * [209] Minimum Size Subarray Sum
 */

// @lc code=start
class Solution {
   public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int left = 0, ans = nums.size() + 1, sum = 0, len = 0;

        for (int right = 0; right < nums.size(); right++) {
            sum += nums[right];
            if (sum >= target) {
                while (sum >= target) sum -= nums[left++];
                len = right - left + 2;
                ans = ans > len ? len : ans;
            }
        }

        ans = ans > nums.size() ? 0 : ans;
        return ans;
    }
};
// @lc code=end
