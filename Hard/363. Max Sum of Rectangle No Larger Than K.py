class Solution:
    def maxSumSubmatrix(self, matrix: list, k: int) -> int:
        self.matrix = matrix
        row = len(matrix)
        col = len(matrix[0])
        self.dp = [[0] * (col+1) for _ in range(row)]
        
        for i in range(row):
            for j in range(col):
                self.dp[i][j] = self.dp[i][j-1] + matrix[i][j]
        
        ans = float("-inf")
        
        for r in range(row):
            for c in range(col):
                for i in range(row-r):
                    for j in range(col-c):
                        curSum = self.getSum(i,j,i+r,j+c)
                        if curSum <= k:
                            ans = max(ans, curSum)
                            
        return ans
                    
    def getSum(self, x1, y1, x2, y2) -> int:
        ans = 0
        for i in range(x1, x2+1):
            ans += self.dp[i][y2] - self.dp[i][y1-1]
        
        return ans