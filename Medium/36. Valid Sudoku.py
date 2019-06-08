class Solution:
    def isValidSudoku(self, board: list) -> bool:
        for col in range(9):
            for row in range(8):
                if board[col][row] != '.':
                    if board[col][row] in board[col][row+1:]:
                        print(board[col][row],board[col][row+1:])
                        return False
        
        for col in range(8):
            for row in range(9):
                if board[col][row] != '.':
                    for run in range(col+1,9):
                        if board[col][row] == board[run][row]:
                            return False
        
        for i in range(0,9,3):
            for j in range(3):
                cusList = []
                for k in range(3):
                    cusList += board[i+k][j*3:(j+1)*3]
                for l in range(8):
                    if cusList[l] != '.':
                        for m in range(l+1,9):
                            if cusList[l] == cusList[m]:
                                return False
        
        return True