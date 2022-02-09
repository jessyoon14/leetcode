/*
 * @lc app=leetcode id=39 lang=cpp
 *
 * [39] Combination Sum
 */

// @lc code=start
class Solution {
   private:
    vector<vector<int>> result;
    int targetSum;

    void buildSum(vector<int>& candidates, vector<int>& acc, int sum) {
        if (candidates.empty())
            return;

        int n = candidates.back();
        candidates.pop_back();
        int count = 0;
        while (sum <= targetSum) {
            if (sum == targetSum) {
                result.push_back(acc);
                break;
            } else {
                buildSum(candidates, acc, sum);
                acc.push_back(n);
                sum += n;
                count++;
            }
        }

        candidates.push_back(n);
        for (int i = 0; i < count; i++)
            acc.pop_back();
    }

   public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        targetSum = target;
        sort(candidates.begin(), candidates.end());
        vector<int> acc;
        buildSum(candidates, acc, 0);
        return result;
    }
};
// @lc code=end
