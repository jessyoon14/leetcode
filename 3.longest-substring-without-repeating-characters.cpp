/*
 * @lc app=leetcode id=3 lang=cpp
 *
 * [3] Longest Substring Without Repeating Characters
 */

// @lc code=start
class Solution
{
public:
    int lengthOfLongestSubstring(string s)
    {

        // index of character occuring in this substring
        int DEFAULT = -1;
        int indices[128] = {};
        for (int i = 0; i < 128; i++)
        {
            indices[i] = -1;
        }

        int maxLength = 0;
        int currLength = 0;

        for (int i = 0; i < s.length(); i++)
        {
            int curr = s[i];
            // printf("currLength: %i, maxLength: %i, indices[curr]: %i \n", currLength, maxLength, indices[curr]);

            // first occurence in current substring
            if (indices[curr] == DEFAULT)
            {
                // printf("first occurence\n");
                indices[curr] = i;
                currLength++;
            }
            // second occurence in current substring, reset
            else
            {
                // printf("second occurence\n");
                maxLength = maxLength > currLength ? maxLength : currLength;
                int old_index = indices[curr];
                int startWindow = indices[curr];
                indices[curr] = i;
                for (int j = 0; j < 128; j++)
                {
                    if (indices[j] > DEFAULT && indices[j] < startWindow)
                    {
                        indices[j] = DEFAULT;
                        currLength--;
                    }
                }
            }
        }

        return maxLength > currLength ? maxLength : currLength;
    }
};
// @lc code=end
