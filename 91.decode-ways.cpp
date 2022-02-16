/*
 * @lc app=leetcode id=91 lang=cpp
 *
 * [91] Decode Ways
 */

// @lc code=start
class Solution {
   public:
    int numDecodings(string s) {
        if (s[0] == '0') return 0;

        int decodeCount[s.size()];
        memset(decodeCount, 0, sizeof(decodeCount));

        for (int i = 0; i < s.size(); i++) {
            if (i == 0)
                decodeCount[i] = 1;
            else {
                if ('0' < s[i])
                    decodeCount[i] += decodeCount[i - 1];
                if ((s[i - 1] == '1' || (s[i - 1] == '2' && s[i] < '7'))) {
                    if (i > 1)
                        decodeCount[i] += decodeCount[i - 2];
                    else
                        decodeCount[i]++;
                }
            }
        }

        return decodeCount[s.size() - 1];
    }
};
// @lc code=end
