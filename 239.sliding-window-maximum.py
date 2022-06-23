#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#

# @lc code=start
class Solution:
    '''
    Brute force
    time O(n*k)
    space O(n - k + 1) for output array
    '''
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         if len(nums) < k:
#             return max(nums)

#         maxes = []
#         for i in range(len(nums) -  k + 1):
#             maxes.append(max(nums[i:i + k]))
#         return maxes

    '''
    Sliding window with queue
    left, right, max_idx
    
    Time O(N) -> every element is added /removed from queue 1 time
    Space O(N) -> O(N - k + 1) for output, O(k) for deque
    '''

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n * k == 0:
            return []
        if k == 1:
            return nums

        def clean_deque(i):
            # remove indices of elements outside sliding window
            if deq and deq[0] == i - k:
                deq.popleft()

            while deq and nums[i] > nums[deq[-1]]:
                deq.pop()

        # init
        deq = deque()
        max_idx = 0

        # process first number
        for i in range(k):
            clean_deque(i)
            deq.append(i)
            if nums[i] > nums[max_idx]:
                max_idx = i
        output = [nums[max_idx]]

        for i in range(k, n):
            clean_deque(i)
            deq.append(i)
            output.append(nums[deq[0]])

        return output

    '''
    Dynamic programming
    time O(N)
    space O(k)
    '''

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        # build left
        left = [float('-inf')] * n
        # build right
        right = [float('-inf')] * n

        curr_max = nums[0]

        for i in range(n):
            if i % k == 0:
                left[i] = nums[i]
            else:
                left[i] = max(left[i - 1], nums[i])

        for i in reversed(range(n)):
            if i == n - 1 or i % k == k - 1:
                right[i] = nums[i]
            else:
                right[i] = max(right[i + 1], nums[i])

        result = []
        for i in range(n - k + 1):
            result.append(max(right[i], left[i + k - 1]))

        return result


# @lc code=end
