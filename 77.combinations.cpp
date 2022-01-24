/*
 * @lc app=leetcode id=77 lang=cpp
 *
 * [77] Combinations
 */

// @lc code=start

// solution using recursion
class Solution {
    // n x k x k vector 만들어서 한번 계산할때 저장해줘도 좋을듯
   public:
    vector<vector<int>> combine(int n, int k) {
        if (k == 0 && n > 0) return {{}};
        if (n < k || n < 1 || k < 0) return {};
        if (n == k) {
            vector<int> v(n);
            iota(v.begin(), v.end(), 1);
            return {v};
        }

        vector<vector<int>> containsN = combine(n - 1, k - 1);
        for (auto &v : containsN)
            v.push_back(n);

        vector<vector<int>> withoutN = combine(n - 1, k);
        withoutN.insert(withoutN.end(), containsN.begin(), containsN.end());
        return withoutN;
    }
};

// very efficient solution, using while loop
// https://leetcode.com/problems/combinations/discuss/26992/Short-Iterative-C%2B%2B-Answer-8ms

class Solution {
   public:
    vector<vector<int>> combine(int n, int k) {
        vector<vector<int>> result;
        int i = 0;
        vector<int> p(k, 0);
        while (i >= 0) {
            p[i]++;
            if (p[i] > n)
                --i;
            else if (i == k - 1)
                result.push_back(p);
            else {
                ++i;
                p[i] = p[i - 1];
            }
        }
        return result;
    }
};

// @lc code=end
