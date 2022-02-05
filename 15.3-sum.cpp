/*
 * @lc app=leetcode id=15 lang=cpp
 *
 * [15] 3Sum
 */

// @lc code=start
class Solution {
   public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> result;

        if (nums.size() < 3)
            return {};

        sort(nums.begin(), nums.end());

        for (int i = 0; i < nums.size() - 2; i++) {
            while (i > 0 && i < nums.size() - 2 && nums[i - 1] == nums[i]) {
                i++;
            }

            int target = -nums[i];

            int l = i + 1;
            int r = nums.size() - 1;

            while (l < r) {
                int sum = nums[l] + nums[r];

                if (sum < target)
                    while (nums[++l] == nums[l - 1] && l < r) {
                    }

                else if (sum > target && r > l)
                    while (nums[--r] == nums[r + 1] && r > l) {
                    }

                else {
                    result.push_back(vector<int>{nums[i], nums[l], nums[r]});
                    while (nums[++l] == nums[l - 1] && l < r) {
                    }
                    while (nums[--r] == nums[r + 1] && r > l) {
                    }
                }
            }
        }

        return result;
    }
};

// @lc code=end

vector<vector<int>> threeSum(vector<int>& nums) {
    sort(nums.begin(), nums.end());
    int n = nums.size();
    vector<vector<int>> result;
    for (int i = 0; i < nums.size() - 2; i++) {
        if (i > 0 && nums[i - 1] == nums[i]) {
            continue;
        }

        int left = i + 1, right = n - 1;

        while (left < right) {
            int sum = nums[i] + nums[left] + nums[right];

            if (sum < 0)
                left++;
            else if (sum > 0)
                right--;
            else {
                result.push_back({nums[i], nums[left], nums[right]});
                while (left + 1 < right && nums[left] == nums[left + 1]) left++;
                while (left < right - 1 && nums[right] == nums[right - 1]) right--;
                left++;
                right++;
            }
        }
    }

    return result;
}

class Solution {
   public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> result;
        for (int i = 0; i < nums.size(); i++) {
            if (i > 0 && nums[i - 1] == nums[i]) {
                continue;
            }
            if (nums[i] > 0) break;
            for (int j = i + 1; j < nums.size(); j++) {
                for (int k = nums.size() - 1; k > j; k--) {
                    if (nums[i] + nums[j] + nums[k] == 0) {
                        vector<int> temp = {nums[i], nums[j], nums[k]};
                        if (result.size() == 0 || temp != result[result.size() - 1])
                            result.push_back(temp);
                        break;
                    }

                    if (nums[i] + nums[j] + nums[k] < 0)
                        break;
                }
            }
        }

        return result;
    }
};

class Solution {
   public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        if (nums.size() < 3) return {};

        vector<vector<int>> result;

        for (int i = 0; i < nums.size(); i++) {
            for (int j = i + 1; j < nums.size(); j++) {
                for (int k = j + 1; k < nums.size(); k++) {
                    if (nums[i] + nums[j] + nums[k] == 0) {
                        int a = max(nums[i], max(nums[j], nums[k]));
                        int c = min(nums[i], min(nums[j], nums[k]));
                        int b = 0 - a - c;

                        vector<int> temp = {a, b, c};
                        // printf("{%i, %i, %i}\n", a, b, c);

                        bool exists = false;
                        for (auto v : result) {
                            if (v == temp)
                                exists = true;
                        }
                        if (!exists)
                            result.push_back(temp);
                    }
                }
            }
        }

        return result;
    }
};
