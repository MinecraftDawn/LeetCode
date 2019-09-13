class Solution:
    def maxProfit(self, prices: list) -> int:
        buy = [-2e30,-2e30]
        sell = [0,0]
        
        for price in prices:
            buy[0] = max(buy[0], -price)
            sell[0] = max(sell[0], buy[0] + price)
            buy[1] = max(buy[1], sell[0] - price)
            sell[1] = max(sell[1], buy[1] + price)
        return sell[1]