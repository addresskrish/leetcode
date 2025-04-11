class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        numToBeat = 1
        for num in nums:
            if num < 1:
                continue
            if num == numToBeat:
                numToBeat += 1
            elif num > numToBeat:
                return numToBeat
        return max(nums[-1] + 1, 1)