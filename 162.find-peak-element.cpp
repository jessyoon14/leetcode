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

        // now, left element is going up, right element is going down
        while (left < right) {
            int mid = (left + right) / 2;
            // TODO: mid +- 1로 처리해서 첫 if 문 없앨 수 있어
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
