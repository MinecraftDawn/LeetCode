class Solution:
    def maxProfit(self, prices: list) -> int:
        if not prices: return 0
        profit = 0
        days = len(prices)
        curMin = prices[0]
        
        for i in range(1,days):
            if curMin > prices[i]: curMin = prices[i]
            else: profit = max(profit, prices[i]-curMin)

        return profit