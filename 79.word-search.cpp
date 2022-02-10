/*
 * @lc app=leetcode id=79 lang=cpp
 *
 * [79] Word Search
 */

// @lc code=start
class Solution {
    int step[4][2] = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
    int h, w;

   private:
    bool check(vector<vector<char>>& board, string word, int i, int j) {
        if (word.empty()) return true;
        if (board[i][j] != word[0]) return false;
        if (word.size() == 1) return true;
        char c = board[i][j];
        board[i][j] = '.';

        for (int k = 0; k < 4; k++) {
            int y = i + step[k][0];
            int x = j + step[k][1];

            if (x > -1 && x < w && y > -1 && y < h) {
                if (check(board, word.substr(1), y, x)) return true;
            }
        }
        board[i][j] = c;
        return false;
    }

   public:
    bool exist(vector<vector<char>>& board, string word) {
        h = board.size();
        w = board[0].size();
        for (int i = 0; i < h; i++) {
            for (int j = 0; j < w; j++) {
                // if (board[i][j] == word[0])
                if (check(board, word, i, j))
                    return true;
            }
        }

        return false;
    }
};
// @lc code=end
