class Solution:
    def exist(self, board: list, word: str) -> bool:
        if not word: return True
        if not board: return False
        
        self.board = board
        self.boardCol = len(board[0])
        self.boardRow = len(board)
        
        for rowNum,row in enumerate(board):
            for colNum,element in enumerate(row):
                if element == word[0]:
                    if self.dfs(rowNum,colNum,[],word[1:]):
                        return True
        
        return False
                    
    def dfs(self, row, col, filled, word):
        if not word: return True
        filled.append([row,col])
        nowFilled = filled.copy()
        
        if row - 1 >= 0:
            if [row-1,col] not in filled:
                if word[0] == self.board[row-1][col]:
                    nowFilled = filled.copy()
                    if self.dfs(row-1,col,nowFilled,word[1:]): return True
                    
        if row + 1 <= self.boardRow - 1:
            if [row+1,col] not in filled:
                if word[0] == self.board[row+1][col]:
                    nowFilled = filled.copy()
                    if self.dfs(row+1,col,nowFilled,word[1:]): return True
                    
        if col - 1 >= 0:
            if [row,col-1] not in filled:
                if word[0] == self.board[row][col-1]:
                    nowFilled = filled.copy()
                    if self.dfs(row,col-1,nowFilled,word[1:]): return True
                    
        if col + 1 <= self.boardCol - 1:
            if [row,col+1] not in filled:
                if word[0] == self.board[row][col+1]:
                    nowFilled = filled.copy()
                    if self.dfs(row,col+1,nowFilled,word[1:]): return True
       
        return False