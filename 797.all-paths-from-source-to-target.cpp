/*
 * @lc app=leetcode id=797 lang=cpp
 *
 * [797] All Paths From Source to Target
 */

// @lc code=start
class Solution {
   private:
    vector<vector<int>> result;
    int n;
    int target;

    void dfs(vector<vector<int>>& graph, vector<int> path) {
        int currNode = path.back();

        if (currNode == target) {
            result.push_back(path);
            return;
        }

        for (int i : graph[currNode]) {
            path.push_back(i);
            dfs(graph, path);
            path.pop_back();
        }
    }

   public:
    vector<vector<int>> allPathsSourceTarget(vector<vector<int>>& graph) {
        n = graph.size();
        target = n - 1;

        for (int i : graph[0]) {
            dfs(graph, {0, i});
        }

        return result;
    }
};
// @lc code=end
