class Solution:
    def canCompleteCircuit(self, gas: list, cost: list) -> int:
        curGas = 0
        start = 0
        totalGas = 0
        
        for i in range(len(gas)):
            curGas += gas[i] - cost[i]
            totalGas += gas[i] - cost[i]
            
            if curGas < 0:
                start = i+1
                curGas = 0

        if totalGas < 0: return -1
        else: return start