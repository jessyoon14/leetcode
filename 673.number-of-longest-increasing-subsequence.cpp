/*
 * @lc app=leetcode id=673 lang=cpp
 *
 * [673] Number of Longest Increasing Subsequence
 */

// @lc code=start
class Solution {
   public:
    int findNumberOfLIS(vector<int>& nums) {
        int seqLengths[nums.size()];
        fill_n(seqLengths, nums.size(), 1);
        int seqCounts[nums.size()];
        fill_n(seqCounts, nums.size(), 1);

        int maxSeqLength = 1;
        int maxSeqCount = nums.size();

        for (int i = 1; i < nums.size(); i++) {
            for (int j = i - 1; j >= 0; j--) {
                // update sequence length
                if (nums[j] < nums[i] && seqLengths[i] < seqLengths[j] + 1) {
                    seqLengths[i] = seqLengths[j] + 1;
                    seqCounts[i] = seqCounts[j];

                    if (seqLengths[i] > maxSeqLength) {
                        maxSeqLength = seqLengths[i];
                        maxSeqCount = seqCounts[i];
                    } else if (seqLengths[i] == maxSeqLength) {
                        maxSeqCount += seqCounts[j];
                    }

                }
                // update sequence count
                else if (nums[j] < nums[i] && seqLengths[i] == seqLengths[j] + 1) {
                    seqCounts[i] += seqCounts[j];

                    if (seqLengths[i] == maxSeqLength) {
                        maxSeqCount += seqCounts[j];
                    }
                }
            }
        }
        return maxSeqCount;
    }
};
// @lc code=end
