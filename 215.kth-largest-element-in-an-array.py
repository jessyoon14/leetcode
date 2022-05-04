#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
class Solution:

    """
    Quicksort-based -> VIP
    Time complexity: O(n) average, O(n^2) worst case (if descending order or n same elements)
        -> to guarantee O(n) running time for most cases, shuffle the array order 
    Space complexity: O(1)
    """

    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(left, right, pivot_index):
            pivot = nums[pivot_index]
            # move pivot to end
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
            # move all smaller elements to the left
            store_index = left
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[store_index], nums[i] = nums[i], nums[store_index]
                    store_index += 1
            # move pivot to final place
            nums[right], nums[store_index] = nums[store_index], nums[right]
            return store_index

        def select(left, right, k_smallest):
            if left == right:
                return nums[left]

            pivot_index = random.randint(left, right)
            pivot_index = partition(left, right, pivot_index)
            if k_smallest == pivot_index:
                return nums[k_smallest]
            elif k_smallest < pivot_index:
                return select(left, pivot_index - 1, k_smallest)
            else:
                return select(pivot_index + 1, right, k_smallest)

        return select(0, len(nums) - 1, len(nums) - k)

    """
    Min Heap (only keep the k largest elements)
    Time complexity: O(n log k)
    Space complexity: O(k)
    """
#    def findKthLargest(self, nums: List[int], k: int) -> int:
    # by default, python is minheap -> use as maxheap by multiplying -1
#         heap = []
#         heapify(heap)

#         for n in nums:
#             heappush(heap, n)
#             if len(heap) > k:
#                 heappop(heap)

#         return heappop(heap)

    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     return heapq.nlargest(k, nums)[-1]

    """
    Trivial, sort
    Time complexity: O(n log n)
    Space complexity: O(n)
    """
    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     nums.sort(reverse=True)
    #     return nums[k-1]
# @lc code=end
