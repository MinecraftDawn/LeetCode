class Solution:
    def pacificAtlantic(self, matrix: list) -> list:
        if not matrix: return []
        self.matrix = matrix
        self.rows = len(self.matrix)
        self.cols = len(self.matrix[0])
        ans = []
        self.hasArr = [[[False, False] for _ in range(self.cols)] for _ in range(self.rows)]

        for row in range(self.rows):
            for col in range(self.cols):
                visited = [[False for _ in range(self.cols)] for _ in range(self.rows)]
                visited[row][col] = True
                if self.dfs(row, col, visited) == [True, True]:
                    ans.append((row, col))

        return ans

    def dfs(self, row: int, col: int, visited: list):
        curVal = self.matrix[row][col]
        for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nxtRow = row + i
            nxtCol = col + j
            if nxtRow < 0 or nxtCol < 0:
                self.hasArr[row][col][0] = True
            elif nxtRow >= self.rows or nxtCol >= self.cols:
                self.hasArr[row][col][1] = True
            else:
                nxtVal = self.matrix[nxtRow][nxtCol]
                if nxtVal <= curVal:
                    if visited[nxtRow][nxtCol]:
                        t1, t2 = self.hasArr[nxtRow][nxtCol]
                        self.hasArr[row][col] = [self.hasArr[row][col][0] or t1, self.hasArr[row][col][1] or t2]
                    else:
                        visited[nxtRow][nxtCol] = True
                        t1, t2 = self.dfs(nxtRow, nxtCol, visited)
                        self.hasArr[row][col] = [self.hasArr[row][col][0] or t1, self.hasArr[row][col][1] or t2]

        return self.hasArr[row][col]