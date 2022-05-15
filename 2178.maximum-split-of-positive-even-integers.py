"""
unique positive even integers
12 => 2, 4, 6 (3 ints)

edge cases
- only one sum: 2, 4
- sum of consecutive
- sum of nonconsecutive
- sum of varying lengths
- no answer (-, 0, odd)

28: 2, 4, 6, 16


must start from 2

search: 2, 4, 6, ...

if current sum goes over?
4: 2 -> upgrade last elem to 4
6: 2, 4
8: 2, 4 -> upgrade last elem to target - current_sum

-> O(n)
1) keep track of current elements in stack
    - add even numbers from 2
    - if sum goes over, set last element equal to target - current sum
2) calculate sum of even numbers, find max sum of even numbers that's under target, and upgrade largest number

28
stack: [2, 4, 6, 28 - 12 = 16]
curr_sum: 2 + 4 + 6 
"""

class Solution:
    """
    Greedy -> can improve to log n with binary search approach
    Time = O(sqrt(x)) -> # elements in answer
    Space = O(sqrt(x)) -> # elements in answer
    """
#     def maximumEvenSplit(self, finalSum: int) -> List[int]:
#         if finalSum < 2 or finalSum % 2 == 1:
#             return []
        
#         stack = []
#         i = 2
#         curr_sum = 0
#         while curr_sum + i <= finalSum:
#             stack.append(i)
#             curr_sum += i
#             i += 2
            
#         # fix last element
#         curr_sum -= stack.pop()
#         stack.append(finalSum - curr_sum)
        
#         return stack


    """
    Greedy, but starting from largest element
    """
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        ans, i = [], 2
        if finalSum % 2 == 0:
            while i <= finalSum:
                ans.append(i)
                finalSum -= i
                i += 2
            ans[-1] += finalSum
        return ans