class Solution:
    def minimumTotal(self, triangle: list) -> int:
        self.triangle = triangle
        self.minSize = 2e30
        self.height = len(triangle) - 1
        
        self.dfs(triangle[0][0], 0, 0)
        return self.minSize
    
    def dfs(self, num, row, index):
        if row == self.height:
            self.minSize = min(self.minSize,num)
            return
        else:
            leftVal = num + self.triangle[row+1][index]
            rightVal = num + self.triangle[row+1][index+1]
            self.dfs(leftVal, row+1, index)
            self.dfs(rightVal, row+1, index+1)