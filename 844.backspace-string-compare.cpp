/*
 * @lc app=leetcode id=844 lang=cpp
 *
 * [844] Backspace String Compare
 */

// @lc code=start

/**
 * Two methods
 * 1. Process two strings to get rid of # (using left & right ptr), then compare
 * 2. Read both strings backwards to compare without editing
 */
class Solution {
   public:
    // if s[i] is not #, return s[i]
    // if s[i] is #, return last undeleted char
    int findValidCharIndex(string s, int i) {
        if (i < 0) return -1;
        int count = 0;
        while (i >= 0) {
            count = s[i] == '#' ? count + 1 : count - 1;
            if (count < 0) break;
            if (--i >= 0 && count == 0 && s[i] != '#')
                break;
        }
        return i;
    }

    bool backspaceCompare(string s, string t) {
        int si = s.size() - 1, ti = t.size() - 1;

        si = findValidCharIndex(s, si);
        ti = findValidCharIndex(t, ti);

        while (si >= 0 && ti >= 0) {
            if (s[si] != t[ti])
                return false;
            si = findValidCharIndex(s, --si);
            ti = findValidCharIndex(t, --ti);
        }

        si = findValidCharIndex(s, si);
        ti = findValidCharIndex(t, ti);

        return (si < 0 && ti < 0);
    }
};
// @lc code=end
