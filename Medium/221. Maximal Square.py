class Solution:
    def maximalSquare(self, matrix: list) -> int:
        if not matrix or not matrix[0]: return 0
        
        dp = [[[0,0] for _ in range(len(matrix[0])+1)] for _ in range(len(matrix)+1)]
        maxSquare = 0
        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                element = matrix[row][col]
                if element == "1":
                    dp[row+1][col+1][0] = min(dp[row+1][col][0] + 1, dp[row][col][0]+1)
                    dp[row+1][col+1][1] = min(dp[row][col+1][1] + 1, dp[row][col][1]+1)
                    maxSquare = max(maxSquare, min(dp[row+1][col+1]))
        
        return maxSquare**2