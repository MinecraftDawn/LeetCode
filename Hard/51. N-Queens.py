class Solution:
    def solveNQueens(self, n: int) -> list:
        self.size = n
        self.ans = []
        self.dfs([],0)
        
        return self.ans
    
    def dfs(self,inPuzzle,curRow):
        if curRow == self.size:
            puzzle = self.generatePuzzle(inPuzzle)
            self.ans.append(puzzle)
            return
        
        searchRow = set(list(range(self.size)))
        for row,col in inPuzzle:
            searchRow -= set([col])
            searchRow -= set([curRow-row+col])
            searchRow -= set([col-(curRow-row)])
        
        for i in searchRow:
            nextInPuzzle = inPuzzle.copy()
            nextInPuzzle.append((curRow,i))
            
            self.dfs(nextInPuzzle,curRow+1)
            
        
    def generatePuzzle(self,inPuzzle):
        puzzle = ['.' * self.size for _ in range(self.size)]
        for row,col in inPuzzle:
            puzzle[row] = puzzle[row][:col] + 'Q' +puzzle[row][col+1:]
            
        return puzzle