/*
 * @lc app=leetcode id=162 lang=cpp
 *
 * [162] Find Peak Element
 */

// @lc code=start
class Solution {
   public:
    int findPeakElement(vector<int>& nums) {
        int left = 0, right = nums.size() - 1;

        if (nums.size() == 1)
            return 0;

        // check first element
        if (nums[0] > nums[1])
            return 0;

        // check last element
        if (nums[right] > nums[right - 1])
            return right;

        // now, left element is going up, right element is going down
        while (left < right) {
            int mid = (left + right) / 2;
            if (mid == left) {
                if (nums[left] < nums[right])
                    return right;
                else
                    return left;
            }

            bool isRising = nums[mid] > nums[mid - 1];

            if (isRising)
                left = mid;
            else
                right = mid;
        }

        return left;
    }
};
// @lc code=end
