/*
 * @lc app=leetcode id=47 lang=cpp
 *
 * [47] Permutations II
 */

// @lc code=start
class Solution {
   private:
    vector<vector<int>> result;
    void buildPermutation(vector<int>& nums, vector<int>& acc) {
        if (nums.empty()) result.push_back(acc);

        for (int i = 0; i < nums.size(); i++) {
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            int n = nums[i];
            acc.push_back(n);
            nums.erase(nums.begin() + i);
            buildPermutation(nums, acc);
            acc.pop_back();
            nums.insert(nums.begin() + i, n);
        }
    }

   public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<int> acc;
        buildPermutation(nums, acc);
        return result;
    }
};
// @lc code=end
