class Solution:
    
    charList = '123456789'
    
    def solveSudoku(self, board: list) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        self.signelAnser(board)
        
        self.dfs(board)
        
    def signelAnser(self,board) -> None:
        emptyBox = 81
        
        while self.emptyBoxNums(board) != emptyBox:
            emptyBox = self.emptyBoxNums(board)
            for rowCount,row in enumerate(board):
                
                for element in self.charList:
                    if element in row: continue
                    emptyRow = self.findRowEmptyPosition(board,rowCount)
                    runRow = emptyRow.copy()
                    for i in runRow:
                        if self.checkBlockHasNum(board,rowCount,i,element) \
                        or self.checkColHasNum(board,i,element):
                            emptyRow.remove(i)
                            
                    if len(emptyRow) == 1:
                        board[rowCount][emptyRow[0]] = element
                
            for colCount,col in enumerate(zip(*board)):
    
                for element in self.charList:
                    if element in col: continue
                    emptyCol = self.findColEmptyPosition(board,colCount)
                    runCol = emptyCol.copy()
                    for i in runCol:
                        if self.checkBlockHasNum(board,i,colCount,element) \
                        or self.checkRowHasNum(board,i,element):
                            emptyCol.remove(i)
                            
                    if len(emptyCol) == 1:
                        board[emptyCol[0]][colCount] = element
                    
            for row in range(9):
                for col in range(9):
                    numList = []
                    if board[row][col] != '.': continue
                    for number in range(1,10):
                        if self.checkBlockHasNum(board,row,col,number) \
                        or self.checkColHasNum(board,col,number) \
                        or self.checkRowHasNum(board,row,number):
                            numList.append(str(number))
                            
                    if len(numList) == 8:
                        num = [i for i in self.charList if i not in numList]
                        board[row][col] = str(num[0])
                    
        return 
    
    def dfs(self,board):
        emptyBox = self.emptyBoxNums(board)
        if emptyBox == 0: return True
        
        row,col = self.findEmptyBox(board)
        
        for num in range(1,10):
            if not self.checkBlockHasNum(board,row,col,num) \
            and not self.checkColHasNum(board,col,num) \
            and not self.checkRowHasNum(board,row,num):
                board[row][col] = str(num)
                
                if self.dfs(board):
                    return True
                
                board[row][col] = '.'
            
        return False
    
    def findEmptyBox(self,board):
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    return (row,col)
        return (0,0)
    
    def emptyBoxNums(self,board):
        emptyBox = 0 
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    emptyBox += 1
                    
        return emptyBox
                
    def checkBlockHasNum(self,board,row,col,num) -> bool:
        blockCol = col // 3 * 3
        blockRow = row // 3 * 3
        num = str(num)
        for col in range(3):
            for row in range(3):
                if board[blockRow+row][blockCol+col] == '.': continue
                elif board[blockRow+row][blockCol+col] == num:
                    return True 
        return False
    
    def checkRowHasNum(self,board,row,num) -> bool:
        num = str(num)
        for ele in board[row]:
            if ele == num:
                return True
        return False
    
    def checkColHasNum(self,board,col,num) -> bool:
        num = str(num)
        for row in range(9):
            if board[row][col] == num:
                return True
        return False
    
    def findRowEmptyPosition(self,board,row) -> bool:
        rowEmpty = []
        for col in range(9):
            if board[row][col] == '.':
                rowEmpty.append(col)
        return rowEmpty
    
    def findColEmptyPosition(self,board,col) -> bool:
        colEmpty = []
        for row in range(9):
            if board[row][col] == '.':
                colEmpty.append(row)
        return colEmpty