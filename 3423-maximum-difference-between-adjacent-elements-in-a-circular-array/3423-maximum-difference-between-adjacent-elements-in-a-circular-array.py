class Solution:
    def maxAdjacentDistance(self, a: List[int]) -> int:
        return max(abs(v-u) for v,u in pairwise(a+a))