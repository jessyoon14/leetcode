/*
 * @lc app=leetcode id=438 lang=cpp
 *
 * [438] Find All Anagrams in a String
 */

// @lc code=start
class Solution {
   public:
    vector<int> findAnagrams(string s, string p) {
        vector<int> result;

        if (s.length() < p.length()) return {};

        unsigned long long pv = 0;
        for (int i = 0; i < p.length(); i++) {
            pv += 1 << (p[i] - 'a');
            pv += (p[i] - 'a') * (p[i] - 'a');
        }

        unsigned long long sv = 0;
        int windowStartIndex = 0;
        for (int i = 0; i < s.length(); i++) {
            if (i < p.length() - 1) {
                sv += 1 << (s[i] - 'a');
                sv += (s[i] - 'a') * (s[i] - 'a');
            } else if (i == p.length() - 1) {
                sv += 1 << (s[i] - 'a');
                sv += (s[i] - 'a') * (s[i] - 'a');
                windowStartIndex = 0;
                if (sv == pv) result.push_back(windowStartIndex);
            } else {
                sv += 1 << (s[i] - 'a');
                sv += (s[i] - 'a') * (s[i] - 'a');
                sv -= (s[windowStartIndex] - 'a') * (s[windowStartIndex] - 'a');
                sv -= 1 << (s[windowStartIndex] - 'a');
                windowStartIndex++;
                if (sv == pv) result.push_back(windowStartIndex);
            }
        }

        return result;
    }
};

class Solution {
   public:
    vector<int> findAnagrams(string s, string p) {
        int s_len = s.length();
        int p_len = p.length();

        if (s_len < p_len) return {};

        vector<int> freq_p(26, 0);
        vector<int> window(26, 0);

        for (int i = 0; i < p_len; i++) {
            freq_p[p[i] - 'a']++;
            window[s[i] - 'a']++;
        }

        vector<int> ans;
        if (freq_p == window) ans.push_back(0);

        for (int i = p_len; i < s_len; i++) {
            window[s[i - p_len] - 'a']--;
            window[s[i] - 'a']++;

            if (freq_p == window) ans.push_back(i - p_len + 1);
        }

        return ans;
    }
};

// @lc code=end
