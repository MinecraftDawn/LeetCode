class Solution:
    def minPathSum(self, grid: list) -> int:
        if not grid: return 0
        
        dp = [[2**20] * (len(grid[0])+1) for _ in range(len(grid)+1)]
        dp[0][1] = 0
        for rowNum,row in enumerate(grid):
            for colNum,element in enumerate(row):
                dp[rowNum+1][colNum+1] = min(dp[rowNum][colNum+1],dp[rowNum+1][colNum]) + element

        return dp.pop().pop()