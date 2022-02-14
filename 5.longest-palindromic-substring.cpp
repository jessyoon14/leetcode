/*
 * @lc app=leetcode id=5 lang=cpp
 *
 * [5] Longest Palindromic Substring
 */

// @lc code=start
class Solution {
    // private:
    // checkPalindromeAt(string s, int left, int right)
   public:
    string longestPalindrome(string s) {
        // find max odd-length palindrome
        int maxLen = 1, bestLeft = 0;
        for (int i = 0; i < s.size(); i++) {
            int left = i, right = i;
            while (left > 0 && right < s.size() - 1 && s[left - 1] == s[right + 1]) {
                left--;
                right++;
            }
            if (right - left + 1 > maxLen) {
                maxLen = right - left + 1;
                bestLeft = left;
            }
        }

        for (int i = 0; i < s.size() - 1; i++) {
            int left = i + 1, right = i;
            while (left > 0 && right < s.size() - 1 && s[left - 1] == s[right + 1]) {
                left--;
                right++;
            }
            if (right - left + 1 > maxLen) {
                maxLen = right - left + 1;
                bestLeft = left;
            }
        }
        return s.substr(bestLeft, maxLen);
    }
};

// @lc code=end
