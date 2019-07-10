class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list) -> int:
        if not obstacleGrid: return 0
        
        dp = [[0] * len(obstacleGrid[0]) for _ in range(len(obstacleGrid))]
        
        canGo = 1
        for c,i in enumerate(obstacleGrid[0]):
            if i: canGo = 0
            dp[0][c] = canGo
        
        canGo = 1
        for c,i in enumerate(list(zip(*obstacleGrid))[0]):
            if i: canGo = 0
            dp[c][0] = canGo
        
        for rc,row in enumerate(obstacleGrid[1:]):
            for lc,col in enumerate(row[1:]):
                if not col:
                    dp[rc+1][lc+1] = dp[rc][lc+1] + dp[rc+1][lc]
                
        return dp.pop().pop()