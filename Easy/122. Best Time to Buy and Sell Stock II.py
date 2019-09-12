class Solution:
    def maxProfit(self, prices: list) -> int:
        if not prices: return 0
        
        upDown = []
        upDown.append(prices[0])
        switch = False
        money = 0
        
        for i in prices:
            tail = upDown[-1]
            if switch:
                if i >= tail:
                    upDown[-1] = i
                else:
                    upDown.append(i)
                    switch = not switch
            else:
                if i <= tail:
                    upDown[-1] = i
                else:
                    upDown.append(i)
                    switch = not switch
            
        while len(upDown) >= 2:
            money += -upDown.pop(0) + upDown.pop(0)
            
        return money