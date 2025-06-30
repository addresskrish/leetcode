class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counts = sorted(Counter(nums).items())
        res = 0
        for i in range(len(counts) - 1):
            if counts[i + 1][0] == counts[i][0] + 1:
                res = max(res, counts[i][1] + counts[i + 1][1])
        return res