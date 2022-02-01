/*
 * @lc app=leetcode id=34 lang=cpp
 *
 * [34] Find First and Last Position of Element in Sorted Array
 */

// @lc code=start
class Solution {
   public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int size = nums.size();
        vector<int> result(2, -1);

        // optimization, not necessary (in case list empty or not in range)
        if (!size || nums[0] > target || nums[size - 1] < target)
            return result;

        // find left boundary
        int left = 0, right = size - 1;
        while (left < right) {
            int mid = (left + right) / 2;
            if (nums[mid] < target)
                left = mid + 1;
            else if (nums[mid] > target)
                right = mid - 1;
            else
                right = mid;
        }

        if (nums[left] != target)
            return result;
        result[0] = left;

        // find right boundary
        right = size - 1;
        while (left < right) {
            int mid = (left + right + 1) / 2;
            if (nums[mid] == target)
                left = mid;
            else
                right = mid - 1;
        }

        result[1] = right;
        return result;
    }
};

// clean solution: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/discuss/14717/C%2B%2B-binary-search-solution-(lower_bound-implementation).
class Solution {
   public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int left = search(nums, target);
        int right = search(nums, target + 1) - 1;

        if (left < nums.size() && nums[left] == target)
            return {left, right};
        else
            return {-1, -1};
    }

    int search(vector<int>& nums, int target) {
        int left = 0, right = nums.size() - 1;

        while (left <= right) {
            int mid = (right - left) / 2 + left;
            if (nums[mid] < target)
                left = mid + 1;
            else
                right = mid - 1;
        }

        return left;
    }
};

// @lc code=end
