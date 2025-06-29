class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        mod = 10**9 + 7
        nums.sort()
        n = len(nums)

        res = 0
        l, r = 0, n - 1

        while l <= r:
            if nums[l] + nums[r] <= target:
                res = res + pow(2, r - l, mod)
                res = res % mod
                l += 1
            else:
                r -= 1
        return res