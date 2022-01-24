/*
 * @lc app=leetcode id=784 lang=cpp
 *
 * [784] Letter Case Permutation
 */

// @lc code=start
class Solution {
   public:
    vector<string> letterCasePermutation(string s) {
        vector<string> result;
        // make lowercase
        for_each(s.begin(), s.end(), [](char& c) { c = ::tolower(c); });
        recursivePermutation(s, 0, result);
        return result;
    }

    // [0..begin-1]: is fixed
    // [begin..end]: need to permute
    void recursivePermutation(string& s, int currIndex, vector<string>& result) {
        if (currIndex >= s.size()) {
            result.push_back(s);
            return;
        }

        recursivePermutation(s, currIndex + 1, result);

        if (isalpha(s[currIndex])) {
            s[currIndex] = toupper(s[currIndex]);
            recursivePermutation(s, currIndex + 1, result);
            s[currIndex] = tolower(s[currIndex]);
        }
    }
};
// @lc code=end
