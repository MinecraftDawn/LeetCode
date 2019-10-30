#Reference: https://leetcode.com/problems/dungeon-game/discuss/364108/Python3-simple-and-easy-to-understand

class Solution:
    def calculateMinimumHP(self, dungeon: list) -> int:
        row = len(dungeon)
        col = len(dungeon[0])
        dp = [[float('inf')] * (col+1) for _ in range(row+1)]
        dp[-2][-1] = 1
        dp[-1][-2] = 1
        for i in range(row-1, -1, -1):
            for j in range(col-1, -1, -1):
                dp[i][j] = max(min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j], 1)
            
        return dp[0][0]