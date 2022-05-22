'''
1. Brute force: backtracking (build all possible parentheses strings of size 2n, then filter out the invalid ones)
2. Optimized backtracking: only build valid parentheses 
    time: O(2^n) (size of output)
    space: O(2^n) (size of output)

f(acc, open_count, close_count): 
    if open count > close count: f(acc + ')', open_count, close_count + 1)
    if open count < max open count: f(acc + '(', open_count + 1, close_count)
base case:
    open count == close count == n

3. Base case and build
n = 1: ()
n = 2: ( 1 ) 2
n = 3: ( 1 ) 2

Edge cases
- n = 0, 1, ..., k
'''

from typing import List

'''
My solution: build
time : O(2^n)
space: O(2^n + n^2) -> could be optimized to 2^n + n with stack
'''


def build_parens(n: int) -> List[str]:
    def rec(acc, open_count, close_count):
        if open_count == n and close_count == n:
            result.append(acc)
            return
        if open_count > close_count:
            rec(acc + ')', open_count, close_count + 1)
        if open_count < n:
            rec(acc + '(', open_count + 1, close_count)

    result = []
    rec('', 0, 0)
    return result


if __name__ == '__main__':
    print(build_parens(3))
