class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        h = len(nums) - 1
        mini = float('inf')
        while l <= h:
            mid = (l + h) // 2
            if nums[l] < nums[h]:
                mini = min(mini, nums[l])
                return mini
            mini = min(mini, nums[l])
            if nums[l] <= nums[mid]:
                l = mid + 1
            else:
                h = mid
        if mini == float('inf'):
            return 1
        else:
            return mini
