/*
 * @lc app=leetcode id=986 lang=cpp
 *
 * [986] Interval List Intersections
 */

// @lc code=start
class Solution {
   public:
    vector<vector<int>> intervalIntersection(vector<vector<int>>& firstList, vector<vector<int>>& secondList) {
        int s1 = firstList.size(), s2 = secondList.size();
        if (s1 == 0 || s2 == 0) return {};
        vector<vector<int>> res;
        int i1 = 0, i2 = 0;

        vector<int> interval1;
        vector<int> interval2;
        while (i1 < s1 && i2 < s2) {
            interval1 = firstList[i1];
            interval2 = secondList[i2];
            int start = max(interval1[0], interval2[0]);
            int end = min(interval1[1], interval2[1]);
            if (start <= end)
                res.push_back({start, end});
            if (end == interval1[1])
                i1++;
            else
                i2++;
        }
        return res;
    }
};
// @lc code=end
