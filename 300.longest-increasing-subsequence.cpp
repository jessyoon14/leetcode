/*
 * @lc app=leetcode id=300 lang=cpp
 *
 * [300] Longest Increasing Subsequence
 */

// @lc code=start
class Solution {
   public:
    int lengthOfLIS(vector<int>& nums) {
        int seqLengths[nums.size()];
        fill_n(seqLengths, nums.size(), 1);
        int maxSeqLength = 1;

        for (int i = 1; i < nums.size(); i++) {
            for (int j = i - 1; j >= 0; j--) {
                if (nums[j] < nums[i] && seqLengths[i] < seqLengths[j] + 1) {
                    seqLengths[i] = seqLengths[j] + 1;
                    maxSeqLength = max(seqLengths[i], maxSeqLength);
                }
            }
        }

        return maxSeqLength;
    }
};
// @lc code=end
