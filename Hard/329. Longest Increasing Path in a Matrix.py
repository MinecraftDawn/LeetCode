class Solution:
    def longestIncreasingPath(self, matrix: list) -> int:
        visted = [[False] * len(matrix[0]) for _ in range(len(matrix))]
        
        def dfs(row:int, col:int):
#            print(row,col)
            
            curVal = matrix[row][col]
            visted[row][col] = True
            left = right = up = down = 0
            if col - 1 >= 0 and not visted[row][col-1] and matrix[row][col-1] > curVal:
                left = dfs(row, col-1)
                
            if col + 1 < len(matrix[0]) and not visted[row][col+1] and matrix[row][col+1] > curVal:
                right = dfs(row, col+1)
                
            if row - 1 >= 0 and not visted[row-1][col] and matrix[row-1][col] > curVal:
                up = dfs(row-1, col)
                
            if row + 1 < len(matrix) and not visted[row+1][col] and matrix[row+1][col] > curVal:
                down = dfs(row+1, col)
                
            visted[row][col] = False
            
#            print((left, right, up, down))
            return max((left, right, up, down))+1
                    
    
        maxPath = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                maxPath = max(maxPath, dfs(row, col))
                
        return maxPath