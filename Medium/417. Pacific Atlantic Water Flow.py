from collections import deque


class Solution:
    def pacificAtlantic(self, matrix: list) -> list:
        if not matrix: return []
        self.matrix = matrix
        self.rows = len(self.matrix)
        self.cols = len(self.matrix[0])
        self.ans = []

        for row in range(self.rows):
            for col in range(self.cols):
                self.bfs(row, col)

        return self.ans

    def bfs(self, row: int, col: int):
        visited = [[False for _ in range(self.cols)] for _ in range(self.rows)]
        visited[row][col] = True
        arrive = [False, False]

        queue = deque([(row, col)])
        while queue:
            curRow, curCol = queue.popleft()
            curVal = self.matrix[curRow][curCol]
            for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nxtRow = curRow + i
                nxtCol = curCol + j
                if nxtRow < 0 or nxtCol < 0:
                    arrive[0] = True
                    if arrive[1]:
                        self.ans.append((row, col))
                        return
                elif nxtRow >= self.rows or nxtCol >= self.cols:
                    arrive[1] = True
                    if arrive[0]:
                        self.ans.append((row, col))
                        return
                else:
                    nxtVal = self.matrix[nxtRow][nxtCol]

                    if nxtVal <= curVal and not visited[nxtRow][nxtCol]:
                        queue.append((nxtRow, nxtCol))
                    visited[nxtRow][nxtCol] = True