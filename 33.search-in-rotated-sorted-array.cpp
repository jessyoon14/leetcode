/*
 * @lc app=leetcode id=33 lang=cpp
 *
 * [33] Search in Rotated Sorted Array
 */

// @lc code=start
class Solution {
   public:
    int search(vector<int>& nums, int target) {
        // find pivot spot (index of min)
        int left = 0, right = nums.size() - 1;
        while (left < right) {
            int mid = (left + right) / 2;

            if (nums[mid] > nums[right])
                left = mid + 1;
            else
                right = mid;
        }
        int min = left;

        // find target
        if (target >= nums[0])
            left = 0, right = min > 0 ? min - 1 : nums.size() - 1;
        else
            left = min, right = nums.size() - 1;

        while (left < right) {
            int mid = (left + right) / 2;
            if (nums[mid] < target)
                left = mid + 1;
            else if (nums[mid] > target)
                right = mid - 1;
            else
                return mid;
        }

        if (nums[left] == target)
            return left;
        else
            return -1;
    }
};
// @lc code=end

// clever solution: https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/14435/Clever-idea-making-it-simple

int search(vector<int>& nums, int target) {
    int lo = 0, hi = nums.size();
    while (lo < hi) {
        int mid = (lo + hi) / 2;

        double num = (nums[mid] < nums[0]) == (target < nums[0])
                         ? nums[mid]
                     : target < nums[0] ? -INFINITY
                                        : INFINITY;

        if (num < target)
            lo = mid + 1;
        else if (num > target)
            hi = mid;
        else
            return mid;
    }
    return -1;
}

// alternate solution using mod
// https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/14425/Concise-O(log-N)-Binary-search-solution

class Solution {
   public:
    int search(int A[], int n, int target) {
        int lo = 0, hi = n - 1;
        // find the index of the smallest value using binary search.
        // Loop will terminate since mid < hi, and lo or hi will shrink by at least 1.
        // Proof by contradiction that mid < hi: if mid==hi, then lo==hi and loop would have been terminated.
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (A[mid] > A[hi])
                lo = mid + 1;
            else
                hi = mid;
        }
        // lo==hi is the index of the smallest value and also the number of places rotated.
        int rot = lo;
        lo = 0;
        hi = n - 1;
        // The usual binary search and accounting for rotation.
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            int realmid = (mid + rot) % n;
            if (A[realmid] == target) return realmid;
            if (A[realmid] < target)
                lo = mid + 1;
            else
                hi = mid - 1;
        }
        return -1;
    }
};