#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    """
    Stack -> 이걸로 꼭 다시 풀어보기!!!!!
    Time complexity: O(n)
    Space complexity: O(n)
    """
    # def trap(self, height: List[int]) -> int:
    #     ans, curr = 0, 0
    #     stack = []
    #     n = len(height)
    #     for curr in range(n):
    #         while stack and height[curr] > height[stack[-1]]:
    #             top = stack.pop()
    #             if not stack:
    #                 break
    #             distance = curr - stack[-1] - 1
    #             bounded_height = min(height[curr], height[stack[-1]]) - height[top]
    #             ans += distance * bounded_hegiht
    #         stack.push(curr)
    #     return ans

    """
    Two pointers
    Time complexity: O(n)
    Space complexity: O(1)
    """

    def trap(self, height: List[int]) -> int:
        n = len(height)
        left, right = 0, n - 1
        left_max, right_max = 0, 0
        ans = 0
        while left < right:
            if height[left] < height[right]:  # update left pointer
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    ans += left_max - height[left]
                left += 1
            else:  # update right pointer
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    ans += right_max - height[right]
                right -= 1
        return ans

    """
    Brute force:
    For each bar, find the max water if can trap above, 
    by finding max left bar and max right bar
    Time complexity: O(n^2)
    Space complexity: O(1)
    """
#     def trap(self, height: List[int]) -> int:
#         result = 0
#         n = len(height)
#         for i in range(n):
#             left_max = 0
#             right_max = 0

#             for j in range(i+1):
#                 left_max = max(left_max, height[j])
#             for j in range(i, n):
#                 right_max = max(right_max, height[j])
#             result += min(left_max, right_max) - height[i]
#         return result

    """
    Dynamic Programming
    Optimize brute force by storing left_max and right_max as dp
    Time complexity: O(n)
    Space complexity: O(n)
    """
#     def trap(self, height: List[int]) -> int:
#         if not height:
#             return 0

#         n = len(height)
#         left_max, right_max = [0] * n, [0] * n
#         left_max[0], right_max[-1] = height[0], height[-1]

#         for i in range(1, n):
#             left_max[i] = max(height[i], left_max[i-1])
#             right_max[n-1-i] = max(height[n-1-i], right_max[n-i])

#         result = 0
#         for i in range(n):
#             result += min(left_max[i], right_max[i]) - height[i]

#         return result

    """
    Recursive solution
    Time complexity: O(n)
    Space complexity: O(n) worst case, O(log n) average
    """
#     def trap(self, height: List[int]) -> int:
#         def rec (l, r): # return rainwater between l and r
#             # find max_idx
#             if l >= r - 1:
#                 return 0
#             max_val = max(height[l+1:r])
#             if max_val > height[l] or max_val > height[r]:
#                 max_idx = height.index(max_val, l+1, r)
#                 return rec(l, max_idx) + rec(max_idx, r)
#             else:
#                 area = min(height[l], height[r]) * (r - l - 1)
#                 # subtract bar space
#                 for i in range(l+1, r):
#                     area -= height[i]
#                 return area


#         return rec(0, len(height) - 1)

# @lc code=end
