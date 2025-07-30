class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        size = res = 0
        curr_max = 0
        for i in nums:
            if i>curr_max:
                res = 0
                size = 1
                curr_max = i
            elif i==curr_max:
                size+=1
            else:
                size = 0
            res = max(size,res)
        return res