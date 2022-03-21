/*
 * @lc app=leetcode id=583 lang=cpp
 *
 * [583] Delete Operation for Two Strings
 */

// @lc code=start
class Solution {
   public:
    int minDistance(string word1, string word2) {
        short arr[501][501];

        for (int i = 1; i < 501; i++) {
            arr[0][i] = i;
            arr[i][0] = i;
        }

        for (int i = 0; i < word1.size(); i++) {
            for (int j = 0; j < word2.size(); j++) {
                arr[i + 1][j + 1] = word1[i] == word2[j] ? arr[i][j] : min(arr[i + 1][j], arr[i][j + 1]) + 1;
            }
        }

        return arr[word1.size()][word2.size()];
    }
};
// @lc code=end
