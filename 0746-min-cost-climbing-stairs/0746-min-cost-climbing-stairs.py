class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev1 , prev2 = cost[0], cost[1]
        for j in range(2,len(cost)):
            curr = min(prev1, prev2) + cost[j]
            prev1,prev2 = prev2,curr
        return min(prev1, prev2)