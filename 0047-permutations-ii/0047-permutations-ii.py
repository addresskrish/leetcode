class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort() 
        used = [False] * len(nums)

        def backtrack(pat):
            if len(pat) == len(nums):
                res.append(pat[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue 
                used[i] = True
                pat.append(nums[i])
                backtrack(pat)
                used[i] = False
                pat.pop()

        backtrack([])
        return res
