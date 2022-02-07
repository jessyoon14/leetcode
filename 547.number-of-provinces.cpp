/*
 * @lc app=leetcode id=547 lang=cpp
 *
 * [547] Number of Provinces
 */

// @lc code=start
class Solution {
   public:
    int findCircleNum(vector<vector<int>>& isConnected) {
        int size = isConnected.size();
        queue<int> next;
        int count = 0;
        int curr = 0;

        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                if (isConnected[i][j] > 0) {
                    count++;
                    next.push(i);
                    next.push(j);
                    isConnected[i][j] = 0;
                    isConnected[j][i] = 0;

                    while (!next.empty()) {
                        curr = next.front();
                        next.pop();
                        for (int k = 0; k < size; k++) {
                            if (isConnected[curr][k] > 0) {
                                next.push(k);
                                isConnected[curr][k] = 0;
                                isConnected[k][curr] = 0;
                            }
                        }
                    }

                    break;
                }
            }
        }

        return count;
    }
};
// @lc code=end

// https://leetcode.com/problems/number-of-provinces/discuss/101354/C%2B%2B-Clean-Code-DFSorUnionFind
// DFS

class Solution {
   public:
    int findCircleNum(vector<vector<int>>& M) {
        if (M.empty()) return 0;
        int n = M.size();
        vector<bool> visited(n, false);
        int groups = 0;
        for (int i = 0; i < visited.size(); i++) {
            groups += !visited[i] ? dfs(i, M, visited), 1 : 0;
        }
        return groups;
    }

   private:
    void dfs(int i, vector<vector<int>>& M, vector<bool>& visited) {
        visited[i] = true;
        for (int j = 0; j < visited.size(); j++) {
            if (i != j && M[i][j] && !visited[j]) {
                dfs(j, M, visited);
            }
        }
    }
};

// UnionFind

class Solution {
   public:
    int findCircleNum(vector<vector<int>>& M) {
        if (M.empty()) return 0;
        int n = M.size();

        vector<int> leads(n, 0);
        for (int i = 0; i < n; i++) {
            leads[i] = i;
        }  // initialize leads for every kid as themselves

        int groups = n;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {  // avoid recalculate M[i][j], M[j][i]
                if (M[i][j]) {
                    int lead1 = find(i, leads);
                    int lead2 = find(j, leads);
                    if (lead1 != lead2) {  // if 2 group belongs 2 different leads, merge 2 group to 1
                        leads[lead1] = lead2;
                        groups--;
                    }
                }
            }
        }
        return groups;
    }

   private:
    int find(int x, vector<int>& parents) {
        return parents[x] == x ? x : find(parents[x], parents);
    }
};