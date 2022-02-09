/*
 * @lc app=leetcode id=40 lang=cpp
 *
 * [40] Combination Sum II
 */

// @lc code=start
class Solution {
   private:
    vector<vector<int>> result;
    int targetSum;

    void buildSum(vector<int>& candidates, vector<int>& acc, int sum) {
        if (sum == targetSum) {
            result.push_back(acc);
            return;
        }

        if (candidates.empty() || sum > targetSum) return;

        int n = candidates.back();
        int count = 0;

        while (!candidates.empty() && candidates.back() == n) {
            candidates.pop_back();
            count++;
        }

        int newSum = sum;
        int count2 = 0;
        for (int i = 0; i < count; i++) {
            newSum += n;
            if (newSum > targetSum) break;
            acc.push_back(n);
            count2++;
            buildSum(candidates, acc, newSum);
        }

        for (int i = 0; i < count2; i++)
            acc.pop_back();

        buildSum(candidates, acc, sum);

        for (int i = 0; i < count; i++)
            candidates.push_back(n);
    }

   public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        targetSum = target;
        sort(candidates.begin(), candidates.end());
        vector<int> acc;
        buildSum(candidates, acc, 0);
        return result;
    }
};
// @lc code=end
