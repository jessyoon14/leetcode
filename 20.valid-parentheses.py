#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    # same solution but cleaner
    def isValid(self, s: str) -> bool:
        pair = {')': '(', '}': '{', ']': '['}
        open_par = set(['(', '{', '['])
        stack = []
        for c in s:
            if c in open_par:
                stack.append(c)
            elif stack and stack[-1] == pair[c]:
                stack.pop()
            else:
                return False
        return len(stack) == 0

    def isValid(self, s: str) -> bool:
        chars = []
        pairs = {')': '(', '}': '{', ']': '['}
        for c in s:
            # check curr char, if closing, check last char
            if c == '(' or c == '{' or c == '[':
                chars.append(c)
            else:
                pair = pairs[c]
                if len(chars) > 0 and chars[-1] == pair:
                    chars.pop()
                else:
                    return False
        return len(chars) == 0

    def isValid(self, s: str) -> bool:
        pair = {')': '(', '}': '{', ']': '['}
        stack = []
        for c in s:
            # closing
            if c in pair:
                if len(stack) == 0 or stack.pop() != pair[c]:
                    return False
            # opening
            else:
                stack.append(c)
        return len(stack) == 0

# @lc code=end
