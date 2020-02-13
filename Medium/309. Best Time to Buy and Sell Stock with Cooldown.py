class Solution:
    def maxProfit(self, prices: list) -> int:
        if len(prices) < 2: return 0
        
        day = len(prices)
        dp = [0] * day
        dp[1] = max(0, prices[1]-prices[0])
        money = max(-prices[0], -prices[1])
        
        for i in range(2, day):
            dp[i] = max(dp[i-1], money + prices[i])
            money = max(money, dp[i-2]-prices[i])
        
        return dp[-1]