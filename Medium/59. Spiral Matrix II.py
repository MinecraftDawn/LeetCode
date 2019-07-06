class Solution:
    def generateMatrix(self, n: int) -> list:
        ans = [[0] * n for _ in range(n)]
        
        num = 1
        curList = ans
        layer = 0
        
        while num <= n**2:
            for i in range(layer,n - layer):
                curList[layer][i] = num
                num += 1
            
            if  num > n**2: break
            for i in range(layer+1, n-layer):
                curList[i][-1-layer] = num
                num += 1
            
            if  num > n**2: break
            for i in range(n-2-layer, -1+layer, -1):
                curList[-1-layer][i] = num
                num += 1
            
            if  num > n**2: break
            for i in range(n-2-layer,layer,-1):
                curList[i][layer] = num
                num += 1
            
            layer += 1
        return ans