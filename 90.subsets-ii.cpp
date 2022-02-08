/*
 * @lc app=leetcode id=90 lang=cpp
 *
 * [90] Subsets II
 */

// @lc code=start
class Solution {
    vector<int> frequency;

   private:
    vector<vector<int>> subsets(vector<int>& nums) {
        if (nums.size() == 0) return {{}};

        int n = nums.back();
        nums.pop_back();
        vector<vector<int>> sets = subsets(nums);
        vector<vector<int>> results = sets;

        for (vector<int> v : sets) {
            for (int i = 0; i < frequency[n + 10]; i++) {
                v.push_back(n);
                results.push_back(v);
            }
        }
        return results;
    }

   public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        vector<int> temp(21, 0);
        frequency = temp;
        sort(nums.begin(), nums.end());

        int prev = 20;
        vector<int> unique;
        for (int i = 0; i < nums.size(); i++) {
            frequency[nums[i] + 10]++;
            if (nums[i] != prev) {
                unique.push_back(nums[i]);
                prev = nums[i];
            }
        }

        return subsets(unique);
    }
};
// @lc code=end

class Solution {
   public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> result = {{}};
        int start;

        for (int i; i < nums.size(); i++) {
            if (i == 0 || nums[i] != nums[i - 1]) start = 0;
            for (int end = result.size(); start < end; start++) {
                vector<int> clone = result[start];
                clone.push_back(nums[i]);
                result.push_back(clone);
            }
        }
    }
}