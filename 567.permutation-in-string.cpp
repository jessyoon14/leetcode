/*
 * @lc app=leetcode id=567 lang=cpp
 *
 * [567] Permutation in String
 */

// @lc code=start
class Solution
{
public:
    bool checkInclusion(string s1, string s2)
    {
        if (s2.length() < s1.length())
            return false;

        array<int, 26> s1CharCount{};
        array<int, 26> windowCharCount{};

        for (int i = 0; i < s1.length(); i++)
        {
            s1CharCount[s1[i] - 97]++;
            windowCharCount[s2[i] - 97]++;
        }

        for (int i = s1.length(); i < s2.length(); i++)
        {
            if (windowCharCount == s1CharCount)
                return true;

            int leftChar = s2[i - s1.length()];
            windowCharCount[leftChar - 97]--;
            int rightChar = s2[i];
            windowCharCount[rightChar - 97]++;
        }

        return windowCharCount == s1CharCount;
    }
};
// @lc code=end
