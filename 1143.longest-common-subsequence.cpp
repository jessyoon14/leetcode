/*
 * @lc app=leetcode id=1143 lang=cpp
 *
 * [1143] Longest Common Subsequence
 */

// @lc code=start
class Solution {
   public:
    int longestCommonSubsequence(string text1, string text2) {
        short arr[1001][1001] = {};  // need to initialize to 0?

        for (short i = 0; i < text1.size(); i++) {
            for (short j = 0; j < text2.size(); j++) {
                arr[j + 1][i + 1] = text1[i] == text2[j] ? arr[j][i] + 1 : max(arr[j + 1][i], arr[j][i + 1]);
            }
        }

        return arr[text2.size()][text1.size()];
    }
};
// @lc code=end
