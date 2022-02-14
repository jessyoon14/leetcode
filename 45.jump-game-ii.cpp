/*
 * @lc app=leetcode id=45 lang=cpp
 *
 * [45] Jump Game II
 */

// @lc code=start
class Solution {
   public:
    int jump(vector<int>& nums) {
        int n = nums.size(), start = 0, end = 0, step = 0;

        while (end < n - 1) {
            step++;
            int reach = end + 1;
            for (int i = start; i <= end; i++) {
                if (i + nums[i] >= n - 1) return step;
                reach = max(reach, i + nums[i]);
            }

            start = end + 1;
            end = reach;
        }

        return step;
    }
};
// @lc code=end

class Solution {
   public:
    int jump(vector<int>& nums) {
        int n = nums.size(), reach = 0;
        int jumps[n];
        memset(jumps, 0, sizeof(jumps));

        for (int i = 0; i < n; i++) {
            int newReach = i + nums[i];
            if (newReach > reach) {
                for (int j = reach + 1; j <= newReach && j < n; j++) {
                    jumps[j] = jumps[i] + 1;
                }
                reach = newReach;
            }
        }

        return jumps[n - 1];
    }
};
