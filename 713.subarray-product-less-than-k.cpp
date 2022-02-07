/*
 * @lc app=leetcode id=713 lang=cpp
 *
 * [713] Subarray Product Less Than K
 */

// @lc code=start
class Solution {
   public:
    int numSubarrayProductLessThanK(vector<int>& nums, int k) {
        if (k <= 1) return 0;
        int prod = 1, ans = 0, left = 0;

        for (int right = 0; right < nums.size(); right++) {
            prod *= nums[right];
            while (prod >= k) prod /= nums[left++];
            ans += right - left + 1;
        }

        return ans;
    }
};
// @lc code=end

/*
class Solution {
   public:
    int numSubarrayProductLessThanK(vector<int>& nums, int k) {
        vector<int> window;
        int result = 0;
        int prod = 1;


        for (int i = 0; i < nums.size(); i++) {
            window.push_back(nums[i]);
            prod *= nums[i];

            if (prod >= k) {
                i = i - window.size() + 1;
                prod = 1;
                window = {};

            } else {
                result++;
            }

            if (i == nums.size() - 1) {
                if (prod < k) {
                    result += (window.size() * (window.size() - 1)) / 2;
                } else {
                    i = i - window.size() + 1;
                    prod = 1;
                    window = {};
                }
            }
        }

        return result;
    }
};


class Solution {
   public:
    int numSubarrayProductLessThanK(vector<int>& nums, int k) {
        vector<int> window;
        int result = 0;
        int prod = 1;

        for (int i = 0; i < nums.size(); i++) {
            window.push_back(nums[i]);
            prod *= nums[i];
            // printf("i: %i, prod: %i\n", i, prod);

            if (prod >= k) {
                // printf("over\n");
                i = i - window.size() + 1;
                prod = 1;
                window = {};

            } else {
                // printf("yes\n");
                result++;
            }

            if (i == nums.size() - 1) {
                // printf("is last\n");
                i = i - window.size() + 1;
                prod = 1;
                window = {};
            }
        }

        return result;
    }
};

*/