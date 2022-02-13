/*
 * @lc app=leetcode id=213 lang=cpp
 *
 * [213] House Robber II
 */

// @lc code=start
class Solution {
   private:
    int robFrom(vector<int>& nums, int from, int to) {
        if (from == to) return nums[from];
        int prev = 0, curr = 0, temp = 0;
        for (int i = from; i < to + 1; i++) {
            temp = curr;
            curr = max(prev + nums[i], curr);
            prev = temp;
        }
        return curr;
    }

   public:
    int rob(vector<int>& nums) {
        int size = nums.size();
        if (size < 2) return nums[0];

        // case 1: house 0 ~ house n-2
        // case 2: house 1 ~ house n-1
        return max(robFrom(nums, 0, size - 2), robFrom(nums, 1, size - 1));
    }
};
// @lc code=end

// class Solution {
//    public:
//     int rob(vector<int>& nums) {
//         int size = nums.size();

//         if (size == 1) return nums[0];
//         if (size == 2) return max(nums[0], nums[1]);

//         int with_first[size];     // case 1: house 0 ~ house n - 2
//         int without_first[size];  // case 2: house 1 ~ house n - 1

//         with_first[0] = nums[0];
//         with_first[1] = max(nums[0], nums[1]);
//         without_first[1] = nums[1];
//         without_first[2] = max(nums[1], nums[2]);

//         for (int i = 2; i < size - 1; i++) {
//             with_first[i] = max(with_first[i - 2] + nums[i], with_first[i - 1]);
//             without_first[i + 1] = max(without_first[i - 1] + nums[i + 1], without_first[i]);
//         }

//         return max(with_first[size - 2], without_first[size - 1]);
//     }
// };
