/*
 * @lc app=leetcode id=62 lang=cpp
 *
 * [62] Unique Paths
 */

// @lc code=start
class Solution {
   public:
    int uniquePaths(int m, int n) {
        int paths[m][n];
        memset(paths, 0, sizeof(paths));

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (i == 0 || j == 0)
                    paths[i][j] = 1;
                else
                    paths[i][j] = paths[i - 1][j] + paths[i][j - 1];
            }
        }
        return paths[m - 1][n - 1];
    }
};
// @lc code=end
int uniquePaths(int m, int n) {
    if (m == 1 || n == 1) return 1;
    if (m < n) {
        int temp = m;
        m = n;
        n = temp;
    }

    long res = 1;
    int j = 1;
    for (int i = m + 1; i <= m + n; i++, j++) {
        res *= i;
        res /= j;
    }

    return (int)res;
}
/*
// Math solution: Need to arrange m D's and n R's
Total permutations = (m+n)! / (m! * n!)





Use two rows:
class Solution {
public:
    int uniquePaths(int m, int n) {
        vector<int> pre(n, 1), cur(n, 1);
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                cur[j] = pre[j] + cur[j - 1];
            }
            swap(pre, cur);
        }
        return pre[n - 1];
    }
};

// Use one row
class Solution {
public:
    int uniquePaths(int m, int n) {
        vector<int> cur(n, 1);
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                cur[j] += cur[j - 1];
            }
        }
        return cur[n - 1];
    }
};

*/
