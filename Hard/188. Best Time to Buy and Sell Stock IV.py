class Solution:
    def maxProfit(self, k: int, prices: list) -> int:
        if not prices: return 0
        
        newPrices = []
        newPrices.append(prices[0])
        switch = False
        for i in prices:
            tail = newPrices[-1]
            if switch:
                if i >= tail:
                    newPrices[-1] = i
                else:
                    newPrices.append(i)
                    switch = not switch
            else:
                if i <= tail:
                    newPrices[-1] = i
                else:
                    newPrices.append(i)
                    switch = not switch            
        
        
        if k >= len(newPrices):
            return self.orderN(newPrices)
        
        buy = [float('-inf')] * (k+1)
        sell = [0] * (k+1)
        
        for price in prices:
            for i in range(1,k+1):
                buy[i] = max(buy[i], sell[i-1]-price)
                sell[i] = max(sell[i], buy[i] + price)
                
        return sell[k]
    
    def orderN(self, prices: list):
        money = 0
        while len(prices) >= 2:
            money += -prices.pop(0) + prices.pop(0)
        return money