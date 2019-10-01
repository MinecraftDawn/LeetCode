class Solution:
    def canCompleteCircuit(self, gas: list, cost: list) -> int:
        find = False
        for i in range(len(cost)):
            curGas = 0
            for j in range(i,i+len(cost)):
                index = j % len(cost)
                curGas += gas[index]
                curGas -= cost[index]
                if curGas < 0:
                    break
                if j == i+len(cost)-1:
                    find = True
                    
            if find: return i
            
        return -1