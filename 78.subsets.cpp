/*
 * @lc app=leetcode id=78 lang=cpp
 *
 * [78] Subsets
 */

// @lc code=start
class Solution {
   public:
    vector<vector<int>> subsets(vector<int>& nums) {
        if (nums.size() == 0) return {};
        if (nums.size() == 1) return {{}, {nums[0]}};

        int n = nums.back();
        nums.pop_back();

        vector<vector<int>> sets = subsets(nums);
        vector<vector<int>> results = sets;

        for (vector<int> v : sets) {
            v.push_back(n);
            results.push_back(v);
        }

        return results;
    }
};
// @lc code=end

// cascade solution without recursion
class Solution {
   public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> result;
        result.push_back({});

        for (int num : nums) {
            vector<vector<int>> newSubsets;

            for (vector<int> curr : result) {
                curr.push_back(num);
                newSubsets.push_back(curr);
            }

            for (vector<int> curr : newSubsets) {
                result.push_back(curr);
            }
        }

        return result;
    }
};

// bitmask solution
class Solution {
   public:
    vector<vector<int>> subsets(vector<int>& nums) {
        int n = nums.size(), p = 1 << n;
        vector<vector<int>> result(p);

        for (int i = 0; i < p; i++) {
            for (int j = 0; j < n; j++) {
                if ((i >> j) & 1)
                    result[i].push_back(nums[j]);
            }
        }
        return result;
    }
};