class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        s=0
        i=0
        while i<len(nums)-1:
            h=nums[i]+k
            for j in range (i+1,len(nums)):
                if nums[j]>h:
                    i=j
                    s+=1
                    break
            else:
                break
        return s+1