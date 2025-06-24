class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        seen = [0] * len(nums)
        for i in range(len(nums)) :
            if nums[i] == key :
                for j in range(0,k+1) :
                    if j > len(nums) or j < 0 :
                        continue
                    if(i-j>=0):
                        seen[i-j] = 1
                    if(i+j<len(nums)):
                        seen[i+j]=1
        result = []
        for i in range(len(nums)) :
            if seen[i] == 1 :
                result.append(i)
        return result