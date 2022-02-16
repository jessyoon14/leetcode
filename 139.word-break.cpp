/*
 * @lc app=leetcode id=139 lang=cpp
 *
 * [139] Word Break
 */

// @lc code=start
class Solution {
   private:
    set<string> dict;
    string str;
    vector<bool> isWords;
    int maxWordLength;

    void check(int i) {
        int left = i, right = i;

        while (left > -1) {
            while (left > 0 && !isWords[left - 1])
                left--;
            if (right - left + 1 > maxWordLength)
                isWords[right] = false;
            string w = str.substr(left, right - left + 1);
            if (dict.find(w) != dict.end()) {
                isWords[right] = true;
                return;
            }
            left--;
        }
    }

   public:
    bool wordBreak(string s, vector<string>& wordDict) {
        vector<bool> vec(s.size(), false);
        isWords = vec;
        maxWordLength = 0;

        for (string w : wordDict) {
            dict.insert(w);
            if (w.size() > maxWordLength)
                maxWordLength = w.size();
        }

        str = s;

        for (int i = 0; i < s.size(); i++)
            check(i);

        return isWords[s.size() - 1];
    }
};
// @lc code=end

/*
class Solution {
   private:
    set<string> dict;
    string str;
    bool containsChar[26];

    bool check(int left) {
        // printf("check, left: %i\n", left);
        if (!containsChar[str[left] - 'a']) return false;
        for (int len = 1; left + len - 1 < str.size(); len++) {
            string temp = str.substr(left, len);
            // printf("temp: %s, left: %i, len: %i\n", temp.c_str(), left, len);
            if (dict.find(temp) != dict.end()) {
                // printf("temp is in set!\n");
                if (left + len >= str.size() || check(left + len)) {
                    // printf("find true\n");
                    return true;
                }
            }
        }

        return false;
    }

   public:
    bool wordBreak(string s, vector<string>& wordDict) {
        // put all strings in unordered_map

        memset(containsChar, 0, sizeof(containsChar));
        for (auto w : wordDict) {
            dict.insert(w);
            for (char c : w) {
                containsChar[c - 'a'] = true;
            }
        }

        for (char c : s) {
            if (!containsChar[c - 'a']) return false;
        }

        str = s;

        return check(0);
    }
};
*/