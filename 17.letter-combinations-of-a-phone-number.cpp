/*
 * @lc app=leetcode id=17 lang=cpp
 *
 * [17] Letter Combinations of a Phone Number
 */

// @lc code=start
class Solution {
   public:
    vector<string> letterCombinations(string digits) {
        if (digits.empty()) return {};

        vector<string> digitToLetter = {"abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        vector<string> results = {""};

        for (char const &d : digits) {
            string candidates = digitToLetter[d - '2'];
            int results_size = results.size();
            for (int i = 0; i < results_size; i++) {
                string acc = results.front();
                results.erase(results.begin());
                for (char const &c : candidates) {
                    acc.push_back(c);
                    results.push_back(acc);
                    acc.pop_back();
                }
            }
        }
        return results;
    }
};
// @lc code=end
