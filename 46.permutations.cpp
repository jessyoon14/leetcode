/*
 * @lc app=leetcode id=46 lang=cpp
 *
 * [46] Permutations
 */

// @lc code=start
class Solution {
   public:
    vector<vector<int>> permute(vector<int> &nums) {
        if (nums.size() == 0) return {};
        if (nums.size() == 1) return {{nums[0]}};

        vector<vector<int>> acc;
        int curr = -20;
        for (int i = 0; i < nums.size(); i++) {  // get permutations ending with nums[i]
            curr = nums[i];
            nums.erase(nums.begin() + i);
            vector<vector<int>> temp = permute(nums);

            for (auto &v : temp)
                v.push_back(curr);  // add curr to the end of each vector

            nums.insert(nums.begin() + i, curr);              // restore vector
            acc.insert(acc.end(), temp.begin(), temp.end());  // add to acc
        }

        return acc;
    }
};

// cleaner recursive solution
// https://leetcode.com/problems/permutations/discuss/18247/My-elegant-recursive-C%2B%2B-solution-with-inline-explanation
class Solution {
   public:
    vector<vector<int>> permute(vector<int> &num) {
        vector<vector<int>> result;

        permuteRecursive(num, 0, result);
        return result;
    }

    // permute num[begin..end]
    // invariant: num[0..begin-1] have been fixed/permuted
    void permuteRecursive(vector<int> &num, int begin, vector<vector<int>> &result) {
        if (begin >= num.size()) {
            // one permutation instance
            result.push_back(num);
            return;
        }

        for (int i = begin; i < num.size(); i++) {
            swap(num[begin], num[i]);
            permuteRecursive(num, begin + 1, result);
            // reset
            swap(num[begin], num[i]);
        }
    }
};
// @lc code=end
