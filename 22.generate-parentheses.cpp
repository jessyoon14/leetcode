/*
 * @lc app=leetcode id=22 lang=cpp
 *
 * [22] Generate Parentheses
 */

// @lc code=start
class Solution {
   public:
    vector<string> generateParenthesis(int n) {
        vector<pair<string, int>> strings = {{"(", 0}};

        string s;
        int open_count;
        int close_count;
        int strings_size;

        for (int k = 1; k < 2 * n; k++) {
            strings_size = strings.size();
            for (int i = 0; i < strings_size; i++) {
                s = strings.front().first;
                close_count = strings.front().second;
                strings.erase(strings.begin());
                open_count = s.size() - close_count;

                if (open_count < n)
                    strings.push_back({s + "(", close_count});

                if (open_count > close_count)
                    strings.push_back({s + ")", close_count + 1});
            }
        }

        vector<string> result;
        for (pair<string, int> p : strings) {
            result.push_back(p.first);
        }

        return result;
    }
};
// @lc code=end

class Solution {
   public:
    vector<string> generateParenthesis(int n) {
        vector<string> result;

        if (n == 0)
            result.push_back("");
        else {
            for (int c = 0; c < n; ++c) {
                for (string left : generateParenthesis(c))
                    for (string right : generateParenthesis(n - 1 - c))
                        result.push_back("(" + left + ")" + right);
            }
        }
    }
};

/*
class Solution {
   public:
    vector<string> generateParenthesis(int n) {
        vector<string> result = {"()"};
        if (n == 1) return result;
        vector<string> prev = generateParenthesis(n - 1);

        for (int i = 0; i < prev.size(); i++) {
            string s = prev[i];
            result.push_back("()" + s);
            result.push_back("(" + s +)

        }



        for (int i = 1; i < n; i++) {
            // printf("i: %i\n", i);
            int result_size = result.size();
            for (int j = 0; j < result_size; j++) {
                // printf("j: %i\n", j);
                string curr = result.front();

                // printf("curr: %s\n", curr.c_str());
                result.erase(result.begin());

                result.push_back("()" + curr);

                result.push_back("(" + curr + ")");

                // printf("%s\n", ("(" + curr + ")").c_str());
                // printf("%s\n", ("()" + curr).c_str());

                if (j > 0) {
                    result.push_back(curr + "()");
                    // printf("%s\n", (curr + "()").c_str());
                }
            }
        }

        return result;
    }
};

*/