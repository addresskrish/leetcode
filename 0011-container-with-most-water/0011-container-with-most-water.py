class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1
        if height[l] == height[r] and r == 1:
            return height[l]

        while l < r :
            area = (r - 1) * min(height[l], height[r])
            res = max(res, area)
            
            if height[l] < height[r] :
                l += 1
            else :
                r -= 1
        return res