/*
 * @lc app=leetcode id=130 lang=cpp
 *
 * [130] Surrounded Regions
 */

// @lc code=start
class Solution {
   private:
    int h, w;
    const int step[4][2] = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
    void dfs(vector<vector<char>>& board, int i, int j) {
        board[i][j] = 'O';
        const bool edge[4] = {i == 0, j == w - 1, i == h - 1, j == 0};

        for (int k = 0; k < 4; k++) {
            int y = i + step[k][0];
            int x = j + step[k][1];

            if (!edge[k] && board[y][x] == 'N')
                dfs(board, y, x);
        }
    }

   public:
    void solve(vector<vector<char>>& board) {
        // set all 'O' to 'N'
        h = board.size();
        w = board[0].size();

        for (int i = 0; i < h; i++) {
            for (int j = 0; j < w; j++) {
                if (board[i][j] == 'O')
                    board[i][j] = 'N';
            }
        }

        // look around edge, mark 'N' to 'O'
        for (int i = 0; i < h; i++) {
            if (board[i][0] == 'N')
                dfs(board, i, 0);
            if (board[i][w - 1] == 'N')
                dfs(board, i, w - 1);
        }

        for (int j = 0; j < w; j++) {
            if (board[0][j] == 'N')
                dfs(board, 0, j);
            if (board[h - 1][j] == 'N')
                dfs(board, h - 1, j);
        }

        // traverse and mark 'N' to 'X'
        for (int i = 0; i < h; i++) {
            for (int j = 0; j < w; j++) {
                if (board[i][j] == 'N')
                    board[i][j] = 'X';
            }
        }
    }
};
// @lc code=end
