class Solution:
    def maxSumSubmatrix(self, matrix: list, k: int) -> int:
        if not matrix or not matrix[0]: return 0
        
        row = len(matrix)
        col = len(matrix[0])
        
        if row > col:
            matrix = list(zip(*matrix))
            row,col = col,row
            
        self.matrix = matrix
        self.dp = [[0] * (col+1) for _ in range(row+1)]
        
        for i in range(row):
            for j in range(col):
                self.dp[i+1][j+1] = self.dp[i][j+1] + self.dp[i+1][j] + matrix[i][j] - self.dp[i][j]
        
        for i in self.dp:
            print(i)
        
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
        return self.dp[x2+1][y2+1] - self.dp[x1][y2+1] - self.dp[x2+1][y1] + self.dp[x1][y1]
                   