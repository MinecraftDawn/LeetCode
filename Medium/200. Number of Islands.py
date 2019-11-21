class Solution:
    def numIslands(self, grid: list) -> int:
        if not grid: return 0
        rowLen = len(grid)
        colLen = len(grid[0])
        dp = [['0'] * colLen for _ in range(rowLen)]
        
        def search(row, col):
            if row < 0 or row >= rowLen \
            or col < 0 or col >= colLen: return
            
            if dp[row][col] == '1': return
            if grid[row][col] == '0': return
            dp[row][col] = '1'
            
            search(row+1, col)
            search(row, col+1)
            search(row-1, col)
            search(row, col-1)
            
        
        ans = 0
        for rowNum,row in enumerate(grid):
            for colNum,ele in enumerate(row):
                if ele == '1' and dp[rowNum][colNum] == '0':
                    ans += 1
                    search(rowNum, colNum)
                    
        return ans