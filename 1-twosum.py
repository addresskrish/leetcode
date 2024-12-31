# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:

#         n = len(nums)
#         for i in range(n - 1) :
#             for x in range(i + 1, n) :
#                 if nums[i] + nums[x] == target :
#                     return i, x