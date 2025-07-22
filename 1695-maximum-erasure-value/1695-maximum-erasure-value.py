class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l=0
        r=0
        s=0
        m=0
        d=defaultdict(int)
        while r<len(nums) and l<=r:
            
            if not d[nums[r]]:
                d[nums[r]]=1
                s+=nums[r]
                r+=1
            elif d[nums[r]]==1:
        
                m=max(m,s)
                while nums[l]!=nums[r]:
                    d[nums[l]]-=1
                    s-=nums[l]
                    l+=1
                s-=nums[1]
                d[nums[l]]-=1
                
                l+=1
                m=max(s,m)
        m=max(m,sum(nums[l:r]))
        return m