class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #Brutforce approch
        # n = len(nums)
        # for i in range(n) :
        #     for x in range(i + 1, n) :
        #         if nums[i] == nums[x] :
        #             return True
        # return False

        #Sorting approch
        # n = len(nums)
        # nums.sort()
        # for i in range(1, n) :
        #     if nums[i] == nums[i - 1] :
        #         return True 
        # return False

        #Hashset approch
        seen = set()
        for num in nums :
            if num in seen :
                return True
            seen.add(num)
        return False