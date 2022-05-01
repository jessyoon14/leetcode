#
# @lc app=leetcode id=43 lang=python3
#
# [43] Multiply Strings
#

# @lc code=start
class Solution:
    """
    나머지 솔루션도 있는데... 이 문제는 마음에 들지 않아..
    """

    """
    Elementary math
    """

    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'

        first_number = nums1[::-1]
        second_number = nums2[::-1]

        result = []
        for index, digit in enumerate(second_number):
            results.append(self.multiply_one_digit(digit, index, first_number))

        answer = self.sum_results(results)

        return ''.join(str(digit) for digit in reversed(answer))

    def multiply_one_digit(self, digit2, num_zeros, first_number):
        current_result = [0] * num_zeros
        carry = 0

        for digit1 in first_number:
            multiplication = int(digit1) * int(digit2) + carry
            carry = multiplication // 10
            current_result.append(multiplication % 10)
        if carry != 0:
            current_result.append(carry)
        return current_result

    def sum_results(self, results):
        answer = results.pop()

        for result in results:
            new_answer = []
            carry = 0
            for digit1, digit2 in zip_longest(result, answer, fillvalue=0):
                curr_sum = digit1 + digit2 + carry
                carry = curr_sum//10
                new_answer.append(curr_sum % 10)

            if carry != 0:
                new_answer.append(carry)
            answer = new_answer
        return answer

    """
    Methods
    1. recursion
        time complexity: n(log(m) + log(n))
    2. Process digit by digit
    
    
    # edge cases
    - n * 0
    - n * n with carry
    - negative (if exists)
    """

    def multiply(self, num1: str, num2: str) -> str:
        if num1[0] == '0' or num2[0] == '0':
            return '0'

        def rec(n1, n2):
            if len(n2) > len(n1):
                n1, n2 = n2, n1
            if not n1 or not n2:
                return ''
            if len(n1) == 1 and len(n2) == 1:
                return str(int(n1) * int(n2))
            ans1 = rec(n1[:len(n1)//2], n2) + '0' * ((len(n1) + 1)//2)
            ans2 = rec(n1[len(n1)//2:], n2)
            return string_add(ans1, ans2)

        def string_add(s1, s2):
            if len(s2) > len(s1):
                s1, s2 = s2, s1
            result = ''
            i1, i2 = len(s1) - 1, len(s2) - 1
            carry = 0
            while i1 > -1 and i2 > -1:
                curr = int(s1[i1]) + int(s2[i2]) + carry
                result += str(curr % 10)
                if curr >= 10:
                    carry = 1
                else:
                    carry = 0
                i1 -= 1
                i2 -= 1

            while i1 > -1:
                curr = int(s1[i1]) + carry
                result += str(curr % 10)
                if curr >= 10:
                    carry = 1
                else:
                    carry = 0
                i1 -= 1

            if carry:
                result += '1'
            return result[::-1]

        return rec(num1, num2)


# @lc code=end
