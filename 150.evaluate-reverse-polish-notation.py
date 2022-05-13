#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
class Solution:
    """
    In-place list modification, with lambda functions
    Time complexity: O(n^2) -> can be implemented with linked-list to get O(n) (but this impl. is much more difficult)
    Space complexity: O(1)
    """
#     def evalRPN(self, tokens: List[str]) -> int:
#         operations = {
#             '+': lambda a, b: a + b,
#             '-': lambda a, b: a - b,
#             '/': lambda a, b: int(a/b),
#             '*': lambda a, b: a * b
#         }
#         current_position = 0

#         while len(tokens) > 1:
#             while tokens[current_position] not in '+-*/':
#                 current_position += 1

#             operator = tokens[current_position]
#             number_1 = int(tokens[current_position - 2])
#             number_2 = int(tokens[current_position - 1])

#             operation = operations[operator]
#             tokens[current_position] = operation(number_1, number_2)

#             tokens.pop(current_position - 2) # need to move the n elements after current_position -> O(n)
#             tokens.pop(current_position - 2)
#             current_position -= 1
#         return tokens[0]

    """
    Better stack solution
    Time complexity: O(n)
    Space complexity: O(n)
    """

    def evalRPN(self, tokens: List[str]) -> int:
        operations = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: - (abs(a) // abs(b)) if a*b < 0 else a // b
        }

        stack = []
        n = len(tokens)

        for i in range(n):
            if tokens[i] in operations:
                # pop two elements from stack and add result
                operation = operations[tokens[i]]
                right_operand = stack.pop()
                left_operand = stack.pop()
                stack.append(operation(left_operand, right_operand))
            else:
                stack.append(int(tokens[i]))
        return stack[0]

    """
    Stack solution
    Time complexity: O(n)
    Space complexity: O(n)
    """
#     def evalRPN(self, tokens: List[str]) -> int:
#         def operate(operation, left, right):
#             if operation == '+':
#                 return left + right
#             elif operation == '-':
#                 return left - right
#             elif operation == '*':
#                 return left * right
#             else:
#                 if left * right < 0 :
#                     return - (abs(left) // abs(right))
#                 else:
#                     return left // right # check rounding

#         stack = [tokens[-1]]
#         n = len(tokens)
#         ops = ('+', '-', '*', '/')

#         for i in range(n-2, -1, -1):
#             c = tokens[i]
#             while stack and c not in ops and stack[-1] not in ops:
#                 right_operand = stack.pop()
#                 op = stack.pop()
#                 c = operate(op, int(c), int(right_operand))
#             stack.append(c)
#         return stack[0]

    """
    Recursive solution
    Time complexity: O(n)
    Space complexity: O(n)
    """
#     def evalRPN(self, tokens: List[str]) -> int:
#         def evaluate(left, right):
#             if left == right:
#                 return int(tokens[left])
#             split = find_split(left, right) # start index of right operand
#             left_operand = evaluate(left, split - 1)
#             right_operand = evaluate(split, right - 1)
#             return op(tokens[right], left_operand, right_operand)


#         def find_split(left, right):
#             operand_count = 2
#             for i in range(right - 1, left, -1):
#                 operand_count -= 1
#                 if tokens[i] in ('+', '-', '*', '/'):
#                     operand_count += 2
#                 if operand_count == 1:
#                     return i

#         def op(operation, left, right):
#             if operation == '+':
#                 return left + right
#             elif operation == '-':
#                 return left - right
#             elif operation == '*':
#                 return left * right
#             else:
#                 if left * right < 0 :
#                     return - (abs(left) // abs(right))
#                 else:
#                     return left // right # check rounding

#         return evaluate(0, len(tokens) - 1)
# @lc code=end
