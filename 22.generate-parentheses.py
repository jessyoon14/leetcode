#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:

    """
    Brute force: create all possible strings and check if well-formed
    Time complexity: O(2^2n * n)
    Space complexity: O(2^n * n + n)
    """
#     def generateParenthesis(self, n: int) -> List[str]:
#         def generate(acc):
#             if len(acc) == 2 * n:
#                 if valid(acc):
#                     ans.append(''.join(acc))
#             else:
#                 acc.append('(')
#                 generate(acc)
#                 acc.pop()
#                 acc.append(')')
#                 generate(acc)
#                 acc.pop()
#         def valid(acc):
#             bal = 0
#             for c in acc:
#                 if c == '(':
#                     bal += 1
#                 else:
#                     bal -= 1
#                 if bal < 0:
#                     return False
#             return bal == 0

#         ans = []
#         generate([])
#         return ans

    """
    Closure Number
    """

    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return ['']
        ans = []
        for c in range(n):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(n-1-c):
                    ans.append('({}){}'.format(left, right))
        return ans

    """
    Brute force: create all possible strings and check if well-formed
    Time complexity: O(2^n)
    Space complexity: O(2^n * n + n ^ 2)
    """
#     def generateParenthesis(self, n: int) -> List[str]:
#         results = []

#         def rec(s, open_count, close_count):
#             if open_count < close_count or open_count > n:
#                 return
#             if len(s) == n * 2:
#                 results.append(s)
#                 return

#             rec(s + '(', open_count + 1, close_count)
#             rec(s + ')', open_count, close_count + 1)

#         rec('', 0, 0)
#         return results

    """
    Backtracking (Stack)
    Time complexity: O(# results * n) -> # 
    Space complexity: O(# results * n + n)
    """
#     def generateParenthesis(self, n: int) -> List[str]:
#         results = []
#         stack = []
#         final_len = 2 * n
#         def build(open_count, close_count):
#             if len(stack) == final_len:
#                 results.append(''.join(stack))
#                 return
#             if open_count - close_count > 0:
#                 stack.append(')')
#                 build(open_count, close_count + 1)
#                 stack.pop()
#             if open_count < n:
#                 stack.append('(')
#                 build(open_count + 1, close_count)
#                 stack.pop()

#         build(0, 0)
#         return results


# @lc code=end
