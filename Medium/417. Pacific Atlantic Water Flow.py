class Solution:
    def pacificAtlantic(self, matrix: list) -> list:
        if not matrix: return []
        self.matrix = matrix
        self.rows = len(self.matrix)
        self.cols = len(self.matrix[0])
        pacific = set()
        atlantic = set()

        for i in range(self.cols):
            pacific.add((0, i))
            self.dfs(0, i, pacific)
            atlantic.add((self.rows-1, i))
            self.dfs(self.rows-1, i, atlantic)

        for i in range(self.rows):
            pacific.add((i, 0))
            self.dfs(i, 0, pacific)
            atlantic.add((i, self.cols-1))
            self.dfs(i, self.cols-1, atlantic)
        
        return pacific & atlantic

    def dfs(self, row:int, col:int, ocean:set):
        value = self.matrix[row][col]

        for i,j in [(1,0), (-1,0), (0,1), (0,-1)]:
            nxtRow = row + i
            nxtCol = col + j
            if 0 <= nxtRow < self.rows and 0 <= nxtCol < self.cols:
                nxtValue = self.matrix[nxtRow][nxtCol]
                if value <= nxtValue and (nxtRow, nxtCol) not in ocean:
                    ocean.add((nxtRow, nxtCol))
                    self.dfs(nxtRow, nxtCol, ocean)
