class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp=[0,0]
        for i in range(1,len(prices)):
            grow=prices[i]-prices[i-1]
            dp[0],dp[1]=max(dp[0],dp[1]+grow-fee),max(dp[0],dp[1]+grow)
        return dp[0]