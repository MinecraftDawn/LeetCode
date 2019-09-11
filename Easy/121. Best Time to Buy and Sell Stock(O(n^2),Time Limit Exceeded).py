class Solution:
    def maxProfit(self, prices: list) -> int:
        days = len(prices)
        profit = 0
        
        for i in range(days-1):
            for j in range(i+1,days):
                profit = min(profit,prices[i] - prices[j])
                
        return -profit