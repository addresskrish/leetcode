class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        maximum=-1
        for i in range (0,len(nums)-1):
            for j in range (i+1,len(nums)) : 
                if(nums[j]- nums[i]> maximum and nums[j] > nums[i] ):
                    maximum=nums[j]-nums[i]
        return maximum