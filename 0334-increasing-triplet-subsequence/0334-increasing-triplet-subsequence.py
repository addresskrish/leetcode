class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        
        first = float('inf')
        second = float('inf')
        
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
            
        return False