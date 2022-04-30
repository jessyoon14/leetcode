#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    """
    Best conceivable runtime: O(n^2)
    """
    """
    Brute force: generate all possible triplets
    """
    # skip

    """
    Hashset: O(n^2)
    
    """
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         result = []
#         nums.sort()
#         for i in range(len(nums)):
#             if nums[i] > 0:
#                 break
#             if i == 0 or nums[i] != nums[i-1]:
#                 self.find_triple(nums, i, result)
#         return result

#     def find_triple(self, nums, i, result): # find triple starting with element i
#         seen = set()
#         j = i + 1
#         while j < len(nums):
#             complement = 0 - nums[i] - nums[j]
#             if complement in seen:  # found triplet!
#                 result.append([nums[i], complement, nums[j]])
#                 while j + 1 < len(nums) and nums[j] == nums[j+1]:
#                     j += 1
#             seen.add(nums[j])
#             j += 1

    """
    Two pointers -> O(n^2)
    """
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         result = []
#         nums.sort()
#         for i in range(len(nums)):
#             if nums[i] > 0:
#                 break
#             if i == 0 or nums[i] != nums[i-1]:
#                 self.find_triple(nums, i, result)
#         return result

#     def find_triple(self, nums, i, result): # find triple starting with element i
#         target_sum = 0 - nums[i]
#         left, right = i + 1, len(nums) - 1
#         while left < right:
#             curr_sum = nums[left] + nums[right]
#             if curr_sum == target_sum:
#                 result.append([nums[i], nums[left], nums[right]])
#                 left += 1
#                 right -= 1
#                 while left < right and nums[left] == nums[left - 1]:
#                     left += 1
#             elif curr_sum < target_sum:
#                 left += 1
#             else:
#                 right -= 1

    """
    인터뷰에서는 중요하지 않음!!!!!
    No-sort: if can't modify input array / can't copy to sort because large size?
    Use HashSet, adapted for unsorted array (put triples in hashset, values in triple ordered)
    """

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        duplicates = set()
        seen = {}

        for i, val1 in enumerate(nums):
            if val1 not in duplicates:  # not seen yet
                duplicates.add(val1)
                for j, val2 in enumerate(nums[i+1:]):
                    complement = -val1 - val2
                    # i + 1 ~ j - 1 사이인 원소
                    if complement in seen and seen[complement] == i:
                        result.add(tuple(sorted((val1, val2, complement))))
                    seen[val2] = i  # val2를 마지막으로 확인한 건 i다
        return result

    """
    Failed attempt..
    Sort
    [-1,0,1,2,-1,-4]
    [-4, -1, -1, 0, 1, 2]
    Two pointer + binary search
    For two pointer:
        update pointer (until element with different value) for the element with greater absolute value
    For binary search:
        search for 0 - a - b in the range [left + 1], [right + 1]
    """
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         def binary_search(left: int, right: int, target: int) -> bool:
#             while left <= right:
#                 mid = (left + right) // 2
#                 if nums[mid] == target:
#                     return True
#                 elif target < nums[mid]:
#                     right = mid - 1
#                 else:
#                     left = mid + 1

#             return False


#         left = 0
#         right = len(nums) - 1
#         result = []
#         nums.sort()
#         prev_left = -1
#         while left + 1 < right:
#             # check current pair
#             mid_element = 0 - nums[left] - nums[right]
#             if binary_search(left + 1, right - 1, mid_element):
#                 result.append([nums[left], mid_element, nums[right]])
#             if prev_left >= 0:
#                 left = prev_left
#                 prev_left = -1
#                 while right > left and nums[right] == nums[right - 1]:
#                     right -= 1
#                 right -= 1
#                 continue
#             if -nums[left] == nums[right]:
#                 prev_left = left
#                 while left < right and nums[left] == nums[left + 1]:
#                     left += 1
#                 left += 1
#             elif -nums[left] > nums[right]:
#                 while left < right and nums[left] == nums[left + 1]:
#                     left += 1
#                 left += 1

#             else:
#                 while right > left and nums[right] == nums[right - 1]:
#                     right -= 1
#                 right -= 1
#         return result


# @lc code=end
