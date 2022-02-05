/*
 * @lc app=leetcode id=11 lang=cpp
 *
 * [11] Container With Most Water
 */

// @lc code=start
class Solution {
   public:
    int maxArea(vector<int>& height) {
        int l = 0, r = height.size() - 1, maxArea = 0, currArea = 0;
        int prevHeight;
        while (l < r) {
            currArea = min(height[l], height[r]) * (r - l);
            maxArea = currArea > maxArea ? currArea : maxArea;

            if (height[l] < height[r]) {
                // update left wall to next highest
                prevHeight = height[l];
                while (++l < r && prevHeight >= height[l])
                    ;
            } else {
                // update right wall to next highest
                prevHeight = height[r];
                while (l < --r && prevHeight >= height[r])
                    ;
            }
        }

        return maxArea;
    }
};
// @lc code=end
