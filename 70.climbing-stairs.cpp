/*
 * @lc app=leetcode id=70 lang=cpp
 *
 * [70] Climbing Stairs
 */

// @lc code=start
class Solution {
   public:
    int climbStairs(int n) {
        if (n < 2) return 1;

        int ways[n + 1];
        ways[0] = 1;  // one way to get to 0
        ways[1] = 1;  // one way to get to 1

        for (int i = 2; i < n + 1; i++)
            ways[i] = ways[i - 1] + ways[i - 2];

        return ways[n];
    }
};

// @lc code=end
