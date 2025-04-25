class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        prev = cnt = 0
        max = 0
        if 0 not in nums: return len(nums) - 1
        for i in range(len(nums)):
            if nums[i] == 1:
                cnt += 1
                if prev + cnt > max:
                    max = prev + cnt
            else:
                prev = cnt
                cnt = 0
        return max