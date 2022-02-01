/*
 * @lc app=leetcode id=34 lang=cpp
 *
 * [34] Find First and Last Position of Element in Sorted Array
 */

// @lc code=start
class Solution {
   public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int left = 0;
        int right = nums.size() - 1;
        int mid = (left + right) / 2;

        if (!nums.size()) {
            vector<int> result{-1, -1};
            return result;
        }

        // printf("finding target\n");
        // find target
        while (left < right) {
            // printf("mid: %i\n", mid);

            if (nums[mid] > target)
                right = mid - 1;
            else if (nums[mid] < target)
                left = mid + 1;
            else
                break;
            mid = (left + right) / 2;
        }

        if (nums[mid] != target) {
            vector<int> result{-1, -1};
            return result;
        }

        // find left boundary
        // printf("finding left boundary\n");
        int left1 = left;
        int right1 = mid;
        int mid1 = (left1 + right1) / 2;

        while (left1 < right1) {
            // printf("mid: %i\n", mid1);

            if (nums[mid1] < target)
                left1 = mid1 + 1;

            else {
                right1 = mid1;
            }

            mid1 = (left1 + right1) / 2;
        }

        // now, left == right == left boundary

        // find right boundary
        int left2 = mid;
        int right2 = right;
        int mid2 = (left2 + right2) / 2;

        // printf("finding right boundary\n");
        // printf("before loop, left2: %i, right2: %i, mid: %i\n", left2, right2, mid2);

        while (left2 < right2 - 1) {
            // printf("left2: %i, right2: %i, mid: %i\n", left2, right2, mid2);

            if (nums[mid2] == target)
                left2 = mid2;

            else
                right2 = mid2 - 1;
            mid2 = (left2 + right2) / 2;
        }

        if (nums[right2] == target)
            left2 = right2;

        vector<int> result{left1, left2};
        return result;
    }
};
// @lc code=end
