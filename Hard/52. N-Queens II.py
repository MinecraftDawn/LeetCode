class Solution:
    def totalNQueens(self, n: int) -> int:
        self.size = n
        self.ans = 0
        self.dfs([],0)
        
        return self.ans
    
    def dfs(self,inPuzzle,curRow):
        if curRow == self.size:
            self.ans += 1
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